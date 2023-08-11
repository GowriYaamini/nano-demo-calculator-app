from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data=request.get_json()
    if "first" in data and "second" in data:
        return jsonify({"result":data["first"]+data["second"]})
    else:
        return jsonify({"error":"values missing"})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data=request.get_json()
    if "first" in data and "second" in data:
        return jsonify({"result":data["first"]-data["second"]})
    else:
        return jsonify({"error":"values missing"})

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
