class Student:
  def __init__(self,name,roll_no,dept,mark1,mark2,mark3):
    self.name=input()
    self.roll_no=int(input())
    self.dept=input()
    self.mark1=int(input())
    self.mark2=int(input())
    self.mark3=int(input())

  def result(self):
    self.total=self.mark1 + self.mark2 + self.mark3
    self.avg=(self.total)/3
    if(avg>90):
      self.grade="A"
    elif(avg>80):
      self.grade="B"
    elif(avg>70):
      self.grade="C"
    elif(avg>60):
      self.grade="D"
    elif(avg>50):
      self.grade="E"
    else:
      self.grade="Fail"
  
  def display(self):
    print("Student Details: \n")
    print(f"Name: {self.name}")
    print(f"Roll_number: {self.roll_no}")
    print(f"mark1: {self.mark1}")
    print(f"mark2: {self.mark2}")
    print(f"mark3: {self.mark3}")
    print(f"Total Marks: {self.total}")
    print(f"Average: {self.avg}")

s=Student
s.result()
s.display()