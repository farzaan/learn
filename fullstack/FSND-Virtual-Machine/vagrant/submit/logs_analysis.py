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

def top_authors():
    DB = psycopg2.connect(database = DBNAME)
    c = DB.cursor()
    c.execute("select c.name, count(c.id) as cnt from articles as a, log as l, authors as c where a.slug = replace(l.path,'/article/', '') and a.author = c.id group by c.name, c.id order by cnt desc limit 3")
    posts = c.fetchall()
    DB.close()
    return posts  

#news=> select date(time), count(status) from log where status = '404 NOT FOUND' as a group by date(time), status = '404 NOT FOUND';
def error_rates():

    strsql = "select date(time) ,\
            round( CAST(float8 (100 * CAST(SUM(CAST((status = '404 NOT FOUND')  AS INT)) as DOUBLE PRECISION) / SUM(CAST((status ='200 OK')  AS INT))) as numeric), 2) as p\
            from log group by date(time) order by p desc limit 1"

    DB = psycopg2.connect(database = DBNAME)
    c = DB.cursor()
    c.execute(strsql)
    error_rates = c.fetchall()
    DB.close()
    return error_rates

if __name__ == '__main__':



    data = top_articles()

    with open('view_report.txt','wb') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['TITLE','VIEWS'])
        for row in data:
            csv_out.writerow(row)

    info = top_authors()

    with open('author_report.txt','wb') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['AUTHOR','VIEWS'])
        for row in info:
            csv_out.writerow(row)   


    errors = error_rates()

    with open('error_rates.txt','wb') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['DATE','ERROR_RATE'])
        for row in errors:
            csv_out.writerow(row)               
       