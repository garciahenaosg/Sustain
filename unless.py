from flask import Flask, request, redirect, render_template
app = Flask(__name__)


@app.route('/')
def Hello_World():
    return 'Hello World!'

@app.route('/success')
def success():
    return 'success!'

@app.route('/failure')
def failure():
    return 'failure :)'


@app.route('/sustain')
def sustain_function():
    author = "Me"
    name = "You"
    return render_template('index.html', author=author, name=name)

@app.route('/signup', methods = ['POST'])
def signup():
    response = request.form['response']
    print("The response is '" + response + "'")
    if response == 'happy':
        return redirect('/success')
    else:
        return redirect('/failure')

if __name__=='__main__':
     app.run()
    