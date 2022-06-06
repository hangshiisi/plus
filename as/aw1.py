import asyncio

async def phoneWorker():
    while True:
        await asyncio.sleep(1)
        print("Phone Task Executed")


async def vehicleWorker():
    while True:
        await asyncio.sleep(2)
        print("Vehicle Task Executed")
        
        
loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(phoneWorker())
    asyncio.ensure_future(vehicleWorker())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()