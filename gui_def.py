import tkinter as tk


class GUI(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Test')
        self.resizable(width=False, height=False)       
        self.geometry('{}x{}'.format(800,800))

        self.canvas = tk.Canvas(self,width = 800,height = 800)
        self.canvas.pack()

        self.create_circle(100,100,20,self.canvas)
#window = tk.Tk()
    def create_circle(self,x, y, r, canvasName): #center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        return canvasName.create_oval(x0, y0, x1, y1)
#window.title('Test')

#window.resizable(width=False, height=False)
#window.geometry('{}x{}'.format(800,800))

if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
