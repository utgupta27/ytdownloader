from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import os
import pydub
details = []

path = os.path.realpath('./Downloads')

def resolveLink(link):
    remove="https://www.youtube.com/watch?v="
    reslove ="https://youtu.be/"
    if link[:len(remove)] == remove :
        newLink = reslove+link[len(remove):]
        return newLink
    else:
        return link



def update():
    main.update()
    videoInfoMsg.config(
        text="Searching...(This may take time depending upon internet connection)",
        font= ("calibri",9,"bold"),
        bg='light blue'

    )
    main.update()

def getPath():
    global path
    path = filedialog.askdirectory()
    pathDisplay.config(
        text= "Location: "+path,
        font= ("calibri",12,"bold"),
        bg='light blue'
    )
    status()

def status():
    videoIndex = index.get()
    prefferedStream = videoStream[videoIndex]
    fileSize = prefferedStream.filesize
    if fileSize>1024 *1024 *1024:
        size = fileSize/(1024*1024)
        unit = " GB"
    elif fileSize > 1024*1024:
        size = fileSize//(1024) 
        unit = " MB"
    else:
        size = fileSize
        unit = " KB"
    sizeDisplay.config(
        text="File Size: "+ str(size/1024)[:4]+ unit,
        font= ("calibri",12,"bold"),
        bg='light blue'
    )

def get_video_info(url):
    global details
    update()
    yt=YouTube(url)
    main.update()
    details.append(yt.title)
    details.append(yt.rating)
    details.append(yt.length)
    details.append(yt.views)
    main.update()
    check=True
    return details
    

def get_streams(url):

    global yt
    streams = []
    main.update()
    yt= YouTube(url,on_progress_callback=progress_check)
    main.update()
    streams.append(yt.streams.get_by_itag(22))
    main.update()
    streams.append(yt.streams.get_by_itag(18))
    main.update()
    streams.append(yt.streams.get_by_itag(133))
    main.update()
    streams.append(yt.streams.get_by_itag(160))
    main.update()
    streams.append(yt.streams.get_by_itag(140))
    main.update()
    return streams
 

def getVideoDetails():
    global check   
    check =False
    global data 
    global videoStream
    videoUrl = resolveLink(inputlink.get())
    
    try:
        data= get_video_info(videoUrl)
        main.update()
        videoStream = get_streams(videoUrl)
        main.update()
    except:
        videoInfoMsg.config(
            text="Error Occured: Enter a Valid Url...",
            font= ("calibri",15,"bold"),bg='red'
            )
    else:
        videoInfoMsg.config(
            text="Video Found: Available for download ",
            font= ("calibri",15,"bold"),
            bg='light green'
            )
        videoTitle.config(
            text="Title: "+ data[0][:19]+"...",
            font= ("calibri",10,"bold"),
            bg='light blue'
            )
        videoRating.config(
            text="Rating: "+ str(data[1])[:3],
            font= ("calibri",10,"bold"),
            bg='light blue'
            )
        if data[2]>60*60:
            size = data[2]/(60*60)
            unit = " Hrs"
        elif data[2] > 60:
            size = data[2]/(60) 
            unit = " Mins"
        else:
            size = data[2]
            unit = " Sec"
        videoDuration.config(
            text="Duration: "+ str(size)[:4]+unit,
            font= ("calibri",10,"bold"),
            bg='light blue'
            )
        videoViews.config(
            text="Views: "+ str(data[3]),
            font= ("calibri",10,"bold"),
            bg='light blue'
            )

def download():
    global fileSize
    global videoStream
    global url
    main.update()
    videoIndex = index.get()
    try:
        if check == False :
            pass
    except:
        sizeDisplay.config(
            text = "Error: Click video info. button first!",
            font= ("calibri",12,"bold"),
            bg='orange'
        )
    if videoIndex == 5:
    	prefferedStream = videoStream[videoIndex-1]
    else:
    	prefferedStream = videoStream[videoIndex]
    fileSize = prefferedStream.filesize
    try:
    	main.update()
    	finalPath = prefferedStream.download(path)

    	if videoIndex == 5:
            mp4_version = pydub.AudioSegment.from_file(finalPath, "mp4")
            name = details[0]
            location = os.path.join(path,name+".mp3")
            mp4_version.export(location, format="mp3", bitrate="160k")
            os.remove(finalPath)
    	main.update()
    
    except: 
        downloadSuccess.config(
            text="Download Failed: Download Again",
            font= ("calibri",15,"bold"),bg='red'
            )
    else:
        downloadSuccess.config(
            text="Download Success",
            font= ("calibri",15,"bold"),bg='light green'
            )

global percent
def progress_check(stream,chunk,bytes_remaining):
    percent = (100*(fileSize-bytes_remaining))//fileSize
    main.update()
    progressDisplay.config(
        text= str(percent) + "%",
        font= ("calibri",12,"bold"),
        bg='yellow'
    )
    progressBar['value'] = percent



main = Tk()
main.title('YouTube Downloader')
# main.geometry('500x600')
main.resizable(0,0)



