from flask import Flask, request, render_template, url_for, session, redirect
import json

f = open('products.json')
products = json.load(f)


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/products')
def list_products():
    return render_template('products.jinja', products=products)


@app.route('/item/<item>')
def show_item(item):
    return render_template('item.jinja', product=products[int(item)])


app.run(debug=True)
