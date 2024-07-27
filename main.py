from core.ftp import run_ftp_server
from config.config import Config
from config import logging_config
logging = logging_config.setup_logging(__name__)

logging.info(f"Script initialization, logging level: {Config.log_level}")
logging.info(f"Notify link: {Config.ntfy_serv}{Config.ntfy_topic}")

def main():
    run_ftp_server()

if __name__ == '__main__':
    main()
