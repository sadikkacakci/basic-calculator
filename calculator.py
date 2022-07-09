from tkinter import *


root = Tk()
root.geometry('300x150')
root.title("Basic Calculator")
root.configure(background="gray")
root.resizable(False,False) 

entry1 = Entry(root,fg ="white",bg = "black")
entry1.grid(columnspan=5, ipadx=80)


islemler = ["+","-","*","/"]
def checkEntry(text):
    e_text = entry1.get()
    last_char = e_text[-1]
    last2_char = e_text[-2]
    if (last_char in islemler) and (last2_char in islemler):
        entry1.delete(len(e_text)-2,len(e_text))
        entry1.insert(END, text)


def setResult(result):
    temp_result = str(result)
    temp_list = temp_result.split(".")
    if temp_list[1] == "0":
        result = int(temp_list[0])
    entry1.delete(0,END)
    entry1.insert(0,result)


def set_text(text):
    entry1.insert(END,text) 
    if len(entry1.get()) >= 2:
        checkEntry(text)
    
    
def clear_text():
    entry1.delete(0,END)


def getResult():
    e_text=entry1.get()
    if "+" in e_text:
        values = e_text.split("+")
        result = float(values[0]) + float(values[1])  
        setResult(result)
    if "-" in e_text:
        values = e_text.split("-")
        result = float(values[0]) - float(values[1])     
        setResult(result)
    if "*" in e_text:
        values = e_text.split("*")
        result = float(values[0]) * float(values[1])  
        setResult(result)
    if "/" in e_text:
        values = e_text.split("/")
        result = float(values[0]) / float(values[1]) 
        setResult(result)

    
height_size = 1 #1
width_size = 9 #9

one_button = Button(root,text = "1",command=lambda:set_text("1"),height = height_size, width = width_size,fg = "white",bg="black")
one_button.grid(row = 2, column = 0)

two_button = Button(root,text = "2",command=lambda:set_text("2"),height = height_size, width = width_size,fg = "white",bg="black")
two_button.grid(row = 2, column = 1)

three_button = Button(root,text = "3",command=lambda:set_text("3"),height = height_size, width = width_size,fg = "white",bg="black")
three_button.grid(row = 2, column = 2)

four_button = Button(root,text = "4",command=lambda:set_text("4"),height = height_size, width = width_size,fg = "white",bg="black")
four_button.grid(row = 3, column = 0)

five_button = Button(root,text = "5",command=lambda:set_text("5"),height = height_size, width = width_size,fg = "white",bg="black")
five_button.grid(row = 3, column = 1)

six_button = Button(root,text = "6",command=lambda:set_text("6"),height = height_size, width = width_size,fg = "white",bg="black")
six_button.grid(row = 3, column = 2)

seven_button = Button(root,text = "7",command=lambda:set_text("7"),height = height_size, width = width_size,fg = "white",bg="black")
seven_button.grid(row = 4, column = 0)

eight_button = Button(root,text = "8",command=lambda:set_text("8"),height = height_size, width = width_size,fg = "white",bg="black")
eight_button.grid(row = 4, column = 1)

nine_button = Button(root,text = "9",command=lambda:set_text("9"),height = height_size, width = width_size,fg = "white",bg="black")
nine_button.grid(row = 4, column = 2)

zero_button = Button(root,text = "0",command=lambda:set_text("0"),height = height_size, width = width_size,fg = "white",bg="black")
zero_button.grid(row = 5, column = 0)

topla_button = Button(root,text = "+",command=lambda:set_text("+"),height = height_size, width = width_size,fg = "white",bg="black")
topla_button.grid(row = 2,column = 4)

cikar_button = Button(root,text = "-",command=lambda:set_text("-"),height = height_size, width = width_size,fg = "white",bg="black")
cikar_button.grid(row = 3,column = 4)

carpma_button = Button(root,text = "*",command=lambda:set_text("*"),height = height_size, width = width_size,fg = "white",bg="black")
carpma_button.grid(row = 4,column = 4)

bolme_button = Button(root,text = "/",command=lambda:set_text("/"),height = height_size, width = width_size,fg = "white",bg="black")
bolme_button.grid(row = 5,column = 4)

clear_button = Button(root, text= "Clear",command = lambda:clear_text(),height = height_size, width = width_size,fg = "white",bg="black")
clear_button.grid(row = 5,column = 1)

equal_button = Button(root, text= "=",command = lambda:getResult(),height = height_size, width = width_size,fg = "white",bg="black")
equal_button.grid(row = 5,column = 2)

root.bind('<Return>',lambda event:getResult())
root.mainloop()
