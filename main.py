from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {'welcome' : 'home'}

@app.get("/test/")
def test():
    return {'welcome': 'test'}