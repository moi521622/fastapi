from fastapi import FastAPI
from api.routers import task, done

# FastAPIインスタンスを作成
app = FastAPI()

app.include_router(task.router)
app.include_router(done.router)


# http://localhost:8000/docs
@app.get("/hello")
async def hello():
    return {"message": "Hello World!!!"}