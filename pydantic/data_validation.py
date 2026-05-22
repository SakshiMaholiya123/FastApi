from pydantic import BaseModel
class Student(BaseModel):
    name:str
    age:int

stu1=Student(name='sakshi',age=21)
stu=Student(name='sakshi',age='21')  #will convert from string to int
#sti=Student(name='sakshi',age='abc')      #cant be converted as it is a sequence of characters
print(stu)
print(stu1)