from fastapi import FastAPI 
import asyncio 

app = FastAPI()

@app.get("/ok")
async def root():
    return {"message": "success"}

''' We pass in ms variable to allow different time testing '''
@app.get("/sleep")
async def sleep_endpoint(server_elapsed_time: int, client_timeout_request: int):
    '''
        what i want to do is simulate a client side timeout error
        where the timeout set from the client is shorter then the 
        time it takes to for the server to finish it's task.

        thoughts: 
        - what happens to the asyncio if it doesn't 
        finish in time? 
        - do i have to clear up the CPU manually?
        - can i return before a task is finished?
        - what happens if i dont add the await
    '''
    task_1 = await asyncio.sleep(server_elapsed_time)
    task_2 = await asyncio.sleep(client_timeout_request)
    
    return {"sleptMs": "place-holder"}
