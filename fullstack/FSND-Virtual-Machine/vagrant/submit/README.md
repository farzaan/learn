# Logs Analysis

## Project Description

+ The purpose of this project is top work with databases and glean information from them.
+ The script executes sql queries on the 'news' datbase and formats and writes the results to a text file. It gives the top 3 most viewed articles of the website, the top 3 most viewed authors of the website and the day that "404 NOT FOUND" errors reached greater than 1%.
+ This project used a virtual machine through vagrant, postgreSQL, and python.

## Requirements

+ PostgreSQL

+ Python 2.7.12

+ psycopg2

## Database Set-up

Download [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip "newsdata.sql")

To load the data, use the command ``` psql -d news -f newsdata.sql ```

**The results are in the following files:**

* author_report.txt
* error_rates.txt
* view_report.txt


## How to run

To run the code execute the following:
	
```python
	python logs_analysis.py
```

