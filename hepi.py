# -*- coding: utf-8 -*-
# coding:utf-8
import tkinter
import tkinter.messagebox
class Window:
    def __init__(self):
        self.root=tkinter.Tk()
        menu=tkinter.Menu(self.root)
        submenu=tkinter.Menu(menu,tearoff=0)
        submenu.add_command(label="关于...")
        submenu.add_separator()
        submenu.add_command ( label="退出" )
        menu.add_cascade(label="系统",menu=submenu)

        #menu = tkinter.Menu ( self.root )
        submenu = tkinter.Menu ( menu, tearoff=0 )
        submenu.add_command ( label="扫描垃圾文件" )
        submenu.add_command ( label="删除文件" )
        menu.add_cascade ( label="清理", menu=submenu )

        #menu = tkinter.Menu ( self.root )
        submenu = tkinter.Menu ( menu, tearoff=0 )
        submenu.add_command ( label="E:\3D\Improving_edge_detection_and_watershed_segmentatio.pdf" )
        submenu.add_separator ()
        submenu.add_command ( label="按文件搜索文件" )
        menu.add_cascade ( label="搜索", menu=submenu )

        self.root.config(menu=menu)
        self.progress=tkinter.Label(self.root,anchor=tkinter.W,text="状态",bitmap="hourglass",compound="left")
        self.progress.place(x=10,y=370,width=900,height=600)

        self.flist=tkinter.Listbox(self.root)
        self.flist.place(x=10,y=10,width=900,height=600)


        self.vscroll=tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side="right",fill="y")
        self.flist["yscrollcommand"]=self.vscroll.set
        self.vscroll["command"]=self.flist.yview


    def MainLoop(self):
            self.root.title("I love 何萍萍")
            self.root.minsize(1000,700)
            self.root.maxsize(1000,700)
            self.root.mainloop()

if __name__=="__main__":
    window = Window()
    window.MainLoop()
