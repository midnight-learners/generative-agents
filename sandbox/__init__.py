from dotenv import load_dotenv
from .utils import (
    ENV_FILEPATH
)

# load the .env configuration
assert load_dotenv(ENV_FILEPATH), \
    f'failed to load {ENV_FILEPATH}'