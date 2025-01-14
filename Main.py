import tkinter
from tkinter import *
import tkinter as tk
import keyboard
import random
f = 1
Head = tk.Tk()
Head.title("Билетыыы йоу")
Head.iconbitmap('img\\Logo.ico')
Head.geometry('704x512')
Head.resizable(width=False, height=False)

canvas = Canvas(Head, width=1920, height=1080)
MicroFoneImg = PhotoImage(file='img\\Hitler-y-StalinNoFull.png')
BigFoneImg = PhotoImage(file='img\\Hitler-y-StalinFull.png')
InButtonImg = PhotoImage(file='img\\resize_minimize_maximize_expand_screen_icon_190600.png')
OutButtonImg = PhotoImage(file='img\\resize_minimize_maximize_expand_screen_icon_190602.png')
OptionImg = PhotoImage(file='img\\OptionImage.png')
PlayButtonImg = PhotoImage(file='img\\play.png')
LeftButtonImg = PhotoImage(file='img\\Left.png')
RightButtonImg = PhotoImage(file='img\\Right.png')
NewFactor = 1
countBilet = 10
    # --------------------
n4 = ''
n5 = ("Введите\n  число")
n6 = ''
# --------------------
n1 = '-----------------'
n2 = '-----------------'
n3 = '-----------------'
# --------------------
n7 = '-----------------'
n8 = '-----------------'
n9 = '-----------------'

def MicroDisplay():
    global f
    global NewFactor
    f = 1
    Head.attributes('-fullscreen', False)
    canvas.create_image(0, 0, image=MicroFoneImg, anchor="nw")
    renderFigure(1)
def BigDisplay():
    global f
    f = 0
    Head.attributes('-fullscreen', True)
    canvas.create_image(0,0, image=BigFoneImg, anchor="nw")
    renderFigure(0)
def renderFigure(a):
    global FigureOne
    global FigureTwo
    if a == 1:
        # ------------------------------------Верхний ряд----------------------------------------
        canvas.create_rectangle((262, 166), (322, 226), fill="#FFFFFF", outline="#004D40", tags="FigureOne")
        canvas.create_text(292, 196, text=n1, fill="#004D40", tags="FigureOne")
        canvas.create_rectangle((322, 166), (382, 226), fill="#FFFFFF", outline="#004D40", tags="FigureOne")
        canvas.create_text(352, 196, text=n2, fill="#004D40", tags="FigureOne")
        canvas.create_rectangle((382, 166), (442, 226), fill="#FFFFFF", outline="#004D40", tags="FigureOne")
        canvas.create_text(412, 196, text=n3, fill="#004D40", tags="FigureOne")
        # ------------------------------------Средний ряд-----------------------------------------
        canvas.create_rectangle((262, 226), (322, 286), fill="#FFFFFF", outline="#004D40", tags="FigureOne")
        canvas.create_text(292, 256, text=n4, fill="#004D40", tags="FigureOne")
        canvas.create_rectangle((322, 226), (382, 286), fill="#FFFFFF", outline="#004D40", tags="FigureOne")
        canvas.create_text(352, 256, text=n5, fill="#004D40", tags="FigureOne")
        canvas.create_rectangle((382, 226), (442, 286), fill="#FFFFFF", outline="#004D40", tags="FigureOne")
        canvas.create_text(412, 256, text=n6, fill="#004D40", tags="FigureOne")
        # ------------------------------------Нижний ряд----------------------------------------
        canvas.create_rectangle((262, 286), (322, 346), fill="#FFFFFF", outline="#004D40", tags="FigureOne")
        canvas.create_text(292, 316, text=n7, fill="#004D40", tags="FigureOne")
        canvas.create_rectangle((322, 286), (382, 346), fill="#FFFFFF", outline="#004D40", tags="FigureOne")
        canvas.create_text(352, 316, text=n8, fill="#004D40", tags="FigureOne")
        canvas.create_rectangle((382, 286), (442, 346), fill="#FFFFFF", outline="#004D40", tags="FigureOne")
        canvas.create_text(412, 316, text=n9, fill="#004D40", tags="FigureOne")
    if a == 0:
        # ------------------------------------Верхний ряд----------------------------------------
        canvas.create_rectangle((690, 270), (870, 450), fill="#FFFFFF", outline="#004D40", tags="FigureTwo")
        canvas.create_text(780, 360, text=n1, fill="#004D40", font='Times 20', tags="FigureTwo")
        canvas.create_rectangle((870, 270), (1050, 450), fill="#FFFFFF", outline="#004D40", tags="FigureTwo")
        canvas.create_text(960, 360, text=n2, fill="#004D40", font='Times 20', tags="FigureTwo")
        canvas.create_rectangle((1050, 270), (1230, 450), fill="#FFFFFF", outline="#004D40", tags="FigureTwo")
        canvas.create_text(1140, 360, text=n3, fill="#004D40", font='Times 20', tags="FigureTwo")
        # ------------------------------------Серединий ряд----------------------------------------
        canvas.create_rectangle((690, 450), (870, 630), fill="#FFFFFF", outline="#004D40", tags="FigureTwo")
        canvas.create_text(780, 540, text=n4, fill="#004D40", font='Times 20', tags="FigureTwo")
        canvas.create_rectangle((870, 450), (1050, 630), fill="#FFFFFF", outline="#004D40", tags="FigureTwo")
        canvas.create_text(960, 540, text=n5, fill="#004D40", font='Times 20', tags="FigureTwo")
        canvas.create_rectangle((1050, 450), (1230, 630), fill="#FFFFFF", outline="#004D40", tags="FigureTwo")
        canvas.create_text(1140, 540, text=n6, fill="#004D40", font='Times 20', tags="FigureTwo")
        # ------------------------------------Нижний ряд-----------------------------------------
        canvas.create_rectangle((690, 630), (870, 810), fill="#FFFFFF", outline="#004D40", tags="FigureTwo")
        canvas.create_text(780, 720, text=n7, fill="#004D40", font='Times 20', tags="FigureTwo")
        canvas.create_rectangle((870, 630), (1050, 810), fill="#FFFFFF", outline="#004D40", tags="FigureTwo")
        canvas.create_text(960, 720, text=n8, fill="#004D40", font='Times 20', tags="FigureTwo")
        canvas.create_rectangle((1050, 630), (1230, 810), fill="#FFFFFF", outline="#004D40", tags="FigureTwo")
        canvas.create_text(1140, 720, text=n9, fill="#004D40", font='Times 20', tags="FigureTwo")
