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


def get_cast_by_two_actors(name1, name2):
    sql = f'''SELECT "cast" FROM netflix WHERE "cast" = '{name1}' AND "cast" = '{name2}' > 2'''
    results = run_sql(sql)
    return jsonify(make_result("cast", data=results))


def get_movies_by_options(_type, release_year, listed_in):
    sql = f'''SELECT 'title', 'description' FROM netflix 
            WHERE 'type' = '{_type}' AND 'release_year' = '{release_year}' AND 'listed_in' = '{listed_in}' '''
    results = run_sql(sql)
    return jsonify(make_result('title', 'description', data=results))
