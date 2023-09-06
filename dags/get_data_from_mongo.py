# def get_data_from_mongo():
#     print("hello!")
# get_data_from_mongo()

import pandas as pd
import pymongo
import json
import urllib.parse

client = pymongo.MongoClient("mongodb+srv://new_user:user123@cluster2sept.ws7yhsy.mongodb.net/?retryWrites=true&w=majority")

db = client["AVD2"]
collect_name = 'AVD_practice'
collection = db[collect_name]

cursor = collection.find({})
data = list(cursor)

df = pd.DataFrame(data)

df1 = df.rename(columns=lambda  x:x.strip().lower().replace(" ", "_"))
output_path = r'E:\output.csv'
df1.to_csv(output_path,index=False)