import asyncio
import time


# simple usage using async and await
async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def driver():
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"finished at {time.strftime('%X')}")


# execute tasks at the same time.
async def driver_for_tasks():
    # asyncio.create_task(coro, *, name=None) 3.8+
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
asyncio.run(driver())
asyncio.run(driver_for_tasks())
