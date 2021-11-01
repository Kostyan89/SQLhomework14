import sqlite3


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
