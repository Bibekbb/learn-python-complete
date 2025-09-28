import time
import asyncio
async def function1():
    await asyncio.sleep(2)
    print("Bibek")
    return "Baby"

async def function2():
    await asyncio.sleep(2)
    print("BB")
    return "Mousam"

async def function3():
    await asyncio.sleep(5)
    print("Musu")
    return "Badal"

async def main():
    L = await asyncio.gether(
        function1(),
        function2(),
        function3(),
    )
    print(L)


#     task = asyncio.create_task(function)
#     # await function1()
#     await function2()
#     await function3()

# asyncio.run(main())
