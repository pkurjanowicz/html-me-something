from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/ratio-beerworks')
def ratio_beerworks():
    return render_template('ratio-beerworks.html')

@app.route('/denver-beer-co')
def denver_beer_co():
    return render_template('denver-beer-co.html')

@app.route('/great-divide')
def great_divide():
    return render_template('great-divide.html')

@app.route('/cerebal-brewing')
def cerebral_brewing():
    return render_template('cerebal-brewing.html')

app.run()