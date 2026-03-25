# pylint: disable=missing-docstring

import os

def start():
    env_value = os.getenv("FLASK_ENV")

    if env_value == "development":
        return "Starting in development mode..."

    elif env_value == "production":
        return "Starting in production mode..."

    else:
        return "Starting in empty mode..."

if __name__ == "__main__":
    print(start())
