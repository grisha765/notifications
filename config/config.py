import os

class Config:
    log_level: str = "INFO"
    ftp_user: str = 'user'
    ftp_passwd: str = '12345'
    ip: str = "0.0.0.0"
    port: int = 2121
    ntfy_serv: str = "https://ntfy.sh/"
    camera_topic: str = "ergolyam"

    @classmethod
    def load_from_env(cls):
        for key, value in cls.__annotations__.items():
            env_value = os.getenv(key.upper())
            if env_value is not None:
                if isinstance(value, int):
                    setattr(cls, key, int(env_value))
                else:
                    setattr(cls, key, env_value)

Config.load_from_env()

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
