#!/usr/bin/env python

# Log Analysis Project

# Import PostgreSQL Database Management
import psycopg2

# Import Datetime and Date
from datetime import date

# Global Database Name
DBNAME = 'news'


# Connects to Database and Executes Queries
def con_news_Query(query):
    try:
        db = psycopg2.connect('dbname=' + DBNAME)
        c = db.cursor()
        c.execute(query)
        rows = c.fetchall()
        db.close()
        return rows
    except BaseException:
        print("Connection to database has failed")


# Queries to be Executed for Project

# 1. What are the most popular three articles of all time?
def popular_articles_show():
    query = """SELECT title, COUNT(log.id) AS views
            FROM articles, log
            WHERE log.path = CONCAT('/article/', articles.slug)
            GROUP BY articles.title ORDER BY views desc LIMIT 3;"""
    three_pop_articles = con_news_Query(query)
    # Show query and add new line
    print('\n' +
          '1. What are the most popular three articles of all time?' +
          '\n')
    # Show query answer and add new line
    print(' Top Three Articles by Page View' +
          '\n')
    for i in three_pop_articles:
        print(' * ' +
              '"' + i[0] + '" - ' + str(i[1]) + " views")


# 2. Who are the most popular article authors of all time?
def popular_authors_show():
    query = """SELECT name, sum(articles_viewed.views) AS views
            FROM author_of_articles, articles_viewed
            WHERE author_of_articles.title = articles_viewed.title
            GROUP BY name ORDER BY views desc;"""
    three_pop_authors = con_news_Query(query)
    # Show query and add new line
    print('\n' +
          '2. Who are the most popular article authors of all time?' +
          '\n')
    # Show query answer and add new line
    print(' Most Popular Authors' + ' by Total Views:' +
          '\n')
    for i in three_pop_authors:
        print(' * ' +
              i[0] + ' - ' + str(i[1]) + ' views')


# 3. On which days did more than 1% of requests lead to errors?
def percentage_error_show():
    query = """SELECT d_error.day,
            ROUND(
            ((d_error.d_error/final.final) * 100)::DECIMAL, 2)::TEXT
            as percentage
            FROM d_error, final
            WHERE final.day = d_error.day
            AND (((d_error.d_error/final.final) * 100) > 1.0)
            ORDER BY d_error.day;"""
    error_requests = con_news_Query(query)
    # Show Query and add new line
    print('\n' +
          '3. On which days did more than 1% of requests lead to errors?' +
          '\n')
    # Show Query Answer and add new line
    print(' Days Where Errors Exceeded 1%' + ' of Total Views' +
          '\n')
    for i in error_requests:
        print(' * ' +
              i[0].strftime('%B %d, %Y') + " - " + i[1] + "%" + " errors")
    # Show Statement on Last Query
    print('\n' + ' Queries Finished Successfully' + '\n')

if __name__ == '__main__':
    print('\n' + "**** Executing Queries ****")
    popular_articles_show()
    popular_authors_show()
    percentage_error_show()
