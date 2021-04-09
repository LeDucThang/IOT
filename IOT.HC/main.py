import uvicorn
from fastapi import FastAPI
from Rpc import CategoryController


app = FastAPI()

app.include_router(CategoryController.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=5001, reload=True, access_log=False, env_file='.env')