from tkinter import *

main = Tk()
main.title('Testing..')
main.geometry('500x600')
main.resizable(0,0)
frame1 =Frame(main)
frame1.grid(column =0 ,row=0)
lable =Label(frame1,text="|||||||||||||||||||||||||||||||||||||||||||||||||||||||")
lable.grid()



frame2 =Frame(main)
frame2.grid(column =0 ,row=1)
lable2 =Label(frame2,text="|||||||||||||||||||djfvhdfgef||||||||||||||||||||||||||||||||||||")
lable2.pack()




main.mainloop()