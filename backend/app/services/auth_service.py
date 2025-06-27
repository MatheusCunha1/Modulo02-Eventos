from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/events")
def get_events():
    return {"message": "This will return events in the future."}
