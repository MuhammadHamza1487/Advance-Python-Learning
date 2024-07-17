# Python Program to perform addition 
# of two complex numbers using binary 
# + operator overloading.
 
class complex:
    def __init__(self, a):
        self.a = a
 
     # adding two objects 
    def __gt__(self, other):
        print("Good")
 
Ob1 = complex(1)
Ob2 = complex(2)
if Ob1 < Ob2:
    print()