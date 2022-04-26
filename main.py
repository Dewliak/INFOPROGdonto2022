
import tkinter as tk


class GUI(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Test')
        self.resizable(width=False, height=False)       
        self.geometry('{}x{}'.format(800,800))

        self.size = 800
        
        self.canvas = tk.Canvas(self,width = 800,height = 800)
        self.canvas.pack()

        #self.create_square(100,100,20,self.canvas)
#window = tk.Tk()
    def create_square(self,x, y,size, canvasName,fill_name): #center coordinates, radius

        return canvasName.create_rectangle(x, y, x+size, y + size,fill=fill_name)
#window.title('Test')


class Field:
    def __init__(self,data):
        self.types = data[0]
        self.cat = data[1]
        self.cost = data[2]
        self.diff = data[3]
        #self.vehichle = data[4]

def main():

    brail = {}
    palya = []
    map_data = []
    map_types = []
    world_map = []
    hegyek = []
    
    with open(file = "mellekletek/code.in",mode="r", encoding = "UTF-8") as code:
    
        for line in code.readlines()[1:]: # [1:] ignoralja a szamot
            l = line.strip().split(";")
            brail[l[0]] = l[1]


    with open(file = "mellekletek/fields.in", mode = "r", encoding = "UTF-8") as fields:

        for line in fields.readlines()[1:]:
            l = line.strip().split(';')
            map_data.append(Field(l))
            map_types.append(l[0])    

    counter = 0
    
    with open(file = "mellekletek/map_1.html", mode = "r", encoding = "UTF-8") as world:

        string = ""
        
        height = 0
        
        for line in world.readlines()[1:]:
            row = []
            width = 0
            
            for letter in line.strip().split(";"):
    

                if letter != "":
                    string += brail[letter[2:]]
                
                if string in map_types:
                    if string == "hegy":
                        counter += 1
                        hegyek.append(tuple([width,height]))
                    row.append(string)
                    string  = ""
                    width += 1
                
                                      
            world_map.append(row)

            height += 1

    egyik = []
    masik = []
    
    for i in hegyek:
        if len(egyik) != 0:
            if(egyik[-1][0] == i[0] or egyik[-1][1] == i[1]) and len(egyik) < 2:
                egyik.append(i)
            else:
                masik.append(i)
        else:
            egyik.append(i)
    print("kordinatak:")
    x = (min(egyik[0][0],egyik[1][0]) + max(masik[0][0],masik[1][0]))/2
    y = (min(egyik[0][1],egyik[1][1]) + max(masik[0][1],masik[1][1]))/2

    print(x+1,y+1)
   
    
    
    gui = GUI()
    
    grid_size = len(world_map[0])

    relative_size = gui.size/grid_size

    colors = {"ocean" : "blue",
              "tenger" : "cyan",
              "part" : "yellow",
              "oserdo": "green",
              "sivatag" :"yellow",
              "hegy" : "grey",
              "to" : "cyan",
              "folyo" : "blue",
              "mocsar" : "green",
              }
    print(world_map)
    for i in range(grid_size):
        for j in range(grid_size):
            color = colors[world_map[i][j]]
            gui.create_square(j*relative_size,i*relative_size,relative_size,gui.canvas,color)
    
    


    
    gui.mainloop()
if __name__ == "__main__":
    main()
