from flask import Flask

app = Flask(__name__)#creating the app instance
@app.route('/home')
def home():
    return '<h2> Name: Aloyo brenda Ojera  Cohort:3 I love coding </h2>'

if __name__=='__main__':
    app.run(debug=True)