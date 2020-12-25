from pytube import YouTube
import requests
link = "https://www.youtube.com/watch?v=GO3A8vcNZbk"

# def progress_check(stream,chunk,bytes_remaining):
#     percent = (100*(file_size-bytes_remaining))/file_size
#     print("{:00.0f}% downloaded".format(percent))


yt = YouTube(link,on_progress_callback=progress_check)
# thubmnailurl = yt.thumbnail_url
# r=requests.get(thubmnailurl)
# with open("thumbnail.png",'wb') as f:
#     f.write(r.content)
# # yt = YouTube(link)

print("Title: ",yt.title)
# print("Description: ",yt.description)
print("Views: ",yt.views)
# print("Metadata: ",yt.metadata)
print("Rating: ", yt.rating)
print("Length: ",yt.length," sec")
print("\n\nVideo Streams Available : ")
for stream in yt.streams.filter():
    print(stream)
# print("\n\nAudio Streams Available : ")
# for stream in yt.streams.filter(only_audio=True):
#     print(stream)

# preferred_stream =yt.streams.get_by_itag(160)
# file_size = preferred_stream.filesize

# yt.register_on_complete_callback(progress_check)
# preferred_stream.download()