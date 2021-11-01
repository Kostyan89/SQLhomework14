from flask import Flask, request, jsonify
import sqlite3


app = Flask(__name__)


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


@app.route('/movie')
def movie_title():
    results = []
    name = request.args.get('s')
    if name:
        sql = f"SELECT title, country, release_year, listed_in, description from netflix"\
              f"WHERE lower(title) LIKE '%{name.lower()}%'ORDER BY release_year desc limit 1"

        results = run_sql(sql)
    return jsonify(make_result('title', 'country', 'genre', 'description', data=results)[0])


if __name__ == '__main__':
    app.run()
