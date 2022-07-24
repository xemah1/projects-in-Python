import ParagraphMaker
from tkinter import *
from functools import partial
from tkinter.messagebox import showinfo

def validate(paragraph, realParagraph) :
    i = 0.0
    j = 0.0
    if( len(paragraph.get()) < len(realParagraph) ) :
        length = len(paragraph.get())
        lenDiff = len(realParagraph) - len(paragraph.get())
    else :
        length = len(realParagraph)
        lenDiff = len(paragraph.get()) - len(realParagraph)
    for k in range(length) :
        if(paragraph.get()[k] == realParagraph[k]) :
            i += 1
        else :
            j += 1
    j += lenDiff
    i = i * (100 / (i + j))
    print(len(paragraph.get()))
    print(len(realParagraph))
    showinfo (title="Info", message="Your success rate is: " + str(round(i)) + "%")
    tkWindow.after(10,lambda:tkWindow.destroy())

def terminate() :
    tkWindow.after(10,lambda:tkWindow.destroy())

realParagraph = ParagraphMaker.paragraph()

#window
tkWindow = Tk()  
tkWindow.geometry('650x375')
tkWindow.title('xemah\'s code')
tkWindow.resizable(False,False)
tkWindow.config(bg='burlywood1')

ctr = 0
tkWindow_var = StringVar()
tkWindow_var.set(0)

Label(tkWindow, text=realParagraph, bd="2", font =('Helvetica bold',10)).place(relx=0.5, rely=0.375, anchor=CENTER)
paragraph = StringVar()

validate = partial(validate, paragraph, realParagraph)
Button(tkWindow, text='FINISH', bd ='2', bg = 'IndianRed1',font =('Helvetica bold',10), command = validate).place(relx=0.5, rely=0.625, anchor=CENTER)

terminate = partial(terminate)
Button(tkWindow, text='EXIT', bd ='2', bg = 'IndianRed1',font =('Helvetica bold',10), command = terminate).place(relx=0.95, rely=0.95, anchor=CENTER)

root = Frame(tkWindow)
root.pack(padx=72, pady=72, fill='x', expand=True)

entry = Entry(root, textvariable=paragraph)
entry.pack(fill='x', expand=True)
entry.focus()

tkWindow.mainloop()