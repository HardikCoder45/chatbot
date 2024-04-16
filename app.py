from flask import Flask, jsonify, request
from flask_cors import CORS
from chat import chatbot

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "allow_headers": ["Content-Type"], "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]}})

@app.route("/data", methods=["POST", "GET"])
def chatbot_app():
    # Get the data from the request
    query = request.data.decode("utf-8")
    sol = chatbot(query)
    if query:
        return jsonify({"query": query, "answer": sol})
    else:
        return jsonify({"query": "no query found"})

if __name__ == '__main__':
    app.run()
