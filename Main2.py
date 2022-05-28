#Student class definition starts here 
class Student:
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score
        
#student class definition ends here
        
​
#creation of student Bob follows
student1 = Student('peter',34,'UI/UX',20.90)
print('INFORMATION ABOUT THE FIRST STUDENT')
#output student1 name
print('NAME::: ', student1.name)
#output student1 age
print('AGE::: ',student1.age)
#output student1 track
print('TRACK::: ',student1.track)
#output student1 score
print('SCORE:::',student1.score)
​
#creatint another intance of class student
student2 = Student('Paul',20,'Fullstack',80)
​
print('\n\nINFORMATION ABOUT THE SECOND STUDENT')
print(student2.name)
print(student2.age)
print(student2.track)
print(student2.score)
