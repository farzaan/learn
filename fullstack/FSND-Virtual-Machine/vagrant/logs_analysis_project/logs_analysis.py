import psycopg2

import csv

DBNAME = "news"

def top_articles():
    DB = psycopg2.connect(database = DBNAME)
    c = DB.cursor()
    c.execute("select a.title, count(a.title) as cnt from articles as a, log as l where a.slug = replace(l.path, '/article/', '') group by a.title order by cnt desc limit 3")
    posts = c.fetchall()
    DB.close()
    return posts  

if __name__ == '__main__':



    data = top_articles()

    with open('view_report.txt','wb') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['TITLE','VIEWS'])
        for row in data:
            csv_out.writerow(row)    
       