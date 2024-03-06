class Furniture:
    def length(self):
        print("lenght of any should be 5ft")
    
    def width(self):
        print("width of any should be 5ft")
        
class Table(Furniture):
    def legs(self):
        print("four legs is imp in table")
    def color(self):
        print("color is grey")
    def area(self):
        print("area of table is 5meter")

class Chair(Furniture):
    def legs(self):
        print("four legs is imp in chahir")
    def color(self):
        print("color is grey")
    def area(self):
        print("area of chair is 8meter")

class Sofa(Furniture):
    def legs(self):
        print("four legs is imp in sofa")
    def color(self):
        print("color is grey")
    def area(self):
        print("area of sofa is 8meter")
    
print("*********************")
t1 = Table()
c1 = Chair()
s1 = Sofa()

print("*********************")
t1.area()
t1.color()
t1.legs()

print("*********************")
c1.area()
c1.color()
c1.legs()
print("*********************")


s1.area()
s1.color()
s1.legs()


