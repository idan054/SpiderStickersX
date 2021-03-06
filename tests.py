import asyncio

async def print_B(): #Simple async def
    print("B sms sent")

async def main_def():
    print("A main starter")
    await asyncio.gather(print_B())
    print("C title changed")
asyncio.run(main_def())