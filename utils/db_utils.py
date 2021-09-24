from datetime import datetime
from app import app

db = []


def filter_last_day_orders():
    today_date = datetime.today().date()
    last_day_oreders = []
    if len(db) > 0 :
        for order in db :
            # add only last day orders to the returned list
            db_order_date = order['date']
            if today_date == db_order_date:
                # convert date to serializble type - str.
                str_date = datetime.strftime(order['date'], '%Y-%m-%d')
                order['date'] = str_date

                # add to response json
                last_day_oreders.append(order)
    else:
        raise ValueError('There is no orders to retrieve.')
    return last_day_oreders


def validate_order(order):
    today_date = datetime.today().date()
    db_new_order = {} # copy payload into new dict to ignore more data if recieved.

    for key in order:

        if key == 'name' :
            if len(order[key]) == 0: # check if not empty string.
                raise ValueError("Wrong value for '{}' key, shouldnt be empty string".format(key))
            db_new_order[key] =  order[key]

        elif key == 'price' :
            if order[key] < 0 : # check if not negative price.
                raise ValueError("Wrong value for '{}' key, must be positive integer".format(key))
            db_new_order[key] =  order[key]
        elif key == 'date' :
            try:
                order_date = order[key].split("T")[0] # ignore time-zone.
                order[key] = datetime.strptime(order_date, '%Y-%m-%d').date() # cast to date
                if order[key] != today_date : raise ValueError() # check if not today date.
                db_new_order[key] =  order[key]
            except ValueError:
                raise ValueError("Only today's date and YYYY-MM-DD date format are allowed")
    
    db.append(order)