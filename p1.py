import tkinter as tk
import tkinter.font as tkFont
import random

class Game(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        rgb1 = (183, 247, 49) # 顏色的編號
        bgcolor  = '#%02x%02x%02x' % rgb1 
        font1 = tkFont.Font(size = 48, family = "Courier New") # 設定字型
        self.label = tk.Label(self, text = 'Crazy Eyes', font = font1, height = 1, width = 20)
        self.label.grid(row = 0, column = 0, columnspan = 4, sticky = tk.SE + tk.NW)
        self.button = {}
        for i in range(16):
            self.button[i] = tk.Button(self, width = 8, height = 8, command = lambda f = i : self.clickBtn(f), highlightbackground = bgcolor)
            self.button[i].grid(row = int(i / 4) + 2, column = i % 4, sticky = tk.SE + tk.NW)    

    def clickBtn(self, index): # 傳了self.clickBtn(f) 的f進index
        self.checkAnswer(index)
        self.changeColor()

    def changeColor(self):
        a = 50
        r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        rgb2 = (r, g, b)
        if r > a:
            rgb3 = (r - a, g, b)
        else:
            rgb3 = (r + a, g, b)
        bgcolor2 = '#%02x%02x%02x' % rgb2
        bgcolor3 = '#%02x%02x%02x' % rgb3

        for i in range(16):
            self.button[i].configure(highlightbackground = bgcolor2)

        new = random.randint(0, 15)
        self.button[new].configure(highlightbackground = bgcolor3)

        return new

    def checkAnswer(self, index):
        pass

gg = Game()
gg.master.title('CrazyEyesGame')
gg.mainloop()

