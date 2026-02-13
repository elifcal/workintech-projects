Data Git Project
Overview
The goal of this project is to master the fundamental version control workflow using Git. It involves implementing basic Python functions while strictly following a professional development cycle, including status checks, staging, multiple commits, and style enforcement.

Project Requirements
The project consists of two primary functions implemented in today.py:

my_name_is(): Returns the developer's name.

my_buddy_is(): Returns the names of designated project buddies.

Technical Workflow
1. Version Control Lifecycle
The project was developed using a step-by-step Git sequence to ensure a clean commit history:

Status Monitoring: Frequent use of git status to verify the state of the working directory.

Incremental Commits: Each function was committed separately after passing its respective test to demonstrate an organized history.

Remote Synchronization: Used git pull --rebase and git push to maintain synchronization with the remote repository.

2. Testing and Automation
The project utilizes a Makefile to streamline the testing and linting process.

Unit Testing: Executed via pytest (triggered by make) to validate the return values of the functions.

Diff Analysis: Used git diff to review code changes before finalizing commits.

3. Code Quality (Linting)
To meet professional standards, the code was audited using Pylint.

Docstrings: Comprehensive module-level and function-level docstrings were added to provide clear documentation.

PEP 8 Compliance: Ensured correct indentation (4 spaces) and naming conventions to achieve a perfect 10/10 Pylint score.
