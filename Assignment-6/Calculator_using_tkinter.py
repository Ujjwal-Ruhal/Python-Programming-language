from tkinter import *

window= Tk()
window.geometry('385x450')
window.title('Calculator using Tkinter')
window.config( bg= "lightblue" )

# create a entry box
e = Entry(window ,borderwidth=4 , font="Bold" )
e.place(x=7 , y= 0 , width=370 , height=35, )


# create a function for click digits
def click(num):
    result = e.get()
    e.delete(0 , END)
    e.insert(0 , str(result) + str(num))

# create buttons ( 0 - 9 )
# Button - 7
b = Button(window, text='7', width=12 , bg="skyblue"  ,command=lambda:click(7) )
b.place(x=10 , y=120)

# Button - 8
b = Button(window, text='8', width=12 , bg="skyblue" , command=lambda:click(8))
b.place(x=100 , y=120)

# Button - 9
b = Button(window, text='9', width=12 , bg="skyblue" , command=lambda:click(9))
b.place(x=190 , y=120)

# Button - 4
b = Button(window, text='4', width=12 , bg="skyblue" , command=lambda:click(4))
b.place(x=10 , y=180)

# Button - 5
b = Button(window, text='5', width=12 , bg="skyblue" , command=lambda:click(5))
b.place(x=100 , y=180)

# Button - 6
b = Button(window, text='6', width=12 , bg="skyblue" , command=lambda:click(6))
b.place(x=190 , y=180)

# Button - 1
b = Button(window, text='1', width=12 , bg="skyblue" , command=lambda:click(1))
b.place(x=10 , y=240)

# Button - 2
b = Button(window, text='2', width=12 , bg="skyblue" , command=lambda:click(2))
b.place(x=100 , y=240)

# Button - 3
b = Button(window, text='3', width=12 , bg="skyblue" , command=lambda:click(3))
b.place(x=190 , y=240)

# Button - 0
b = Button(window, text='0', width=25 , bg="skyblue" , command=lambda:click(0))
b.place(x=10 , y=300)


# create opetators like ( = , + , - ,/, * )



# create function for subtraction 
def sub():
    n1 = e.get()
    global math
    math = 'subtraction'
    global i
    i = float(n1)
    e.delete(0 , END)
# Button -> -
b = Button(window, text='-', width=12 , bg="steelblue" , fg='white' , command=sub)
b.place(x=280 , y=180)


# create function for addition 
def add():
    n1 = e.get()
    global math
    math = 'addition'
    global i
    i = float(n1)
    e.delete(0 , END)
# Button -> +
b = Button(window, text='+', width=12 , bg="steelblue" , fg='white' , command=add)
b.place(x=280 , y=240)


# create function for multiplication 
def multi():
    n1 = e.get()
    global math
    math = 'multiplication'
    global i
    i = float(n1)
    e.delete(0 , END)
# Button -> *
b = Button(window, text='*', width=12 , bg="steelblue" , fg='white' , command=multi)
b.place(x=280 , y=120)


# create function for division 
def div():
    n1 = e.get()
    global math
    math = 'division'
    global i
    i = float(n1)
    e.delete(0 , END)
# Button -> /
b = Button(window, text='/', width=12 , bg="steelblue" , fg='white' , command=div)
b.place(x=280 , y=60)


# create function for clear 
def clr():
    e.delete(0 , END)
# Button -> clear
b = Button(window, text='Clear', width=37 , bg="steelblue" , fg='white' , command=clr)
b.place(x=10 , y=60)



# Button - .
b = Button(window, text='.', width=12 , bg="skyblue" , command=lambda:click('.'))
b.place(x=190 , y=300)


# create function for  equal
def equal():
    n2 = e.get()
    e.delete( 0 , END )
    if math=='addition':
        e.insert(0 , i + float(n2))
    
    elif math=='subtraction':
        e.insert(0 , i - float(n2))

    elif math=='division':
        e.insert(0 , i / float(n2))

    elif math=='multiplication':
        e.insert(0 , i * float(n2))


# Button - =
b = Button(window, text='=', width=12 , bg='blue' , fg='white' , command=equal)
b.place(x=280 , y=300)

# Add a label to say thank you
label = Label(window , text='Thanks for using this calculator' ,bg= "lightblue" , font="Bold")
label.place(x=10 , y= 400)


mainloop()