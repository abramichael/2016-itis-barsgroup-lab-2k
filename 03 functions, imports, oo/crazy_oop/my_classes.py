class Student:

    def __init__(self, name, subjects=(), phone="+7"):
        self.name = name
        self.subjects = subjects
        self.__phone = phone

    def study(self):
        if self.subjects:
            for s in self.subjects:
                print "%s studies %s" % (self.name, s)
        else:
            print ("%s is lazy." % self.name)

class A(object):
    def who_am_i(self):
        print("I am a A")

class B(A):
#    def who_am_i(self):
#        print("I am a B")
    pass

class C(A):
    def who_am_i(self):
        super(C, self).who_am_i()
        print("I am a C")

class D(B,C):
   # def who_am_i(self):
   #     print("I am a D")
   pass

if __name__ == "__main__":
    d1 = D()
    d1.who_am_i()

