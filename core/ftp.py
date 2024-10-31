from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.servers import FTPServer
from camera_jpg.file_handler import FileFTPHandler
from config.config import Config

def run_ftp():
    authorizer = DummyAuthorizer()
    authorizer.add_user(Config.ftp_user, Config.ftp_passwd, "/tmp", perm="elradfmw")

    handler = FileFTPHandler
    handler.authorizer = authorizer
    handler.banner = "Welcome to the FTP server"

    address = (Config.ip, Config.port)
    server = FTPServer(address, handler)
    return server

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")

