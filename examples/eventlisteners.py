from tkinter import *
from q import *
mainWindow(Tk(),PACK_DISPLAY).title("Hello, World!").setDimension(480,360).setPosition([400,200]).s(q(Label(text="I am a text!"))).appendTo(getMainWindow()).s(q(Button(text="Click me!",command=lambda: getMainWindow().children[0].attr("text","My contents have changed!")))).appendTo(getMainWindow()).show()
