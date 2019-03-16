import tkinter
from tkinter.filedialog import askopenfilename

def browse():
    global infile
    infile=askopenfilename()

root=tkinter.Tk()
root.title("My Window Title")
label=tkinter.Label(root,text="This is my window label")
label.pack()
browseButton=tkinter.Button(root,text="Browse",command=browse)
browseButton.pack()
root.mainloop()