# top frame starts here
introFrame = Frame(main)
youTubeDownloader = Label(
    introFrame,
    text='YouTube Downloader',
    padx=10,
    font=("calibri",40,'bold'),
    pady=5,
    bg='red',
    foreground = "white"
    )
youTubeDownloader.grid(
    column = 1
    )


subTitle = Label(
    introFrame,
    text='A video downloader for Youtube Videos only.',
    font= ("calibri",10,"bold")
)
subTitle.grid(
    column =1 ,
    row =1
    )

introFrame.grid(
    column = 1
    )


inputFrame = Frame(main)


inputFrame.grid(
    column = 1,
    row =1
    )

inputFrame2= Frame(main)
inputFrame2.grid(
    column =1,
    row =2,
    pady = 10
    )
enterLink = Label(
    inputFrame2,
    text='Enter Video Link: ',
    font=("calibri",12,"bold")
    )
enterLink.grid(
    column= 1  ,
    row = 1
    )

videoUrl = StringVar()
inputlink = Entry(
    inputFrame2,
    textvariable = videoUrl,
    width =50
    )
inputlink.grid(
    column= 2 ,
    row = 1
    )

findVideo= Button(
    inputFrame2,
    text = "Find Video Information",
    command = getVideoDetails
    )
findVideo.grid(
    column = 1,
    row =2,
    pady=10
    )
videoInfoMsg = Label(
    inputFrame2,
    text="e.g, link starts with 'www.youtube.com/<xyz>'",
    font=("calibri",11,"bold")
    )
videoInfoMsg.grid(
    column= 2  ,
    row = 2
    )

videoTitle = Label(
    inputFrame2,
    text="Title: ",
    font= ("calibri",10,"bold")
)
videoTitle.grid(
    column = 1,
    row =3
    )
videoDuration = Label(
    inputFrame2,
    text="Duration: ",
    font= ("calibri",10,"bold")
)
videoDuration.grid(column = 1,row =4)
videoRating = Label(
    inputFrame2,
    text="Rating: ",
    font= ("calibri",10,"bold")
)
videoRating.grid(column = 2,row =3)
videoViews = Label(
    inputFrame2,
    text="Views: ",
    font= ("calibri",10,"bold")
)
videoViews.grid(
    column = 2,
    row =4
    )

# frame 3 starts here 
frame3 = Frame(main)
frame3.grid(
    column = 1 ,
    row = 3)
space = Label(
    frame3,
    font=("calibri",15,"bold"),
    text='Select The Video Quality- '
    )
space.grid(
    column= 0,
    row = 0
    )
streamList=[
    [''' Type="video/mp4" Resolution="720p" fps="30fps"'''],
    [''' Type="video/mp4" Resolution="360p" fps="30fps"'''],
    [''' Type="video/mp4" Resolution="240p" fps="30fps"'''],
    [''' Type="video/mp4" Resolution="144p" fps="30fps"'''],
    [''' Type="audio/mp4a" Bitrate="160kbps"           '''],
    [''' Type="audio/mp3" Bitrate="160kbps"           ''']]
index = IntVar(main,1)
for i in range(len(streamList)):
    Radiobutton(
        frame3,
        text= streamList[i],
        variable = index, 
        value =i,
        command = None).grid(column = 0 , row = i+1)

frame4 = Frame(main)
frame4.grid(
    column =1 ,
    row =4
    )
downloadPathButton = Button(frame4,
    text = "Select Download Location",
    command= getPath
    )
downloadPathButton.grid(
    column= 0  ,
    row = 7,
    pady=5
    )
pathDisplay = Label(
    frame4,
    text=path,
    font=("calibri",11,"bold")
    )
pathDisplay.grid(
    column= 1  ,
    row = 7
    )


downloadButton = Button(
    frame4,
    text = "Download Selected Video",
    font=("calibri",10,"bold"),
    command = download
    )
downloadButton.grid(
    column= 1  ,
    row = 8,
    pady  = 5
    )

sizeDisplay = Label(
    frame4,
    text='File Size: '
    )
sizeDisplay.grid(
    column= 0  ,
    row = 8
    )
# implement frame 5 here
frame5 = Frame(main)
frame5.grid(column=1 ,row =5)

progressDisplay = Label(
    frame5,
    text=''
    )
progressDisplay.grid(
    column= 0  ,
    row = 0
    )

frame6= Frame(main)
frame6.grid(column =1 ,row =6)
# add the dynamic progress bar 
progressBar = ttk.Progressbar(frame6,orient=HORIZONTAL,length =450,mode ='determinate')
progressBar.grid()


frame7=Frame(main)
frame7.grid(column =1 ,row =7)
downloadSuccess = Label(
    frame7,
    text=""
    )
downloadSuccess.grid(
    column= 0  ,
    row = 0
    )

cancle = Button(
    frame7,
    text="Cancel Download & Exit",
    font=("calibri",10,"bold"),
    foreground ="red",
    command = main.destroy
    )
cancle.grid(
    column= 0  ,
    row = 1,
    pady=5
    )


main.mainloop()
