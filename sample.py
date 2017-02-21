#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 10:08:22 2017

@author: katayama
"""
import pymongo
import pandas as pd
from pandas import Series, DataFrame
import requests

#%% start main
if __name__ == "__main__":
  
  # target_url
  url = "https://{username}:{password}@api.github.com".format(
      username=input("Username: "),
      password=input("Password: "),
  )

  # mongodb
  client = pymongo.MongoClient("localhost", 27017)
  db = client.github
  collection = db.repositories
  
  # set initial value
  df_list = list()
  rate_limit = 1
  since = 1

  # get
  while rate_limit:
    res = requests.get(url + "/repositories", params=dict(since=since))
    print(res.url)
    df = pd.read_json(res.content)
    collection.insert_many(res.json())
    
    rate_limit = res.headers.get("x-ratelimit-limit")
    since = df.id.max()
    