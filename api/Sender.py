#app.py

from flask import Flask, request,jsonify #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/query-example')
def query_example():
    a=["Electronics","Tickets","Tickets"]
    return jsonify(a)



if __name__ == '__main__':
    app.run(debug=True, port=3000) #run app in debug mode on port 5000
