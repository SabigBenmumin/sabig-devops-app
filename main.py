from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Sabig is learning DevOps!"}
