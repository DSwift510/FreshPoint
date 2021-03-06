#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Nov 30, 2017 12:55:13 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import Freshpoint_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = UFood_Data_Analysis (root)
    Freshpoint_support.init(root, top)
    root.mainloop()

w = None
def create_UFood_Data_Analysis(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = UFood_Data_Analysis (w)
    Freshpoint_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_UFood_Data_Analysis():
    global w
    w.destroy()
    w = None


class UFood_Data_Analysis:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("1380x869+596+402")
        top.title("UFood Data Analysis")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.09, rely=0.07, relheight=0.32
                , relwidth=0.2)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(foreground="black")
        self.Labelframe1.configure(text='''Insert Data''')
        self.Labelframe1.configure(background="#d9d9d9")
        self.Labelframe1.configure(highlightbackground="#d9d9d9")
        self.Labelframe1.configure(highlightcolor="black")
        self.Labelframe1.configure(width=270)

        self.Button1 = Button(self.Labelframe1)
        self.Button1.place(relx=0.11, rely=0.76, height=33, width=85)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Clean Data''')

        self.Button2 = Button(self.Labelframe1)
        self.Button2.place(relx=0.67, rely=0.76, height=33, width=76)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Add Data''')

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.22, rely=0.22, height=26, width=142)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Document Classpath''')

        self.Entry1 = Entry(self.Labelframe1)
        self.Entry1.place(relx=0.15, rely=0.44, relheight=0.09, relwidth=0.76)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Labelframe2 = LabelFrame(top)
        self.Labelframe2.place(relx=0.33, rely=0.07, relheight=0.32
                , relwidth=0.22)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(foreground="black")
        self.Labelframe2.configure(text='''Modify table''')
        self.Labelframe2.configure(background="#d9d9d9")
        self.Labelframe2.configure(highlightbackground="#d9d9d9")
        self.Labelframe2.configure(highlightcolor="black")
        self.Labelframe2.configure(width=300)

        self.Button3 = Button(self.Labelframe2)
        self.Button3.place(relx=0.3, rely=0.73, height=33, width=114)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Add Food Type''')

        self.Radiobutton1 = Radiobutton(self.Labelframe2)
        self.Radiobutton1.place(relx=0.27, rely=0.22, relheight=0.11
                , relwidth=0.57)
        self.Radiobutton1.configure(activebackground="#d9d9d9")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#d9d9d9")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify=LEFT)
        self.Radiobutton1.configure(text='''Fruit Vegetable Table''')

        self.Radiobutton2 = Radiobutton(self.Labelframe2)
        self.Radiobutton2.place(relx=0.27, rely=0.36, relheight=0.11
                , relwidth=0.56)
        self.Radiobutton2.configure(activebackground="#d9d9d9")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#d9d9d9")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify=LEFT)
        self.Radiobutton2.configure(text='''Complete Freshpoint''')

        self.Entry2 = Entry(self.Labelframe2)
        self.Entry2.place(relx=0.2, rely=0.55, relheight=0.09, relwidth=0.68)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Labelframe3 = LabelFrame(top)
        self.Labelframe3.place(relx=0.59, rely=0.07, relheight=0.32
                , relwidth=0.17)
        self.Labelframe3.configure(relief=GROOVE)
        self.Labelframe3.configure(foreground="black")
        self.Labelframe3.configure(text='''Calculation and Reports''')
        self.Labelframe3.configure(background="#d9d9d9")
        self.Labelframe3.configure(highlightbackground="#d9d9d9")
        self.Labelframe3.configure(highlightcolor="black")
        self.Labelframe3.configure(width=240)

        self.Button4 = Button(self.Labelframe3)
        self.Button4.place(relx=0.21, rely=0.33, height=33, width=138)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Generate Heatmap''')

        self.Button5 = Button(self.Labelframe3)
        self.Button5.place(relx=0.29, rely=0.69, height=33, width=104)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Export Report''')






if __name__ == '__main__':
    vp_start_gui()



