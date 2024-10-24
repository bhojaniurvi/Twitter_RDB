# """
# DS4300: Large-Scale Information Storage and Retrieval
# Homework 1: Twitter Engineering
# Urvi Bhojani, Rishita Shroff
# January 19th, 2023
#
# Twitter Engineering Database API for MySQL
# """
# from dbutils import DBUtils
# from hw1_objects import Tweets, Follow
#
# class TwitterEngineeringAPI:
#
#     def __init__(self, user, password, database, host="localhost"):
#         self.dbu = DBUtils(user, password, database, host)

# import required libraries
import pymysql
import pandas as pd

# connect to MySQL server and database
cnx = pymysql.connect(host='localhost', user='root', password='PL2007pl', db='twitter_engineering',
                      cursorclass=pymysql.cursors.DictCursor)

# Create a cursor
cursor = cnx.cursor()

df_tweet = pd.read_csv("")

def read_tweets():
    try:
       cursor.callproc('readTweet')
       rows = cursor.fetchall()
       for row in rows:
           print(row)
    except pymysql.Error as e:
        print(f"Error reading the record: {e}")