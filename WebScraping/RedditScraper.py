#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:02:52 2020

@author: jarjar
"""


import praw, requests, re, os
from pathlib import Path

reddit = praw.Reddit(client_id='CDNgf2SIc-K-YQ', 
                      client_secret='f62SskqJG2vVVEj6ErpCko0Lc70', 
                      user_agent='Reddit WebScraping')

subredditList = ["Forest","Food","EarthPorn","carporn"]
alias = ["Forest","Food","Earth","Cars"]

num_subreddits= len(subredditList)
output_dir = "./Images/Reddit/"
img_limit = 5
counter = 1
total = num_subreddits * img_limit

for i in range(num_subreddits):
    subreddit = reddit.subreddit(subredditList[i]) 
    posts = subreddit.top(limit=img_limit)
    print("Fetching images from", alias[i], "subreddit")
    for post in posts:
        url = (post.url)
        file_name = url.split("/")
        if len(file_name) == 0:
            file_name = re.findall("/(.*?)", url)
        img_name = file_name[-1]
        if ".jpg" not in img_name:
            continue
        print("[{0}]/[{1}] {2} {3} {4}".format(counter, total, img_name, "from", alias[i]))
        counter = counter + 1
        try:
            file = "%s%s/%s" % (output_dir, alias[i], img_name)
            if Path(file).is_file():
                print("File already exists")
                continue
            r = requests.get(url)
            os.makedirs(os.path.dirname(file), exist_ok=True)            
            with open(file,"wb") as f:
                f.write(r.content)
        except Exception:
            pass
    print()
    
