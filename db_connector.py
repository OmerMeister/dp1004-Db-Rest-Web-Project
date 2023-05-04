import pymysql

# Establishing a connection to DB and getting cursor
schema_name = "sql7615064"
conn = pymysql.connect(host='sql7.freemysqlhosting.net', port=3306, user='sql7615064', passwd='rRsh6tSbEB',
                       db=schema_name)
conn.autocommit(True)
cursor = conn.cursor()


# serving the GET method, the "cursor.fetchone" returns a tuple
# if any error happens instead for getting a value from the db, the function
# will return 0
def db_get(user_id):
    try:
        cursor.execute(f"SELECT * FROM users where user_id='{user_id}';")
        user_name = cursor.fetchone()[1]  # fetchone returns a tuple
        return user_name
    except Exception as e:
        print("db error: ", e)  # for debugging
        return 0


# gets the whole table of users
def db_get_all():
    try:
        cursor.execute(f"SELECT user_id , user_name FROM users;")
        all_users = cursor.fetchall()  # fetchall returns a tuple
        return str(all_users)  # returns tuple in shape of a string
    except Exception as e:
        print("db error: ", e)  # for debugging
        return 0


# serving the POST method, checks that the id is a number and not already taken
# then, send the request to the db. if all goes well, returns 1 else returns 0
def db_post(user_id, user_name, creation_time):
    try:
        # checks that the id input is a number
        user_id = int(user_id)
        # checks if there is a user with that specific id
        cursor.execute(f"SELECT * FROM users WHERE user_id = '{user_id}';")
    except:
        print("db: int conversion error")  # for debugging
        return 0
    if cursor.rowcount > 0:
        print("db: id already exists.")  # for debugging
        return 0
    try:
        cursor.execute(
            f"INSERT INTO users (user_id, user_name, creation_date) VALUES ('{user_id}', '{user_name}', '{creation_time}');")
        return 1
    except Exception as e:
        print("db error occurred: ", e)  # for debugging
        return 0


# serving the PUT method, checks that the id exists. if it does.
# the method will update the row and return 1. if not, will return 0
def db_put(user_id, user_name, creation_date):
    try:
        # checks that the id input is a number
        user_id = int(user_id)
    except:
        print("db: int conversion error")  # for debugging
        return 0
    try:
        # used to check if there is a user with that specific id
        cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{user_id}';")
    except TypeError:
        print("db error: no such id.")  # for debugging
        return 0
    try:
        cursor.execute(
            f"UPDATE users SET user_name = '{user_name}', creation_date= '{creation_date}' WHERE user_id = {user_id};")
        return 1
    except Exception as e:
        print("db error occurred: ", e)  # for debugging
        return 0


# serving the DELETE method of "users", checks that the id exists. if it does.
# the method will delete the row and return 1. if not, will return 0
def db_delete(user_id):
    try:
        # checks that the id input is a number
        user_id = int(user_id)
    except:
        print("int conversion error")  # for debugging
        return 0
    try:
        # used to check if there is a user with that specific id
        cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{user_id}';")
        user_name = cursor.fetchone()[0]
    except TypeError:
        print("db error: no such id.")  # for debugging
        return 0
    try:
        cursor.execute(f"DELETE FROM users WHERE user_id = {user_id};")
        return user_name
    except Exception as e:
        print("db error occurred: ", e)  # for debugging
        return 0
