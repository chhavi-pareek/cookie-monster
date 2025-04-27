from fastapi import FastAPI
from pydantic import BaseModel
from authentication.accesscookie import authCookie
from authentication.hiddencookie import get_hidden_xsrf
from results.results import displayMarks

app = FastAPI()

class user(BaseModel):
    usn: str
    password: str

@app.get("/")
def home():
    return {
        "welcome" : "this is rvce sappy scrapper",
        "fetch marks" : {
            "route" : "/grades"  ,
            "body" : 
                {"usn" : "string",
                "password" : "string"}       
        }
    }
      
         
@app.get("/grades")
def marks(usn : str, password : str):
   cookies = authCookie(user=usn, password=password) 
   marks = displayMarks(cookies)
   return marks