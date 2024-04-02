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

