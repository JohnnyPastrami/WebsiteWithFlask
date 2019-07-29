from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Website home goes here!"

@app.route('/about/')
def about():
    return "about content"

if __name__=="__main__":
    app.run(debug=True)
