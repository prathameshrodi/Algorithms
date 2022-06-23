import asyncio

from websockets import serve

from server_log import ReadFile


class Serve:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    async def tail_command(self, websocket):
        lp = 0
        while True:
            data, lp = ReadFile().read_file(lp)
            if data:
                await websocket.send(data.decode('utf-8'))

    async def run(self):
        async with serve(self.tail_command, self.__host, self.__port):
            await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(Serve('localhost', 8757).run())
