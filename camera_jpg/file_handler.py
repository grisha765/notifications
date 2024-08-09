import asyncio
import aiohttp
import os
from pyftpdlib.handlers import FTPHandler
from config.config import Config

class FileFTPHandler(FTPHandler):
    async def process_file_received(self, file):
        async with aiohttp.ClientSession() as session:
            with open(file, 'rb') as f:
                file_bytes = f.read()

            async with session.put(
                f"{Config.ntfy_serv}{Config.camera_topic}",
                data=file_bytes,
                headers={"Title": "The camera detect movement!", "Filename": file, "Priority": "max"}
            ) as response:

                if response.status == 200:
                    os.remove(file)

    def on_file_received(self, file):
        asyncio.run(self.process_file_received(file))

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")


