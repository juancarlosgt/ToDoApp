@echo off

rem Command to start the development server
if "%1"=="runserver" (
    call .\venv\Scripts\activate.bat
    python manage.py runserver
)

rem Command to apply migrations
if "%1"=="migrate" (
    call .\venv\Scripts\activate.bat
    python manage.py migrate
)

rem Command to lint a specific file with flake8
if "%1"=="lint" (
    call .\venv\Scripts\activate.bat
    flake8 %2
    black %2
)

rem Command Activate venv
if "%1"=="activate" (
    call .\venv\Scripts\activate.bat
)
