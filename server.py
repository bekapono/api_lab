from fastapi import FastAPI 
import asyncio 

app = FastAPI()

@app.get("/ok")
async def root():
    return {"message": "success"}

''' We pass in ms variable to allow different time testing '''
@app.get("/sleep")
async def sleep_endpoint(ms: int):
    task_1 = await asyncio.sleep(ms/1000)
    
    return {"sleptMs": ms}
