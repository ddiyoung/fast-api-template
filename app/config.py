from dotenv import load_dotenv
import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str = "wsw3998@naver.com"
    items_per_user: int = 50

    class Config:
        env_file = ".env"


settings = Settings(_env_file=f'{os.getenv("")}.env')

print(settings)