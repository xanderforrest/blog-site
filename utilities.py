import json
import sqlite3
from datetime import datetime
from uuid import uuid4
import time


class ContentManager:
    def __init__(self):
        self.conn = sqlite3.connect("default.db", check_same_thread=False)
        self.c = self.conn.cursor()

        self.validate_tables()

    @staticmethod
    def generate_id():
        return str(uuid4()).replace("-", "")

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
            np["id"] = p[0]
            np["heading"] = p[1]
            np["short"] = p[2]
            np["date"] = datetime.utcfromtimestamp(int(p[3])).strftime("%A %d %B, %Y")
            np["intro"] = p[4]
            np["image"] = p[5]
            clean_posts.append(np)

        return clean_posts

    def add_post(self, post_data):
        """
        Add a post to the DB from JSON format
        :param post_data: Dictionary containing post information
        """

        pd = post_data
        id = self.generate_id()

        self.c.execute("""
INSERT INTO TBLPosts VALUES ((?), (?), (?), (?), (?), (?));
        """, (id, pd["heading"], pd["short"], pd["date"], pd["intro"], pd["image"]))
        self.conn.commit()
