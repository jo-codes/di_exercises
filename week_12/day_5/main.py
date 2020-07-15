from flask import Flask, request, render_template, url_for, session, redirect
import json

f = open('products.json')
products = json.load(f)


app = Flask(__name__)


@app.route('/')
def set_country():
    return render_template('home.html', data=products)


@app.route('/products')
def list_products():
    return render_template('products.html', products=products)


@app.route('/home')
def show_sales():
    return render_template('home.html')


@app.route('/item/<item>')
def show_item(item):
    return render_template('item.html', product=products[int(item)])


app.run(debug=True)
