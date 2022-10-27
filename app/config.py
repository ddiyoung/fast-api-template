from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "port": os.environ.get("PORT"),
    "mysql_host": os.environ.get("MYSQL_HOST"),
    "mysql_port": os.environ.get("MYSQL_PORT"),
    "mysql_user": os.environ.get("MYSQL_USER"),
    "mysql_password": os.environ.get("MYSQL_PASSWORD"),
    "mysql_database": os.environ.get("MYSQL_DATABASE"),
}

print(config['port'])