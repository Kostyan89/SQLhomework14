import sqlite3
from flask import jsonify


path_sql = 'netflix.db'


def run_sql(sql):
    with sqlite3.connect(path_sql) as conn:
        cursor = conn.cursor()
        results = cursor.execute(sql).fetchall()
    return results


def make_result(*fields, data):
    results = []
    for line in data:
        results_line = {}
        for i, field in enumerate(fields):
            results_line[field] = line[i]
        results.append(results_line)
    return results


def get_movies_by_listed_in(listed_in):
    sql = f'''SELECT title, description FROM netflix WHERE listed_in = '{listed_in}' 
    ORDER BY date_added
    LIMIT 10'''
    results = run_sql(sql)
    return jsonify(make_result('title', 'description', data=results))

