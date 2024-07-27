from pyftpdlib.handlers import FTPHandler
import requests, os
from config.config import Config

class FileFTPHandler(FTPHandler):
    def on_file_received(self, file):
        with open(file, 'rb') as f:
            file_bytes = f.read()
        
        response = requests.put(
            f"{Config.ntfy_serv}{Config.ntfy_topic}",
            data=file_bytes,
            headers={"Title":"The camera detect movement!", "Filename": file, "Priority": "max"}
        )

        if response.status_code == 200:
            os.remove(file)
        else:
            pass

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
