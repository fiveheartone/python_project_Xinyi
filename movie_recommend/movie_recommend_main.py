import os.path

from flask import Flask, redirect, render_template, request, url_for
import pandas as pd
import time
from src.movie_scraping import scrape_score
from src.handling_file import handle_file


app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def download():
    if request.method == "POST":
        return redirect(url_for("recommendation_movies"))
    return render_template("download.html")


@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation_movies():
    if not os.path.exists('movie_recommend/files/BollywoodMovieRank.csv'):
        scrape_score()  # to get BollywoodMovieRank.csv

    if request.method == "POST":
        try:
            category = request.form["category"]
            number = int(float(request.form["number"]))
            result = handle_file(number, category)
            return redirect(url_for("recommendation_movies", result=result))
        except:
            return redirect(url_for("recommendation_movies", result="Please input valid number."))
    result = request.args.get("result")
    return render_template("recommend.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
