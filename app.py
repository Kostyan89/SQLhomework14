from flask import Flask, request, jsonify, abort
from functions import *


app = Flask(__name__)


@app.route('/movie')
def movie_title():
    results = []
    name = request.args.get('s')
    if name:
        sql = f'''SELECT title, country, release_year, listed_in, description from netflix 
        WHERE lower(title) LIKE '%{name.lower()}%'
        ORDER BY release_year desc limit 1'''
        results = run_sql(sql)
    abort(404)
    return jsonify(make_result('title', 'country', 'genre', 'description', data=results)[0])


@app.route('/movie/<int:year>')
def movie_year(year):
    results = []
    if year:
        sql = f"SELECT title, release_year FROM netflix WHERE release_year = '{year}' LIMIT 100"
        results = run_sql(sql)
    else:
        abort(404)
    print(make_result('title', 'release_year', data=results))
    return jsonify(make_result('title', 'country', 'genre', 'description', data=results))


if __name__ == '__main__':
    app.run()
