#let's import the tkinter module to create GUI
import tkinter
# print(dir(tkinter))
# lets create an empty GUI/root GUI
root = tkinter.Tk()
# lets define the width and height of GUI
root.geometry('400x400')
root.resizable(width=False, height=False)
#lets change the title
root.title("Piyush")
# lets add entry widget
entry = tkinter.Entry(root)
entry.pack()
# lets call the mainloop function
root.mainloop()