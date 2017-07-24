#!/usr/bin/env python

import psycopg2

DBNAME = "news"


def get_data_by_query(strSQL):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)

    Returns:
        A list of tuples containing the results of the query.
    """
    DB = psycopg2.connect(database=DBNAME)
    c = DB.cursor()
    c.execute(strSQL)
    results = c.fetchall()

    DB.close()

    return results


def top_articles():
    """Perform and output sql query for top articles

    Keyword arguments:
    None

    Returns:
        A list of tuples containing the results of the query.
    """
    strSQL = """select a.title,
             count(a.title) as cnt from articles as a, log
             as l where a.slug = replace(l.path, '/article/', '')
             group by a.title order by cnt desc limit 3"""

    posts = get_data_by_query(strSQL)

    return posts


def top_authors():
    """Perform and output sql query for top authors

    Keyword arguments:
    None

    Returns:
        A list of tuples containing the results of the query.
    """
    strSQL = """select c.name,
             count(c.id) as cnt from articles as a, log as l, authors as c
             where l.path = '/article/' || a.slug
             and a.author = c.id group
             by c.name, c.id order by cnt desc limit 3"""

    posts = get_data_by_query(strSQL)

    return posts


def error_rates():
    """Perform and output sql query for error rates.

    Keyword arguments:
    None

    Returns:
        A list of tuples containing the results of the query.
    """

    strSQL = """select date(time),
            round(CAST(float8
            (100 * CAST(SUM(CAST((status = '404 NOT FOUND')
            AS INT)) as DOUBLE PRECISION)
             / count(status)) as numeric), 2)
            as s
            from log
            group by date(time) order by s desc limit 1"""

    error_rates = get_data_by_query(strSQL)

    return error_rates


def write_data_to_file(data, fName, strHeader,
                       cols=['TITLE', 'VIEWS'],
                       showPercent=False):

    """Writes sql query output to text fi;es.

    Keyword arguments:
    data -- the real part (default 0.0)
    fName -- the imaginary part (default 0.0)
    strHeader -- the header for output file
    cols -- description for columns of output
    showPercent -- boolean checking for wether to write output as percent
    """

    lb = "\n"
    print("Writing to file", fName)
    with open(fName, 'wb') as out:

        out.write(strHeader + lb)
        out.write('-' * len(strHeader) + lb)

        for row in data:
            title = row[0]
            value = row[1]
            if(showPercent):
                strData = "\"{0}\" -- {1}% {2} {3}".format(title,
                                                           value,
                                                           cols[1].lower(),
                                                           lb)
            else:
                strData = "\"{0}\" -- {1} {2} {3}".format(title,
                                                          value,
                                                          cols[1].lower(),
                                                          lb)
            out.write(strData + lb)


if __name__ == '__main__':

    data = top_articles()
    write_data_to_file(data,
                       'view_report.txt',
                       "Top three articles sorted by views",
                       ['ARTICLE', 'VIEWS'])

    info = top_authors()
    write_data_to_file(info,
                       'author_report.txt',
                       "Author Rank by Article Views",
                       ['AUTHOR', 'VIEWS'])

    errors = error_rates()
    write_data_to_file(errors,
                       'error_rates.txt',
                       "Dates With More Than 1% Error Rate",
                       ['DATE', 'ERRORS'],
                       True)
