from flask import Flask, render_template, request, jsonify

app =Flask(__name__)

@app.route('/')
def index():
    num = 300
    num1 = 400
    theSum = num +num1
    return "<h1>Our sum is {}<h1>".format(theSum)
@app.route('/home/<name>')
def home(name):
    return "<h1>Hello {}</h1>".format(name)
@app.route('/about')
def about():
    return render_template("base.html")

@app.route('/user')
def user():
    return render_template("formdata.html")

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    someuse ={
        'name':name,
        'location':location
    }
    return jsonify(someuse)

if __name__ == '__main__':
    app.run(debug=True)
