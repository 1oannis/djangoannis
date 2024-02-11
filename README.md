# Djangoannis

A repo for my test apps running in python django

## Contents

- [Get Started](#get-started)

---

## Get Started

1. Create a venv
    ```shell
    py -m venv venv
    ```

2. Activate the venv
    ```shell
    .\venv\Scripts\activate
    ```

3. Change into the Django dir
   ```shell
   cd mysite
   ```

4. Install the ```requirements.txt```
   ```shell
   pip install -r "requirements.txt"
   ```

5. Create Database tables
   ```shell
   py manage.py migrate
   ```

6. Create an admin user
    ```shell
    py manage.py createsuperuser
    ```


---

## Useful prompts

- Make migrations
   ```shell
   py manage.py makemigrations
   ```

- Check the Django project for problems
   ```shell
   py manage.py check
   ```