# bank.py
import json
import random
import string
from pathlib import Path

class Bank:
    db = "Data.json"
    data = []

    @classmethod
    def load_data(cls):
        if Path(cls.db).exists():
            with open(cls.db) as fs:
                cls.data = json.load(fs)
        else:
            cls.data = []

    @classmethod
    def __accountNo(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spc = random.choices("$%&*@/!", k=1)
        id = alpha + num + spc
        random.shuffle(id)
        return "".join(id)

    @classmethod
    def __update(cls):
        with open(cls.db, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def create_account(cls, name, age, email, pin):
        if age < 18 or len(pin) < 4:
            return None
        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "acNo": cls.__accountNo(),
            "balance": 0
        }
        cls.data.append(info)
        cls.__update()
        return info

    @classmethod
    def find_user(cls, acNo, pin):
        return next((i for i in cls.data if i["acNo"] == acNo and i["pin"] == pin), None)

    @classmethod
    def deposit(cls, acNo, pin, amount):
        user = cls.find_user(acNo, pin)
        if user and amount > 0:
            user["balance"] += amount
            cls.__update()
            return user["balance"]
        return None

    @classmethod
    def debit(cls, acNo, pin, amount):
        user = cls.find_user(acNo, pin)
        if user and 0 < amount <= user["balance"]:
            user["balance"] -= amount
            cls.__update()
            return user["balance"]
        return None

    @classmethod
    def update_details(cls, acNo, pin, field, new_value):
        user = cls.find_user(acNo, pin)
        if user and field in ["email", "pin"]:
            user[field] = new_value
            cls.__update()
            return True
        return False

    @classmethod
    def delete_account(cls, acNo, pin):
        user = cls.find_user(acNo, pin)
        if user:
            cls.data.remove(user)
            cls.__update()
            return True
        return False