# AutoGO 🚘


# Setup 🔧

- clone repo
```shell
git clone https://github.com/stenwire/AutoGo.git
```
- Go into the folder
```shell
cd :\\path\\to\\AutoGO
```
- install pipenv
```shell
pip install pipenv
```
- activate pipenv
```shell
pipenv shell
```
- install dependencies
```shell
pipenv install
```
- Create a copy of `.env.example` and rename to `.env` then fill in the values
>- find the treblle keys on the treblle dashboard

- Create admin user with:
> whilst in project directory
```shell
python manage.py shell

>>> from auth.me import CustomUser

>>> CustomUser.objects.create_user(email="youremail@example.com",username="johnDoe707", password="strongpassword", is_staff=True, is_superuser=True)
```

# Testing API

Postman Docs: [click here📬](https://documenter.getpostman.com/view/16596786/2s93zFXKTM)

Swagger Docs:

- use this to generate datetime object to fill into respective fields
```python
from datetime import datetime

t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2018, month = 7, day = 14, hour = 5, minute = 55, second = 13)
t6 = t5 - t4


print("t4 =", t4)
print("t5 =", t5)
print("t6 =", t6)
```
