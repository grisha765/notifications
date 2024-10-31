import os, requests
from pyftpdlib.handlers import FTPHandler
from config.config import Config
from config import logging_config
logging = logging_config.setup_logging(__name__)

class FileFTPHandler(FTPHandler):
    def on_file_received(self, file):
        if file.endswith(('.jpg', '.png')):
            try:
                with open(file, 'rb') as f:
                    file_bytes = f.read()
                
                response = requests.post(
                    f"{Config.ntfy_serv}{Config.camera_topic}",
                    data=file_bytes,
                    headers={
                        "Title": "The camera detect movement!",
                        "Filename": os.path.basename(file),
                        "Priority": "max"
                    }
                )
                if response.status_code == 200:
                    logging.debug(f"File {file} was successfully sent.")
                else:
                    logging.warning(f"Failed to send file {file}. Status code: {response.status_code}")

            except Exception as e:
                logging.error(f"Error processing file {file}: {e}")
            finally:
                os.remove(file)

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
