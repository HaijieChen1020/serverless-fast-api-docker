from fastapi import FastAPI

app = FastAPI()


@app.get("/greeting")
async def greet():
    return {"Hello": "World"}
