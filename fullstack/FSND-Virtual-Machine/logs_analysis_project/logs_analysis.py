import psycopg2

DBNAME = "news"

def top_articles():
    DB = psycopg2.connect(database = DBNAME)
    c = db.cursor()
    c.execute("select * from authors")
    