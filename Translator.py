from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1080x500')
root.resizable(0,0)
root.config(bg = 'skyblue3')

root.title("Language Translator")
Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='Olive Drab1').place(x=410, y=30)


Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=10, pady=40, width = 60)
Input_text.place(x=30,y = 150)
Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white').place(x=190,y=160)


Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=10, pady= 40, width =60)
Output_text.place(x = 600 , y = 150)
Label(root,text ="Output", font = 'arial 13 bold', bg ='white').place(x=780,y=160)


language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values= language, width =70)
src_lang.place(x=30,y=120)
src_lang.set('Choose Input Language')

dest_lang = ttk.Combobox(root, values= language, width =70)
dest_lang.place(x=600,y=120)
dest_lang.set('Choose Output Language')

def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0, END) , src = src_lang.get(), dest = dest_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)


trans_btn = Button(root, text = 'Translate',font = 'arial 10 bold',pady = 3,command = Translate , bg = 'seagreen3', activebackground = 'sky blue')
trans_btn.place(x = 500, y= 270 )


root.mainloop()
