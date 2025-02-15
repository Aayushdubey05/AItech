from fastapi import FastAPI, requests, responses, HTTPException, status

app = FastAPI()

# class root:
#     def home():
#         data = {"data": "You are on dashboard/home page"}
@app.get("/")
def home():
    return {'data': 'You are on Home page'}