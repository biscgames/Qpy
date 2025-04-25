# Qpy
Upcoming tkinter library to make applications easier

VER: BETA 1

## HOW TO
### Simple Window
Requirements:
- Tkinter
- Qpy BETA 1 (or newer)

Making a window using Qpy and Tkinter is simple! Just follow the step accordingly!</br>
**Step 1:** Nothing crazy, import all of Tkinter and Qpy using the `from` and `import` keywords:
```py
from tkinter import *
from q import * # Remember to put q.py inside the directory of your main app.
```
**Step 2:** Set a window to the _mainWindow variable, which is private but can be accessed and set with `mainWindow(window:Tk,display:PACK_DISPLAY|GRID_DISPLAY)`:
```py
mainWindow(Tk(),PACK_DISPLAY) # PACK_DISPLAY ensures it uses the pack display, and not another
```
**Step 3:** Set its title to anything you'd like, which can be done using the `title(string:str)` method inside of the mainWindow. Since `mainWindow(window:Tk,display:int)` always returns the main window, you can just chain it like this:
```py
mainWindow(Tk(),PACK_DISPLAY).title("Hello, World!")
```
**Step 4:** Set the size; It can be any size, as long it isn't bigger than your monitor resolution! We can do this by using the `setDimension(width,height)`. `title(string:str)` always returns the modified window, meaning you can chain it like this:
```py
mainWindow(Tk(),PACK_DISPLAY).title("Hello, World!").setDimension(480,360)
```
**Step 5:** Show the window; This is done using the `show()` method. `setDimension(width,height)` always returns the window this method has modified; Meaning you can simply add `.show()` to all of these:
```py
mainWindow(Tk(),PACK_DISPLAY).title("Hello, World!").setDimension(480,360).show()
```
You have now made a window!:

![Screenshot 2025-04-25 110252](https://github.com/user-attachments/assets/5ab2793b-7cf2-4dc5-b2db-4d80afa07b8c)

More readable version:
```py
from tkinter import *
from q import *

mainWindow(Tk(),PACK_DISPLAY).title("Hello, World!")
# You can use getMainWindow to get the main window
# setPosition changes the position of the window, which can be useful for centering windows
getMainWindow().setDimension(480,360).setPosition([400,200])


getMainWindow().show()
```
### Window with listening button
Requirements:
- Tkinter
- Qpy BETA 1 (or newer)

You've learned how to make a window, you might be wondering how to add buttons and text. Simple!

**Step 1:** Copy from last tutorial
```py
mainWindow(Tk(),PACK_DISPLAY).title("Hello, World!").setDimension(480,360).setPosition([400,200])
```
**Step 2:** Add a label to the window, which can be done by creating the label using `q(Label(text="I am a text!"))` then selecting it by putting it in the `s()` method from the main window; afterwards, use the `appendTo(getMainWindow())` method to add the object to the main window; like this:
```py
mainWindow(Tk(),PACK_DISPLAY).title("Hello, World!").setDimension(480,360).setPosition([400,200]).s(q(Label(text="I am a text!"))).appendTo(getMainWindow())
```
**Step 3:** Add a button to the window for when clicked, the contents of the label will change. You can change the label's contents by getting the first child from the mainWindow (that being the label) by using `getMainWindow().children[0]`, and performing the `attr()` method to change the text attribute. like this:
```py
getMainWindow().children[0].attr("text","My contents have changed!")
```
put all of this in a lambda:
```py
lambda: getMainWindow().children[0].attr("text","My contents have changed!")
```
then finally creating the button using `s(q(Button(text="Click me!"))).appendTo(getMainWindow())`, with the command attribute being the lambda we just made. appendTo always returns the window this method has added the object to, you can take that to your advantage to chain another object to the current line:
```py
mainWindow(Tk(),PACK_DISPLAY).title("Hello, World!").setDimension(480,360).setPosition([400,200]).s(q(Label(text="I am a text!"))).appendTo(getMainWindow()).s(q(Button(text="Click me!",command=lambda: getMainWindow().children[0].attr("text","My contents have changed!")))).appendTo(getMainWindow())
```
**Step 4:** It doesn't really need a rocket scientist in order to know what to do next:
```py
mainWindow(Tk(),PACK_DISPLAY).title("Hello, World!").setDimension(480,360).setPosition([400,200]).s(q(Label(text="I am a text!"))).appendTo(getMainWindow()).s(q(Button(text="Click me!",command=lambda: getMainWindow().children[0].attr("text","My contents have changed!")))).appendTo(getMainWindow()).show()
```
You have successfully created a window with a listening button:

![Screenshot 2025-04-25 114312](https://github.com/user-attachments/assets/cf24bb56-a5bf-47b6-b9aa-162e3d149855)
![Screenshot 2025-04-25 114322](https://github.com/user-attachments/assets/46de99b0-53c3-4ac7-a420-2d363bad7ad0)

Readable code:
```py
from tkinter import *
from q import *

onClick = lambda: getMainWindow().children[0].attr("text","My contents have changed!")

mainWindow(Tk(),PACK_DISPLAY).title("Hello, World!")

q(Label(text="I am a text!")).appendTo(getMainWindow())
q(Button(text="Click me!",command=onClick)).appendTo(getMainWindow())


getMainWindow().setDimension(480,360).setPosition([400,200]).show()
```

More tutorials soon!
