from flask import Flask, request, jsonify, abort
from functions import *


app = Flask(__name__)


@app.route('/movie')
def movie_title():
    results = []
    name = request.args.get('s')
    if name:
        sql = f"SELECT title, country, release_year, listed_in, description from netflix WHERE lower(title) LIKE '%{name.lower()}%'ORDER BY release_year desc limit 1"
        results = run_sql(sql)
    abort(404)
    return jsonify(make_result('title', 'country', 'genre', 'description', data=results)[0])





if __name__ == '__main__':
    app.run()
