from tkinter import *
import time;
import datetime
import pygame

pygame.init()
root =Tk()
root.title("Super Pianino")
root.geometry('1352x700+0+0')
root.configure(background='medium orchid')

ABC = Frame(root, bg="powder blue",bd=20, relief=RIDGE)
ABC.grid()
ABC1 = Frame(root, bg="plum3",bd=20,cursor ="hand2", relief=RIDGE)
ABC1.grid()
ABC2 = Frame(root, bg="powder blue", relief=RIDGE)
ABC2.grid()
ABC3 = Frame(root, bg="powder blue",relief=RIDGE)
ABC3.grid()

str1 = StringVar()
str1.set("Gama C-dur")
Date1 = StringVar()
Time1 = StringVar()
Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))

Label(ABC1, text = "Piano Musical Keys", font=('times',28,'bold'), padx=8, pady = 8, bd=4, bg = 'orchid3',
fg ="bisque", justify=CENTER).grid(row=0,column=0, columnspan=8)

textDate=Entry(ABC1, textvariable=Date1, font=('arial',18,'bold'),bd=20,bg="orchid3",fg="bisque",width=22, cursor ="hand2",justify=CENTER).grid(row=1,column=0,pady=1)

textDisplay=Entry(ABC1, textvariable=str1, font=('times',22,'bold'),bd=20,bg="orchid3", fg="bisque",width=36,cursor ="hand2", justify=CENTER).grid(row=1,column=1,pady=1)

textTime=Entry(ABC1, textvariable=Time1, font=('arial',18,'bold'),bd=20,bg="orchid3", fg="bisque",width=22,cursor ="hand2", justify=CENTER).grid(row=1,column=2,pady=1)



btnCs = Button(ABC2, height=6, width = 5, bd=4, text="C#", font=('arial',18,'bold'), bg="black", fg="white")
btnCs.grid(row=0,column=0,padx=5,pady=5)

btnSpace2 = Button(ABC2, state=DISABLED, height=6, width = 2,bg="plum3", relief=FLAT)
btnSpace2.grid(row=0,column=1,padx=0,pady=0)

btnDs = Button(ABC2, height=6, width = 5, bd=4, text="D#", font=('arial',18,'bold'), bg="black", fg="white")
btnDs.grid(row=0,column=2,padx=5,pady=5)

btnSpace3 = Button(ABC2, state=DISABLED, height=6, width =9,bg="plum3", relief=FLAT)
btnSpace3.grid(row=0,column=3,padx=0,pady=0)

btnFs = Button(ABC2, height=6, width = 5, bd=4, text="F#", font=('arial',18,'bold'), bg="black", fg="white",cursor ="hand2")
btnFs.grid(row=0,column=4,padx=5,pady=5)

btnSpace4 = Button(ABC2, state=DISABLED, height=6, width = 2,bg="plum3", relief=FLAT)
btnSpace4.grid(row=0,column=5,padx=0,pady=0)

btnGs = Button(ABC2, height=6, width = 5, bd=4, text="G#", font=('arial',18,'bold'), bg="black", fg="white",cursor ="hand2")
btnGs.grid(row=0,column=6,padx=5,pady=5)\

btnSpace5 = Button(ABC2, state=DISABLED, height=6, width = 2,bg="plum3", relief=FLAT)
btnSpace5.grid(row=0,column=7,padx=0,pady=0)

btnHs = Button(ABC2, height=6, width = 5, bd=4, text="H#", font=('arial',18,'bold'), bg="black", fg="white",cursor ="hand2")
btnHs.grid(row=0,column=8,padx=5,pady=5)


btnC= Button(ABC3, height=8, width = 6, bd=4, text="C", font=('arial',18,'bold'), bg="white", fg="black",cursor ="hand2")
btnC.grid(row=0,column=0,padx=5,pady=5)
btnD= Button(ABC3, height=8, width = 6, bd=4, text="D", font=('arial',18,'bold'), bg="white", fg="black",cursor ="hand2")
btnD.grid(row=0,column=1,padx=5,pady=5)
btnE= Button(ABC3, height=8, width = 6, bd=4, text="E", font=('arial',18,'bold'), bg="white", fg="black",cursor ="hand2")
btnE.grid(row=0,column=2,padx=5,pady=5)
btnF= Button(ABC3, height=8, width = 6, bd=4, text="F", font=('arial',18,'bold'), bg="white", fg="black",cursor ="hand2")
btnF.grid(row=0,column=3,padx=5,pady=5)

btnG= Button(ABC3, height=8, width = 6, bd=4, text="G", font=('arial',18,'bold'), bg="white", fg="black",cursor ="hand2")
btnG.grid(row=0,column=4,padx=5,pady=5)
btnA= Button(ABC3, height=8, width = 6, bd=4, text="A", font=('arial',18,'bold'), bg="white", fg="black",cursor ="hand2")
btnA.grid(row=0,column=5,padx=5,pady=5)
btnH= Button(ABC3, height=8, width = 6, bd=4, text="H", font=('arial',18,'bold'), bg="white", fg="black",cursor ="hand2")
btnH.grid(row=0,column=6,padx=5,pady=5)
btnC1= Button(ABC3, height=8, width = 6, bd=4, text="C1", font=('arial',18,'bold'), bg="white", fg="black",cursor ="hand2")
btnC1.grid(row=0,column=7,padx=5,pady=5)

root.mainloop()



