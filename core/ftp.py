import asyncio
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.servers import FTPServer
from camera_jpg.file_handler import FileFTPHandler
from config.config import Config

async def run_ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user(Config.ftp_user, Config.ftp_passwd, "/tmp", perm="elradfmw")
    authorizer.add_anonymous("/tmp")

    handler = FileFTPHandler
    handler.authorizer = authorizer

    server = FTPServer((Config.ip, Config.port), handler)

    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, server.serve_forever)

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")

