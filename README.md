# TodoApp


<p align="center">
  <b>The members of this project are:</b><br>
  Shirley Guadalupe Celis Delgado - 1152212<br>
  Marianella Herrera Rondón - 1151495<br>
  Juan Carlos González Torres - 1152184
</p>

In this project, we use Django as our web development framework. Below, you will find the necessary steps to install Django in a virtual environment.

## Installing Django in a Virtual Environment

To keep our project dependencies separate from the main system, we will use a virtual environment. Make sure you have Python installed on your system before you begin.

1. **Create a virtual environment**: Open a terminal or command prompt and navigate to your project location. Run the following command to create a new virtual environment named 'venv':

    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment**: Depending on your operating system, the command to activate the virtual environment may vary. Use one of the following commands:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3. **Install Django**: With the virtual environment activated, you can install Django using pip, the Python package manager. Run the following command:

    ```bash
    pip install django
    ```

4. **Verify the installation**: To ensure Django has been installed correctly, you can run the following commands to check the installed version:

    ```bash
    python
    import django
    print(django.getversion())
    ```

With these steps, you will have installed Django in a virtual environment and will be ready to start developing your project using this powerful web framework.