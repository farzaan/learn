import psycopg2

import csv

DBNAME = "news"


def get_data_by_query(strSQL):

    DB = psycopg2.connect(database=DBNAME)
    c = DB.cursor()
    c.execute(strSQL)
    results = c.fetchall()

    DB.close()

    return results


def top_articles():

    strSQL = "select a.title,\
             count(a.title) as cnt from articles as a, log\
             as l where a.slug = replace(l.path, '/article/', '')\
             group by a.title order by cnt desc limit 3"

    posts = get_data_by_query(strSQL)

    return posts


def top_authors():

    strSQL = "select c.name,\
             count(c.id) as cnt from articles as a, log as l, authors as c \
             where a.slug = replace(l.path,'/article/', '')\
             and a.author = c.id group \
             by c.name, c.id order by cnt desc limit 3"

    posts = get_data_by_query(strSQL)

    return posts



def error_rates():

    strSQL = "select date(time) ,\
             round(CAST(float8(100 * CAST(SUM\
             (CAST((status = '404 NOT FOUND')AS INT))\
             as DOUBLE PRECISION) / SUM(CAST((status ='200 OK')  AS INT)))\
             as numeric), 2) as p\
             from log group by date(time) order by p desc limit 1"

    error_rates = get_data_by_query(strSQL)

    return error_rates



def write_data_to_file(data, fName, cols=['TITLE', 'VIEWS']):

    lb = "\n" # lineBreak
    print("Writing to file", fName)
    with open(fName, 'wb') as out:
        #csv_out = csv.writer(out)
        out.write(cols + lb)

        for row in data:
            title = row[0]
            value = row[1]
            strData = "\"{0}\" -- {1} {2} {3}".format(title, value, cols[1].lower(), lb)
            out.write(strData + lb)


if __name__ == '__main__':

    data = top_articles()
    write_data_to_file(data, 'view_report.txt', ['TITLE', 'VIEWS'])

    info = top_authors()
    write_data_to_file(info, 'author_report.txt', ['AUTHOR', 'VIEWS'])

    errors = error_rates()
    write_data_to_file(errors, 'error_rates.txt', ['DATE', 'ERROR_RATE'])

