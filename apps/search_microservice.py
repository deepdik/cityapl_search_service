import json
import requests

from flask import Flask, jsonify, Blueprint

srch = Blueprint('search', __name__, )

@srch.route('/')
def search():
    url = 'http://15.207.109.135:9200'+'/products*/_search'
    query = {
        "query":{
            "match_all": {}
        }
    }

    resp = requests.post(url, data=json.dumps(query))
    data = resp.json()
    products = []
    for hit in data['hits']['hits']:
        product = hit['_source']
        product['id'] = hit['_id']
        products.append(product)

    return jsonify(products)
