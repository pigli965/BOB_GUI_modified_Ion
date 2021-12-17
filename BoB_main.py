from tkinter import *
#from relays_class import *
import os

from address_dictionar import *
#function for buttons



alist = [1,2,4,8,16,32,64,128]
blist = [1,2,4,8,16,32,64,128] 

def onoff1():
    if button1.cget("text") == 'OFF':
        button1.configure(text='ON', fg='Green', relief=SUNKEN)
        alist[0]=0
    elif button1.cget("text") == 'ON':
        button1.configure(text='OFF', fg='Red', relief=RAISED)
        alist[0]=1
def onoff2():
    if button2.cget("text") == 'OFF':
        button2.configure(text='ON', fg='Green', relief=SUNKEN)
        alist[1]=0
    elif button2.cget("text") == 'ON':
        button2.configure(text='OFF', fg='Red', relief=RAISED)
        alist[1]=2
def onoff3():
    if button3.cget("text") == 'OFF':
        button3.configure(text='ON', fg='Green', relief=SUNKEN)
        alist[2]=0
    elif button3.cget("text") == 'ON':  
        button3.configure(text='OFF', fg='Red', relief=RAISED)
        alist[2]=4
def onoff4():
    if button4.cget("text") == 'OFF':  
        button4.configure(text='ON', fg='Green', relief=SUNKEN)
        alist[3]=0
    elif button4.cget("text") == 'ON': 
        button4.configure(text='OFF', fg='Red', relief=RAISED)
        alist[3]=8
def onoff5():
    if button5.cget("text") == 'OFF':
        button5.configure(text='ON', fg='Green', relief=SUNKEN)
        alist[4]=0
    elif button5.cget("text") == 'ON':
        button5.configure(text='OFF', fg='Red', relief=RAISED)
        alist[4]=16
def onoff6():
    if button6.cget("text") == 'OFF':
        button6.configure(text='ON', fg='Green', relief=SUNKEN)
        alist[5]=0
    elif button6.cget("text") == 'ON':
        button6.configure(text='OFF', fg='Red', relief=RAISED)
        alist[5]=32
def onoff7():
    if button7.cget("text") == 'OFF':
        button7.configure(text='ON', fg='Green', relief=SUNKEN)
        alist[6]=0
    elif button7.cget("text") == 'ON':
        button7.configure(text='OFF', fg='Red', relief=RAISED)
        alist[6]=64
def onoff8():
    if button8.cget("text") == 'OFF':
        button8.configure(text='ON', fg='Green', relief=SUNKEN)
        alist[7]=0
    elif button8.cget("text") == 'ON':
        button8.configure(text='OFF', fg='Red', relief=RAISED)
        alist[7]=128
def onoff9():
    if button9.cget("text") == 'OFF':
        button9.configure(text='ON', fg='Green', relief=SUNKEN)
        blist[0]=0
    elif button9.cget("text") == 'ON':
        button9.configure(text='OFF', fg='Red', relief=RAISED)
        blist[0]=1
def onoff10():
    if button10.cget("text") == 'OFF':
        button10.configure(text='ON', fg='Green', relief=SUNKEN)
        blist[1]=0
    elif button10.cget("text") == 'ON':
        button10.configure(text='OFF', fg='Red', relief=RAISED)
        blist[1]=2
def onoff11():
    if button11.cget("text") == 'OFF':
        button11.configure(text='ON', fg='Green', relief=SUNKEN)
        blist[2]=0
    elif button11.cget("text") == 'ON':  
        button11.configure(text='OFF', fg='Red', relief=RAISED)
        blist[2]=4
def onoff12():
    if button12.cget("text") == 'OFF':  
        button12.configure(text='ON', fg='Green', relief=SUNKEN)
        blist[3]=0
    elif button12.cget("text") == 'ON': 
        button12.configure(text='OFF', fg='Red', relief=RAISED)
        blist[3]=8
def onoff13():
    if button13.cget("text") == 'OFF':
        button13.configure(text='ON', fg='Green', relief=SUNKEN)
        blist[4]=0
    elif button13.cget("text") == 'ON':
        button13.configure(text='OFF', fg='Red', relief=RAISED)
        blist[4]=16
def onoff14():
    if button14.cget("text") == 'OFF':
        button14.configure(text='ON', fg='Green', relief=SUNKEN)
        blist[5]=0
    elif button14.cget("text") == 'ON':
        button14.configure(text='OFF', fg='Red', relief=RAISED)
        blist[5]=32
def onoff15():
    if button15.cget("text") == 'OFF':
        button15.configure(text='ON', fg='Green', relief=SUNKEN)
        blist[6]=0
    elif button15.cget("text") == 'ON':
        button15.configure(text='OFF', fg='Red', relief=RAISED)
        blist[6]=64
def onoff16():
    if button16.cget("text") == 'OFF':
        button16.configure(text='ON', fg='Green', relief=SUNKEN)
        blist[7]=0
    elif button16.cget("text") == 'ON':
        button16.configure(text='OFF', fg='Red', relief=RAISED)
        blist[7]=128
        

def onoffR():   
        a=sum(alist)
        b=sum(blist)
        board1_Write(a,b)
     

#create window object 
root =Tk()
root.title(" Automate BoB ")
root.geometry('950x300')


#canvas 
canvas = Canvas(root, height = 100, width = 700, bg = '#066450')
canvas.place()

