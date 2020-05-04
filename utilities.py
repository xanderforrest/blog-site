import json
import sqlite3
from datetime import datetime

posts = [{"heading": "First blog post", "short": "Introduction", "date": "1st May 2020", "intro": "THIS IS FIRST BLOG POST", "image": "/static/im.png"},
         {"heading": "Second blog post", "short": "Game",
          "date": "2nd May 2020", "intro": "second BLOG POST", "image": "/static/woh.png"}]


class ContentManager:
    def __init__(self):
        self.conn = sqlite3.connect("default.db")
        self.c = self.conn.cursor()

        self.validate_tables()

    def validate_tables(self):
        create_posts = """
CREATE TABLE IF NOT EXISTS TBLPosts (
PID TEXT PRIMARY KEY,
Heading TEXT,
Short Text,
Date INT,
Intro TEXT,
Image TEXT
);
"""
        self.c.execute(create_posts)
        self.conn.commit()

    def get_posts(self):
        """ Returns a list of formatted dictionaries for Jinja templating to load """

        raw_posts = self.c.execute("SELECT * FROM TBLPosts").fetchall()
        clean_posts = []

        for p in raw_posts:
            np = dict()
            np["heading"] = p[1]
            np["short"] = p[2]
            np["date"] = datetime.utcfromtimestamp(p[3]).strftime("%A %d %B, %Y")
            np["intro"] = p[4]
            np["image"] = p[5]
            clean_posts.append(np)

        return clean_posts







