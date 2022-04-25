
import tkinter as tk

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
    
    with open(file = "mellekletek/map_0.html", mode = "r", encoding = "UTF-8") as world:

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

    for i in hegyek:
        print(i[0],i[1])
    print("hegyek:",counter)    
if __name__ == "__main__":
    main()
