import asyncio
from utilities.utiler import first_task, second_task

path = "./test_folder"

if __name__ == "__main__": 
    asyncio.run(first_task(path))
    second_task()