def on_press_F11(event):
    if event.name == 'f11':
        if f == 1:
            DellDisplay(1)
            displayBig.Factor()
        else:
            DellDisplay(0)
            displayMicro.Factor()
def PlayFunc(a):
    global  PlayButton
    if a == 1:
        PlayButton = tkinter.Button(Head, image=PlayButtonImg, command=lambda:(slotScriptOne(1)))
        canvas.create_window(352, 410, window=PlayButton)
    else:
        PlayButton = tkinter.Button(Head, image=PlayButtonImg, command=lambda:(slotScriptOne(0)))
        canvas.create_window(960, 910, window=PlayButton)
def ResizeButton(a):
    global InButton
    global OutButton
    if a == 1:
        InButton = tkinter.Button(Head, image=InButtonImg, command=lambda:(DellDisplay(1),displayBig.Factor()))
        canvas.create_window(685, 21, window=InButton)
    else:
        OutButton = tkinter.Button(Head, image=OutButtonImg, command=lambda:(DellDisplay(0),displayMicro.Factor()))
        canvas.create_window(1900,21, window=OutButton)
WindowsYes = 0
def OptionButton(a):
    global OptionButtonOne
    global OptionButtonTwo
    if a == 1:
        OptionButtonOne = tkinter.Button(Head, image=OptionImg, command=lambda:(OptionOne(), CreateWindow()))
        canvas.create_window(648, 21, window=OptionButtonOne)
    else:
        OptionButtonTwo = tkinter.Button(Head, image=OptionImg, command=lambda: CreateWindow())
        canvas.create_window(1862, 21, window=OptionButtonTwo)
def DellDisplay(a):
    if a == 1:
        InButton.destroy()
        OptionButtonOne.destroy()
        PlayButton.destroy()
        canvas.delete("FigureOne")
        LeftButton.destroy()
        RightButton.destroy()
        Pole.destroy()
    else:
        OutButton.destroy()
        OptionButtonTwo.destroy()
        canvas.delete("FigureTwo")
        LeftButton.destroy()
        RightButton.destroy()
        Pole.destroy()
def closedOption():
    global WindowsYes
    WindowsYes = 0
    Option.destroy()
def CreateWindow():
    global WindowsYes
    global Option
    WindowsYes = 1
    Option = tk.Tk()
    Option.title("")
    Option.iconbitmap('img\\OptionImage_1.ico')
    Option.resizable(width=False, height=False)
    Option.protocol("WM_DELETE_WINDOW", closedOption)
    optionMenu = Canvas(Option, width=180, height=300)
    optionMenu.pack()
