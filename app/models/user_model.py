#!flask/bin/python
from flask import jsonify
import MySQLdb as MySQL
import traceback

HOST = "127.0.0.1"
USER = "root"
PASSWORD = "cs411fa2016"
DB = "imdb"


def check_existing_user(email):
    try:
        conn = MySQL.connect(host=HOST, user=USER, passwd=PASSWORD, db=DB)
        cursor = conn.cursor()
    except MySQL.Error as e:
        print "SQL Connection Error"
        conn.rollback()
        raise
        return False, "MySQL error"

    check_query = "SELECT * FROM USER WHERE EMAIL = '%s'" % email
    try:
        x = cursor.execute(check_query)
        if x != 0:
            return True, "User Exists"
        return False, None
    except MySQL.Error as e:
        conn.rollback()
        raise
        return True, "SQL connection error"


def add_user(first_name, last_name, email, age, password, runtime, year, occupation, gender):
    try:
        conn = MySQL.connect(host=HOST, user=USER, passwd=PASSWORD, db=DB)
        cursor = conn.cursor()
    except MySQL.Error as e:
        print "SQL Connection Error"
        conn.rollback()
        raise
        return False, "MySQL error"
    insert_query = "INSERT INTO USER VALUES(FIRST_NAME, LAST_NAME, EMAIL, AGE, PASSWORD, Runtime, Year, OCCUPATION, GENDER) \
        VALUES ('%s', '%s', '%s', '%d', '%s', '%d', '%d', '%s', '%s' )" % (first_name, last_name, email, age, password, runtime, year, occupation, gender)
    try:
        cursor.execute(insert_query)
        conn.commit()
        _id = cursor.lastrowid
        return _id
    except MySQL.Error as e:
        traceback.print_exc()
        conn.rollback()
        return -1


def update_user_by_id(user_id, first_name, last_name, age):
    try:
        conn = MySQL.connect(host=HOST, user=USER, passwd=PASSWORD, db=DB)
        cursor = conn.cursor()
    except MySQL.Error as e:
        print "SQL Connection Error"
        conn.rollback()
        raise
        return False, "MySQL error"
    update_query = "UPDATE USER SET FIRST_NAME='%s', LAST_NAME='%s',  AGE='%d' WHERE USERID='%d'" % (
        first_name, last_name, age, user_id)
    try:
        cursor.execute(update_query)
        conn.commit()
        return True, "User updated successfully"
    except MySQL.Error as e:
        conn.rollback()
        raise
        return False, "MySQL error"


def get_user_by_id(user_id):
    try:
        conn = MySQL.connect(host=HOST, user=USER, passwd=PASSWORD, db=DB)
        cursor = conn.cursor()
    except MySQL.Error as e:
        print "SQL Connection Error"
        conn.rollback()
        raise
        return False, None, "MySQL error"
    query = "SELECT * FROM USER WHERE USERID = " + str(user_id)
    try:
        x = cursor.execute(query)
        if x == 0:
            return False, None, "No such user exists"

        result = cursor.fetchone()

        userid = result[0]
        first_name = result[1]
        last_name = result[2]
        email = result[3]
        age = result[4]
        password = result[5]
        runtime = result[6]
        year = result[7]
        occupation = result[8]
        gender = result[9]

        person = {"USERID": userid, "FIRST_NAME": first_name,
                  "LAST_NAME": last_name, "EMAIL": email, "AGE": age, "Password":password, "Runtime":runtime, "Year":year,"Occupation": occupation, "Gender": gender}

        return True, person, "Person found"

    except MySQL.Error as e:
        conn.rollback()
        raise
        return False, None, "SQL connection error"


def get_user_by_email_search(email_id):
    try:
        conn = MySQL.connect(host=HOST, user=USER, passwd=PASSWORD, db=DB)
        cursor = conn.cursor()
    except MySQL.Error as e:
        print "SQL Connection Error"
        conn.rollback()
        raise
        return False, None, "MySQL error"
    query = "SELECT * FROM USER WHERE EMAIL = '%s'" % email_id
    try:
        x = cursor.execute(query)
        if x == 0:
            return False, None, "No such user exists"

        result = cursor.fetchone()

        userid = result[0]
        first_name = result[1]
        last_name = result[2]
        email = result[3]
        age = result[4]

        person = {"USERID": userid, "FIRST_NAME": first_name,
                  "LAST_NAME": last_name, "EMAIL": email, "AGE": age}

        return True, person, "Person found"

    except MySQL.Error as e:
        conn.rollback()
        raise
        return False, None, "SQL connection error"
