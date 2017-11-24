#coding:utf-8

def coord_chng(x,y):
    return (abs(x),abs(y))
class Ant:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.disp_point()


    def move(self,x,y):
        x,y=coord_chng(x,y)
        self.edit_point(x,y)
        self.disp_point()

    def edit_point(self,x,y):
        self.x=self.x+x
        self.y=self.y+y

    def disp_point(self):
        print ("当前位置:(%d,%d)"%(self.x,self.y))

ant_a=Ant()
ant_a.move(2,4)
ant_a.move(-9,6)