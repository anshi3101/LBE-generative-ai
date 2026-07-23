from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel): #inheriting with base model
     #name : str --> 1.Simple 
     
     name:str = 'Anshi'
     age:Optional[int] = None # 2.Default values,4.Coerc-Impicit conversion
     email: EmailStr #optional Field
     cgpa: float = Field(gt=0,lt=10,default=5,description='A decimal value representing cgpa of the student') 
     #5.field function -> default values,constraints,description,regex
     
     
new_student = {'age':32, 'email':'abc@gmail.com'}

student = Student(**new_student)
student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()
