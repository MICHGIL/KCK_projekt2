# KCK_projekt2
Projekt realizowany w ramach przedmiotu Komunikacja Człowiek-Komputer 

from tkinter import *
import time;
import datetime
import pygame

pygame.init()
root =Tk()
root.title("Super Pianino")
root.geometry('1352x700+0+0')
root.configure(background='white')

ABC = Frame(root, bg="powder blue",bd=20, relief=RIDGE)
ABC.grid()
ABC1 = Frame(root, bg="plum3",bd=20,cursor ="hand2", relief=RIDGE)
ABC1.grid()
ABC2 = Frame(root, bg="powder blue",bd=20, relief=RIDGE)
ABC2.grid()
ABC3 = Frame(root, bg="powder blue",bd=20, relief=RIDGE)
ABC3.grid()

str1 = StringVar()
str1.set("Gama C-dur")
Date1 = StringVar()
Time1 = StringVar()
Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))

Label(ABC1, text = "Piano Musical Keys", font=('times',28,'bold'), padx=8, pady = 8, bd=4, bg = 'orchid3',
fg ="bisque", justify=CENTER).grid(row=0,column=0, columnspan=11)

textDate=Entry(ABC1, textvariable=Date1, font=('arial',18,'bold'),bd=20,bg="orchid3",fg="bisque",width=22, cursor ="hand2",justify=CENTER).grid(row=1,column=0,pady=1)

textDisplay=Entry(ABC1, textvariable=str1, font=('times',22,'bold'),bd=20,bg="orchid3", fg="bisque",width=36,cursor ="hand2", justify=CENTER).grid(row=1,column=1,pady=1)

textTime=Entry(ABC1, textvariable=Time1, font=('arial',18,'bold'),bd=20,bg="orchid3", fg="bisque",width=22,cursor ="hand2", justify=CENTER).grid(row=1,column=2,pady=1)


root.mainloop()



