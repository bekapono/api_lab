from fastapi import FastAPI
from typing import Dict
import asyncio 

app = FastAPI()

# --- TEMP DEFS FOR TESTING PURPOSES --- # 
async def server_sleep_task(sleep_time: int) -> Dict[str, int]:
    await asyncio.sleep(sleep_time)
    return {"SERVER" : sleep_time}

async def client_sleep_task(sleep_time: int) -> Dict[str, int]:
    await asyncio.sleep(sleep_time)
    return {"CLIENT" : sleep_time}

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
    server_task = asyncio.create_task(server_sleep_task(server_elapsed_time))
    client_task = asyncio.create_task(client_sleep_task(client_timeout_request))
    
    '''
        async asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)

        return_when={ALL_COMPLETED, FIRST_EXCEPTION, ALL_COMPLETED}
    '''
    # wait for the first one to complete
    done, pending = await asyncio.wait(
            {sever_task, client_task},
            return_when=asyncio.FIRST_COMPLETED
            )
    
    # grab the first completed result
    first_result = done.pop().result()

    # cancel remaining tasks
    for task in pending:
        task.cancel()


    return first_result
