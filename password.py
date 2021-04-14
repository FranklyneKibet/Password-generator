from tkinter import *
import random 
import string
import pyperclip


#creating a window
root = Tk()
root.title('PASSWORD GENERATOR')
root.geometry('500x300')

#Adding title to PASSWORD BLOCKER
Label(root, text='PASSWORD GENERATOR APP', font='arial 20  bold').pack(pady=20)

#Choosing password length
Label(root,text='PASSWORD LENGTH :', font=('arial bold',10)).pack()
pass_len = IntVar()
length = Spinbox(root,from_=8, to_=32, textvariable=pass_len, width=15).pack()
                    
#Generating function
pass_str = StringVar()

def generate_pass():
    password = ''
    
    for x in range(0,4): 
        password = random.choice('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$)')
    for y in range(pass_len.get() - 4): 
        password = password + random.choice('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$)')
    pass_str.set(password)
    
#Generating button
Button(root,text='GENERATE', command=generate_pass,width=15).pack(pady=5)

Entry(root, textvariable=pass_str).pack()

#Copy Function
def Copy_Password(): 
    pyperclip.copy(pass_str.get())
    
#Copy Button
Button(root, text='COPY TO CLIPBOARD', command= Copy_Password,).pack(pady=5)


root.mainloop()
