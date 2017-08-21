# "Database code" for the DB Forum.


import psycopg2



def get_posts():
  """Return all posts from the 'database', most recent first."""
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()
  c.execute("SELECT time, content FROM posts ORDER BY time DESC")
  posts = c.fetchall()
  DB.close()
  return posts

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  DB = psycopg2.connect("dbname=forum")
  c = DB.cursor()
  c.execute("INSERT INTO posts(content) VALUES (%s)" (content,))
  #POSTS.append((content, datetime.datetime.now()))
  DB.commit()
  DB.close()