def OptionOne():
    global WindowsYes
    if WindowsYes == 1:
        Option.destroy()
        WindowsYes = 0
    else:
        WindowsYes = 1

def Vvod(a):
    global  Pole
    global  LeftButton
    global  RightButton
    if a == 1:
        Pole = Entry(Head,width=2)
        Pole.place(x=666,y=491)
        Pole.insert(END,countBilet)
        LeftButton = tkinter.Button(Head, image=LeftButtonImg,width=15,height=15, command=lambda: LeftFunction(1))
        canvas.create_window(656,501,window=LeftButton)
        RightButton = tkinter.Button(Head, image=RightButtonImg,width=15,height=15, command=lambda: RightFunction(1))
        canvas.create_window(692,501,window=RightButton)
    else:
        Pole = Entry(Head, width=2)
        Pole.place(x=2297, y=1060)
        Pole.insert(END,countBilet)
        LeftButton = tkinter.Button(Head, image=LeftButtonImg, width=15, height=15, command=lambda: LeftFunction(0))
        canvas.create_window(1873, 1070, window=LeftButton)
        RightButton = tkinter.Button(Head, image=RightButtonImg, width=15, height=15, command=lambda: RightFunction(0))
        canvas.create_window(1909, 1070, window=RightButton)
def RightFunction(a):
    global countBilet
    global Pole
    if int(Pole.get()) > 50:
        Pole.destroy()
        countBilet = 25
        Pole = Entry(Head, width=2)
        Pole.place(x=666, y=491)
        Pole.insert(END, countBilet)
    if a == 1:
        if int(Pole.get()) < 50:
            countBilet = int(Pole.get()) + 1
            Pole.destroy()
            Pole = Entry(Head, width=2)
            Pole.place(x=666, y=491)
            Pole.insert(END, countBilet)
            print(countBilet)
    if a == 0:
        if int(Pole.get()) < 50:
            countBilet = int(Pole.get()) + 1
            Pole.destroy()
            Pole = Entry(Head, width=2)
            Pole.place(x=2297, y=1060)
            Pole.insert(END, countBilet)
            print(countBilet)
def slotScriptOne(a):
    global n4
    global n5
    global n6
    global NewFactor
    while True:
        n4 = random.randint(1, int(Pole.get()))
        n5 = random.randint(1, int(Pole.get()))
        n6 = random.randint(1, int(Pole.get()))
        print(n4,n5,n6)
        if n4 == n5 and n5 == n6:
            if a == 1:
                canvas.delete("FigureOne")
                renderFigure(1)
                break
            if a == 0:
                canvas.delete("FigureTwo")
                renderFigure(0)
                break
        if n4 != n5 and n4 != n6 and n5 != n6:
            if a == 1:
                canvas.delete("FigureOne")
                renderFigure(1)
                break
            if a == 0:
                canvas.delete("FigureTwo")
                renderFigure(0)
                break
def LeftFunction(a):
    global countBilet
    global Pole
    if int(Pole.get()) < 0:
        Pole.destroy()
        countBilet = 25
        Pole = Entry(Head, width=2)
        Pole.place(x=666, y=491)
        Pole.insert(END, countBilet)
    if a == 1:
        if int(Pole.get()) > 0:
            countBilet = int(Pole.get()) - 1
            Pole.destroy()
            Pole = Entry(Head, width=2)
            Pole.place(x=666, y=491)
            Pole.insert(END, countBilet)
            print(countBilet)
    if a == 0:
        if int(Pole.get()) > 0:
            countBilet = int(Pole.get()) - 1
            Pole.destroy()
            Pole = Entry(Head, width=2)
            Pole.place(x=2297, y=1060)
            Pole.insert(END, countBilet)
            print(countBilet)
class DisplayFactor():
    def __init__(self,MicroOrBig):
        self.MicroOrBig = MicroOrBig
    def Factor(self):
        #Тута если маленький экран
        if self.MicroOrBig:
            MicroDisplay()
            PlayFunc(1)
            ResizeButton(1)
            OptionButton(1)
            Vvod(1)
        #Тута если большой экран
        else:
            BigDisplay()
            PlayFunc(0)
            ResizeButton(0)
            OptionButton(0)
            Vvod(0)
displayMicro = DisplayFactor(True)
displayBig = DisplayFactor(False)
displayMicro.Factor()
keyboard.on_press(on_press_F11)
canvas.pack()
Head.mainloop()