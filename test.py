from flask import Flask, render_template, request, make_response, abort
import requests,sys

app = Flask(__name__)

#Task-1
@app.route('/')
def homepage():
    return "<h2> Hello World-Hemant (You are on the Homepage)</h2>"

#Task-2
@app.route('/authors', methods=['GET'])
def authors():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    users = {d['id']: {'name': d['name'], 'count': 0} for d in data}
    for post in posts:
        users[post['userId']]['count'] += 1
    return render_template('authors.html', users=users)

#Task -3
@app.route('/form')
def form_fill():
    return render_template('set_cookies.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    resp = make_response(render_template('read_cookie.html'))
    if request.method == 'POST':
        user_name = request.form['name']
        user_age = request.form['age']
        resp.set_cookie('My_name', user_name)
        resp.set_cookie('My_age', user_age)

    return resp

#Task-4
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('My_name')
    age = request.cookies.get('My_age')
    return '<h2>Hello , ' + name + ' & your age is ' + age + '</h2>'


#Task-5
@app.route('/robots.txt/')
def custom403():
    abort(403)

#Task-6
@app.route('/image/')
def image():
    return render_template("hasura.html")

#Task-7
@app.route('/input')
def input():
    return render_template('input_data.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("show_result.html", result=result)


#About me
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)

