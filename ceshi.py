# -*- coding: utf-8 -*-
def testtry(index,flag=False):
    stulst=["john","jenny","tom"]
    if flag:
        try:
            astu=stulst[index]
        except IndexError:
            print("IndecError")
        return  "try test finished"
    else:
        estu=stulst[index]

    return "no try test finshed"
print("right params test finished")
print(testtry(1,True))
print(testtry(1,False))
print("ERROR params testing start")
print(testtry(4,True))
print(testtry(4,False))
