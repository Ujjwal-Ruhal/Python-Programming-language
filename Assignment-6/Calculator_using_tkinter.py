from tkinter import *
window= Tk()
window.geometry('400x500')
window.title('Calculator using Tkinter')

# create a entry box
e = Entry(window , width=65 ,borderwidth=4 )
e.place(x=0 , y= 0)

# create buttons ( 0 - 9 )
b = Button(window, text='7', width=12)
b.place(x=10 , y=120)

b = Button(window, text='8', width=12)
b.place(x=100 , y=120)

b = Button(window, text='9', width=12)
b.place(x=190 , y=120)

b = Button(window, text='4', width=12)
b.place(x=10 , y=180)

b = Button(window, text='5', width=12)
b.place(x=100 , y=180)

b = Button(window, text='6', width=12)
b.place(x=190 , y=180)

b = Button(window, text='1', width=12)
b.place(x=10 , y=240)

b = Button(window, text='2', width=12)
b.place(x=100 , y=240)

b = Button(window, text='3', width=12)
b.place(x=190 , y=240)

b = Button(window, text='0', width=25)
b.place(x=10 , y=300)

b = Button(window, text='.', width=12)
b.place(x=190 , y=300)

# b = Button(window, text='1', width=12)
# b.place(x=10 , y=60)

# b = Button(window, text='1', width=12)
# b.place(x=10 , y=60)

# b = Button(window, text='1', width=12)
# b.place(x=10 , y=60)

# b = Button(window, text='1', width=12)
# b.place(x=10 , y=60)

# b = Button(window, text='1', width=12)
# b.place(x=10 , y=60)
mainloop()