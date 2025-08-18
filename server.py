from fastapi import FastAPI 
import asyncio 

app = FastAPI()

@app.get("/ok")
asysnc def root():
    return {"message": "success"}

''' We pass in ms variable to allow different time testing '''
@app.get("/sleep")
async def sleep_endpoint(ms: int):
    await asyncio.sleep(2)
    return {"sleptMs": ms}
