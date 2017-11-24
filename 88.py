class demomthd:
    @staticmethod
    def static_mthd():
        print('调用了静态方法！')

    @classmethod
    def class_mthd(cls):
        print('调用了类方法！')
demomthd.static_mthd()
demomthd.class_mthd()
#dm=demomthd()
#dm.static_mthd()
#dm.class_mthd()
