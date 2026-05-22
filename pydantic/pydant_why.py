from pydantic import BaseModel,EmailStr,Field, field_validator
from typing import Annotated,Dict
class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='name of patient',examples=['sakshi'])
                   ]
    age:int=Field(gt=0)
    email:EmailStr
    contact_details=Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_valid(cls,value):
          valid=['hdfc.com','idfc.com']
          domain=value.split('@')[-1]
          if domain not in valid:
                raise ValueError('not in domain')
          else:
                return value
          
#     @model_validator('age')
# def insert(pat:Patient):
    
            # print(pat.name)
            # print(pat.age)
            # print(pat.email)

patinfo={'name':'sakshi','age':21,'email':'sakshi@hdfc.com'}

patient=Patient(**patinfo)

insert(patient)
