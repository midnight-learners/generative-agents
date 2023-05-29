import os
from pathlib import Path
import tomllib

# root dir of the project
PROJECT_ROOT_DIR = Path(__file__).parent.parent

# path to asserts dir
ASSETS_DIR = PROJECT_ROOT_DIR.joinpath('assets')

# path to .env file
ENV_FILEPATH = ASSETS_DIR.joinpath('.env')
assert ENV_FILEPATH.exists(), f'{ENV_FILEPATH} does not exist'

# keys of env variables
KEY_OF_MYSQL_USER = 'MYSQL_USER'
KEY_OF_MYSQL_PASSWORD = 'MYSQL_PASSWORD'
KEY_OF_OPENAI_API_KEY = 'OPENAI_API_KEY'

# path to prompt templates file
PROMPTS_FILEPATH = ASSETS_DIR.joinpath('prompts').with_suffix('.toml')
assert PROMPTS_FILEPATH.exists(), f'{PROMPTS_FILEPATH} does not exist'


def load_prompts(filepath: os.PathLike) -> str:
    
    with open(filepath, 'rb') as f:
        prompts = tomllib.load(f)
    
    return prompts

# prompt templates
PROMPTS = load_prompts(PROMPTS_FILEPATH)