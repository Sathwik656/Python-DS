'''def area(l,b):
    print("Area : ",l*b)
area(20,30)'''

#keyword arguments
'''def details(name,rank):
    print("Student Name : ",name)
    print("Student Rank : ",rank)

details(rank = 5,name = "Sathwik")'''

#default arguments
'''def details(name,rank=10):
    print("Student Name : ",name)
    print("Student Rank : ",rank)

details(name = "Sathwik")'''

#Arbitrary arguments in python/ Variable length arguments (*args)
'''def demo(*sports):
    print("Displaying passed aguments")
    for n in sports:
        print(n)

demo("football","hockey","Cricket","f1")'''

#Arbitrary keyword arguments (**kwargs)
def demo(**student):
    print("Student name: ",student['student'])
    print("Student section: ",student['section'])

demo(student='jack',section='A')