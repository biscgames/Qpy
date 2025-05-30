from tkinter import *

PACK_DISPLAY = 0
GRID_DISPLAY = 1

_mainWindow = None
class _QWin:
    def __init__(self,obj:Tk,display:int=0):
        self.obj = obj
        self.width = 100
        self.height = 100
        self.position = [0,0]
        self.display = display
        self.children = []
        self._updateWindow()
    def title(self,string:str):
        self.obj.title(string)
        return self
    def show(self):
        self.obj.mainloop()
        return self
    # ROW IS ONLY USED FOR GRID_DISPLAY
    def _updateWindow(self,row=0):
        if self.children:
            for idy,child in enumerate(self.children):
                child.widget.pack_forget() if self.display == PACK_DISPLAY else child.widget.grid_forget()
                child.widget.pack() if self.display == PACK_DISPLAY else child.widget.grid(idy)
        self.obj.geometry("{}x{}+{}+{}".format(self.width,self.height,self.position[0],self.position[1]))
    def setDimension(self,width,height):
        self.width = width
        self.height = height
        self._updateWindow()
        return self
    def setPosition(self,position:list):
        self.position = position
        self._updateWindow()
        return self
    def addChild(self,child):
        self.children.append(child)
        child._parent = self
        self._updateWindow()
        return self
    def s(self,object):
        return object
class _QObject:
    def __init__(self,widget,classType=Widget):
        self.widget = widget
        self.classType = classType
        self._parent = None
    def parent(self):
        return self._parent
    def appendTo(self,window:_QWin):
        window.addChild(self)
        return self._parent if self._parent else None
    def w(window:_QWin):
        return window
    def attr(self,attribute:str|None=None,value=None,attributes:dict|None=None):
        if attribute and value:
            self.widget[attribute] = value
        else:
            self.widget.config(attributes)
        self._parent._updateWindow()

def getMainWindow():
    global _mainWindow
    return _mainWindow
def mainWindow(window:Tk,display:int=0):
    global _mainWindow
    _mainWindow = _QWin(window,display)
    return getMainWindow()
def q(component:Widget):
    return _QObject(component,type(component))
