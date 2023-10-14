from tkinter import *
import matplotlib.pyplot as plt 

def get_array_input():
    input_str = entry.get()  # Get the user's input as a string
    array = [int(num) for num in input_str.split(",")]  # Convert the string into a list of integers
    days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    plt.plot(days,array,color='green',marker='o',markerfacecolor='red')
    plt.xlabel('days')
    plt.ylabel('Pushups')
    plt.title('My Analysis')
    plt.show()

root = Tk() #root is the object of the Tk Class same as OOPs concept
root.title("GUI") #Setting the tittle for the login page
root.minsize(400,400) #it helps to maintain a minimum size for the window
root.maxsize(700,700) #it helps to set a limit upto which your window can work
root.geometry('500x600') #it sets the geometry for the window
root.configure(background='blue')#setting up a background color


text_label = Label(root,text='Progress Analyzer',fg='white',bg='blue')
text_label.pack(pady=(1,15))
text_label.config(font=('verdana',25))#for displaying on the screen
name_input = Label(root,text='Your Good Name',fg='white',bg='blue')
name_input.pack(pady=(2,15))
email_input = Entry(root,width=40)
email_input.pack(ipady=5)#increases the input size in y coordinate
Label_text = Label(root,text='Enter number of pushups per days',fg='white',bg='blue')
Label_text.pack(pady=(60,15))
entry = Entry(root,width=40)
entry.pack(ipady=5)
login_button = Button(root,text='Make Analysis',fg='black',bg='white',command=get_array_input)
login_button.pack(pady=(60,15))


login_button2 = Button(root,text='Chalenge with buddy',fg='black',bg='blue')
login_button2.pack(pady=(60,5))

exit_button = Button(root,text='Analysis Done',fg='black',bg='blue',command=root.quit)
exit_button.pack(pady=(50,15))

root.mainloop() #This will help the window remain on the screen

