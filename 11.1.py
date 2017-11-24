# -*- coding: utf-8 -*-
def testryall(index,i):
    stulst=["john","jenny","tom"]
    af=open("my.txt",'wt+')

    try:
       af.write(stulst[index])
    except:
        pass
    finally:
        af.close()
        print('error')
print('try all ...right')
testryall(1,2)
print('try all one error')
testryall(1,0)
print('try all ...two error')
testryall(4,0)