from api.init import app,db,per_page
from api.init import Book, Song
from flask import Flask, request, jsonify,render_template

from flask_sqlalchemy import pagination 
import os
from api.service.commit_file import commit_file

@app.route("/")
def home():
  return render_template('home.html')

@app.route('/commit', methods=['POST'])
def update_file():
    data = request.json

    if 'content' not in data:
        return jsonify({"status": "error", "message": "contentが見つかりません"}), 400

    result = commit_file(data['content'])
    status_code = 200 if result["status"] == "success" else 500

    return jsonify(result), status_code