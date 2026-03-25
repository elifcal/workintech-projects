# Environment Variables in Python

This project demonstrates how to use environment variables in Python programs and how to dynamically manage the flow of the code using external inputs.

## Concepts Learned
- Using Python's built-in os module and the os.getenv() function.
- The logic of configuring a program externally based on the working environment (development or production) instead of hardcoding values.
- Setting default (fallback) behaviors to prevent errors when an environment variable is not defined (empty mode).

## Project Content
The flask_option.py file in this project contains a start() function that checks for an environment variable named FLASK_ENV. The program returns a different startup message depending on the terminal command used to run it.

## How to Run

You can test the program by defining different environment variables via the terminal as follows:

1. To run in development mode:
```bash
FLASK_ENV=development python flask_option.py
```

2. To run in production mode:
```bash
FLASK_ENV=production python flask_option.py
```

3. To run without specifying any variable (Empty mode):
```bash
python flask_option.py
```
