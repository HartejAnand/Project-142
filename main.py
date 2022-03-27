from flask import Flask, jsonify, request
import pandas as pd
from storage import liked, disliked, allA

df=pd.read_csv('article.csv')

app = Flask(__name__)

@app.route("get")
def get_article():
    global df
    data = {        
        "title": df[0][12],
    }
    return jsonify({
        "data": data,
        "status": "success!"
    })

@app.route("/liked", methods=["POST"])
def liked_atricle():
    likedA = df[0]
    liked.append(likedA)
    df.pop(0)
    return jsonify({
        "status": "success :)"
    }), 201

@app.route("/disliked", methods=["POST"])
def disliked_atricle():
    dislikedA = df[0]
    disliked.append(dislikedA)
    df.pop(0)
    return jsonify({
        "status": "success"
    }), 201


if __name__ == "__main__":
  app.run()