#relay lables
re1_text = StringVar()
re1_label = Label(root, text = 'Relay 1', font = ('bold', 12),padx = 20)
re1_label.grid(row=3, column = 1)

re2_text = StringVar()
re2_label = Label(root, text = 'Relay 2', font = ('bold', 12),padx = 20)
re2_label.grid(row=3, column = 2)

re3_text = StringVar()
re3_label = Label(root, text = 'Relay 3', font = ('bold', 12),padx = 20)
re3_label.grid(row=3, column = 3)

re4_text = StringVar()
re4_label = Label(root, text = 'Relay 4', font = ('bold', 12),padx = 20)
re4_label.grid(row=3, column = 4)

re5_text = StringVar()
re5_label = Label(root, text = 'Relay 5', font = ('bold', 12),padx = 20)
re5_label.grid(row=3, column = 5)

re6_text = StringVar()
re6_label = Label(root, text = 'Relay 6', font = ('bold', 12),padx = 20)
re6_label.grid(row=3, column = 6)

re7_text = StringVar()
re7_label = Label(root, text = 'Relay 7', font = ('bold', 12),padx = 20)
re7_label.grid(row=3, column = 7)

re8_text = StringVar()
re8_label = Label(root, text = 'Relay 8', font = ('bold', 12),padx = 20)
re8_label.grid(row=3, column = 8)

re9_text = StringVar()
re9_label = Label(root, text = 'Relay 9', font = ('bold', 12),padx = 20, pady =20)
re9_label.grid(row=7, column = 1)

re10_text = StringVar()
re10_label = Label(root, text = 'Relay 10', font = ('bold', 12),padx = 20, pady =20)
re10_label.grid(row=7, column = 2)

re11_text = StringVar()
re11_label = Label(root, text = 'Relay 11', font = ('bold', 12),padx = 20, pady =20)
re11_label.grid(row=7, column = 3)

re12_text = StringVar()
re12_label = Label(root, text = 'Relay 12', font = ('bold', 12),padx = 20, pady =20)
re12_label.grid(row=7, column = 4)

re13_text = StringVar()
re13_label = Label(root, text = 'Relay 13', font = ('bold', 12),padx = 20, pady =20)
re13_label.grid(row=7, column = 5)

re14_text = StringVar()
re14_label = Label(root, text = 'Relay 14', font = ('bold', 12),padx = 20, pady =20)
re14_label.grid(row=7, column = 6)

re15_text = StringVar()
re15_label = Label(root, text = 'Relay 15', font = ('bold', 12),padx = 20,pady =20)
re15_label.grid(row=7, column = 7)

re16_text = StringVar()
re16_label = Label(root, text = 'Relay 16', font = ('bold', 12),padx = 20, pady =20)
re16_label.grid(row=7, column = 8)



#buttons
button1 = Button(root, text='OFF', command=onoff1, fg='Red')
button1.grid(row=4, column=1, pady=5, padx=5)

button2 = Button(root, text='OFF', command=onoff2, fg='Red')
button2.grid(row=4, column=2, pady=5, padx=5)

button3 = Button(root, text='OFF', command=onoff3, fg='Red')
button3.grid(row=4, column=3, pady=5, padx=5)

button4 = Button(root, text='OFF', command=onoff4, fg='Red')
button4.grid(row=4, column=4, pady=5, padx=5)

button5 = Button(root, text='OFF', command=onoff5, fg='Red')
button5.grid(row=4, column=5, pady=5, padx=5)

button6 = Button(root, text='OFF', command=onoff6, fg='Red')
button6.grid(row=4, column=6, pady=5, padx=5)

button7 = Button(root, text='OFF', command=onoff7, fg='Red')
button7.grid(row=4, column=7, pady=5, padx=5)

button8 = Button(root, text='OFF', command=onoff8, fg='Red')
button8.grid(row=4, column=8, pady=5, padx=5)

button9 = Button(root, text='OFF', command=onoff9, fg='Red')
button9.grid(row=8, column=1, pady=5, padx=5)

button10 = Button(root, text='OFF', command=onoff10, fg='Red')
button10.grid(row=8, column=2, pady=5, padx=5)

button11 = Button(root, text='OFF', command=onoff11, fg='Red')
button11.grid(row=8, column=3, pady=5, padx=5)

button12 = Button(root, text='OFF', command=onoff12, fg='Red')
button12.grid(row=8, column=4, pady=5, padx=5)

button13 = Button(root, text='OFF', command=onoff13, fg='Red')
button13.grid(row=8, column=5, pady=5, padx=5)

button14 = Button(root, text='OFF', command=onoff14, fg='Red')
button14.grid(row=8, column=6, pady=5, padx=5)

button15 = Button(root, text='OFF', command=onoff15, fg='Red')
button15.grid(row=8, column=7, pady=5, padx=5)

button16 = Button(root, text='OFF', command=onoff16, fg='Red')
button16.grid(row=8, column=8, pady=5, padx=5)

btReady = Button(root, text='READY', command=onoffR, fg='Green')
btReady.grid(row=12, column=4, pady=5, padx=5)

#define menu 

options = ["Board1","Board2","Board3"]
clicked = StringVar()
clicked.set(options[0])
drop=OptionMenu(root,clicked,*options)
drop.config(width=9, font=('bold',12))
drop.grid(row=1, column=1, pady=5, padx=5)


#run

root.mainloop()



