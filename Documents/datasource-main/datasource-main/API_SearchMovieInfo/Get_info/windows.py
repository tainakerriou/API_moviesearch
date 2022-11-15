from tkinter import *


class MyWindow(Tk):
    
    def __init__(self):
        Tk.__init__(self)
               
        self.__name = StringVar()
        
        label = Label( self, text="What movie are you looking for ?")
        label.pack()

        name = Entry(self, textvariable=self.__name )
        name.focus_set()
        name.pack()
        
        button = Button( self, text="Connect!", command=self.doSomething)
        button.pack()

        self.geometry( "300x200" )
        self.title( "Entry widget usage" )

    def doSomething(self):
        print( "You are " + self.__name.get() )


window = MyWindow()
window.mainloop()