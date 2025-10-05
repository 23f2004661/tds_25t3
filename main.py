from flask import Flask,render_template

app = Falsk(__name__)

@app.route('/')
def home():
    return render_template('hi.html')

app.run()
