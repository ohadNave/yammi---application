from datetime import datetime


today_date = today_date = datetime.today().date()


valid_order1 = {"name": "Pizza",
            "price": 10,
            "date": today_date}

valid_order2 = {"name": "Hamburger",
            "price": 15,
            "date": today_date}

valid_order3 = {"name": "Pancake",
            "price": 20,
            "date": "2021-09-23"}


invalid_order1 = {"name": "",
            "price": "10",
            "date": today_date}
