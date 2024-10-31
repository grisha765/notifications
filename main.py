from config.config import Config
from config import logging_config
logging = logging_config.setup_logging(__name__)

logging.info(f"Script initialization, logging level: {Config.log_level}")
logging.info(f"Notify link: {Config.ntfy_serv}{Config.camera_topic}")

def main():
    from core.ftp import run_ftp
    ftp_server = run_ftp()
    try:
        logging.info(f"Starting FTP server on address: {Config.ip}:{Config.port}")
        ftp_server.serve_forever(handle_exit=False)
    except (KeyboardInterrupt, SystemExit):
        logging.info("Stopping FTP server...")
        ftp_server.close()
        logging.info("FTP server stopped.")

if __name__ == '__main__':
    main()
