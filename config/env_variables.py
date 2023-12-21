from dotenv import load_dotenv
import os
from decouple import Config, Csv


load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
env_path = os.path.join(project_root, '.env')

config = Config(env_path)

DATABASE_URL = config('DATABASE_URL')
MAIN_SERVICE_URL = config('MAIN_SERVICE_URL')