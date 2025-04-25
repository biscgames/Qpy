from tkinter import *
import atexit
import shutil
import os

def garbageCollector():
    if os.path.exists("./__pycache__"): shutil.rmtree("./__pycache__")

garbageCollector()
atexit.register(garbageCollector)

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
        self._update()
    def title(self,string:str):
        self.obj.title(string)
        return self
    def show(self):
        self.obj.mainloop()
        return self
    # ROW IS ONLY USED FOR GRID_DISPLAY
    def _update(self,row=0):
        if self.children:
            for idy,child in enumerate(self.children):
                child.widget.pack_forget();child.widget.pack() if self.display == PACK_DISPLAY else child.widget.grid_forget();child.widget.grid(row=idy)
        self.obj.geometry("{}x{}+{}+{}".format(self.width,self.height,self.position[0],self.position[1]))
    def setDimension(self,width,height):
        self.width = width
        self.height = height
        self._update()
        return self
    def setPosition(self,position:list):
        self.position = position
        self._update()
        return self
    def s(self,object):
        return object
    def i(self,index:int):
        return self.children[index]
    def removeChild(self,index:int):
        del self.children[index]
        return self
    def addChild(self,item):
        self.children.append(item)
        item._parent = self
        return self
class _QObject:
    def __init__(self,widget,classType=Widget):
        self.widget = widget
        self.classType = classType
        self._parent = None
        self.children = []
        self.display = PACK_DISPLAY
        self._update()
    def parent(self):
        return self._parent
    def appendTo(self,window):
        window.addChild(self)
        return self._parent if self._parent else None
    def w(window:_QWin):
        return window
    def attr(self,attribute:str|None=None,value=None,attributes:dict|None=None):
        if attribute and value:
            self.widget[attribute] = value
        else:
            self.widget.config(attributes)
        self._parent._update()
        return self
    def removeChild(self,index:int):
        del self.children[index]
        return self
    def addChild(self,item):
        self.children.append(item)
        item._parent = self
        self._update()
        return self
    def _update(self,row=0):
        if self._parent: self.display = self._parent.display
        if self.children:
            for idy,child in enumerate(self.children):
                child.widget.pack_forget();child.widget.pack() if self.display == PACK_DISPLAY else child.widget.grid_forget();child.widget.grid(row=idy)

def getMainWindow():
    global _mainWindow
    return _mainWindow
def mainWindow(window:Tk,display:int):
    global _mainWindow
    _mainWindow = _QWin(window,display)
    return getMainWindow()
def q(component:Widget):
    return _QObject(component,type(component))
