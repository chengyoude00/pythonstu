class demo_property:
    class_name='demo_property'
    def __init__(self,x=0):
        self.x=x

    def class_info(self):
        print('类变量值：',demo_property.class_name)
        print('实例变量值：',self.x)
    def chng(self,x):
        self.x=x
    def chng_cn(self,name):
        demo_property.class_name=name
dpa=demo_property()
dpb=demo_property()
print('初始化两个例子')
dpa.class_info()
dpb.class_info()
print('修改实例变量')
print('修改dpb实例变量')
dpa.chng(3)
dpa.class_info()
dpb.class_info()
print('修改dpa实例变量')
dpa.chng_cn('dpa')
dpa.class_info()
dpb.class_info()
print('修改dpb实例变量')
dpb.chng_cn('dpb')
dpa.class_info()
dpb.class_info()

