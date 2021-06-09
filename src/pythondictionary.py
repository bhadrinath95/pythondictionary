from tkinter import *
from PyDictionary import PyDictionary

dictionary = PyDictionary()
root = Tk()
root.title("Dictionary")
root.geometry("500x500")
def dict():
    if word.get() == "":
        pass
    else:
        try:
            error_message.config(text="")
            meaning.config(text= ',\n '.join([mean.capitalize() for mean in dictionary.meaning(word.get())['Noun'][0:10]]))
            synonym.config(text= "" if dictionary.synonym(word.get()) is None else synonym.config(text= ',\n'.join([syn.capitalize() for syn in dictionary.synonym(word.get())[0:10]])))
            antonym.config(text= "" if dictionary.antonym(word.get()) is None else ',\n'.join([ant.capitalize() for ant in dictionary.antonym(word.get())[0:5]]))
        except:
            meaning.config(text="")
            synonym.config(text= "")
            antonym.config(text= "")
            error_message.config(text = "Sorry! The word '"+ word.get()+ "' is not present in the dictionary.\n Please check the spelling you typed.")
            word.delete(0, END)
def cleartxt():
    meaning.config(text="")
    synonym.config(text= "")
    antonym.config(text= "")
    error_message.config(text="")
    word.delete(0, END)
    
Label(root, text="Dictionary", font=("Arial 20 bold"), fg="Green").pack(pady=10)
frame = Frame(root)
Label(frame, text="Type Word", font=("Arial 15 bold")).pack(side=LEFT)
word = Entry(frame, font=("Arial 15 bold"))
word.pack()
frame.pack(pady=10)

frame1 = Frame(root) 
Label(frame1, text="Meaning: ", font=("Arial 10 bold")).pack(side=LEFT)
meaning = Label(frame1, font=("Arial 10"), wraplength=300)
meaning.pack()
frame1.pack(pady=10)

frame2 = Frame(root) 
Label(frame2, text="Synonym: ", font=("Arial 10 bold")).pack(side=LEFT)
synonym = Label(frame2, font=("Arial 10"))
synonym.pack()
frame2.pack(pady=10)

frame3 = Frame(root) 
Label(frame3, text="Antonym: ", font=("Arial 10 bold")).pack(side=LEFT)
antonym = Label(frame3, font=("Arial 10"))
antonym.pack()
frame3.pack(pady=10)

frame4 = Frame(root)
clear = Button(frame4, text="Clear", font=("Arial 15 bold"), command=cleartxt)
clear.grid(row=0, column=1, padx=10, pady=10)


submit = Button(frame4, text="Submit", font=("Arial 15 bold"), command=dict)
submit.grid(row=0, column=2, padx=10, pady=10)

quit_button = Button(frame4, text="Close", font=("Arial 15 bold"), command=root.destroy)
quit_button.grid(row=0, column=3, padx=10, pady=10)
frame4.pack(pady=10)

frame5 = Frame(root)
error_message = Label(frame5, font=("Arial 10"), fg="Red")
error_message.pack()
frame5.pack(pady=10)

root.mainloop()