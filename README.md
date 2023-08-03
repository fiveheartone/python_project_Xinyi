# python_project_Xinyi
This project is a movie suggestion app based on the genres taken. This repository contains a collection of Python scripts that are designed to scrape IMDB Rating and Watching Viewers from website and recommend the best movies based on the two constraints.
## Dependencies
Based on Flask==2.3.2, Python==3.8.8 on win32. More dependencies (selenium==4.11.1, fuzzywuzzy==0.18.0 and etc.) are listed in the [requirements.txt](https://github.com/fiveheartone/python_project_Xinyi/blob/master/requirements.txt).
## Get Started
To install all the required dependencies
```
pip install -r requirements.txt
```
[movie_recommend_main.py](https://github.com/fiveheartone/python_project_Xinyi/blob/master/movie_recommend/movie_recommend_main.py): to run Flask app and its interface scripts are main.css, download.html, recommend.html. Click to update recommend csv...(see the screenshot of its interface in [download_csv.png](https://github.com/fiveheartone/python_project_Xinyi/blob/master/download_csv.png)), the web jumps to recommending page.
```
\python movie_recommend\movie_recommend_main.py
```
If there isn't BollywoodMovieRank.csv, the project will scrape data from IMDB website.
```
│  movie_recommend_main.py
│
├─files
│      BollywoodMovieDetail.csv
│      BollywoodMovieRank.csv
│
├─src
│     chromedriver.exe
│     handling_file.py
│     movie_scraping.py
│
├─static
│      main.css
│      movie.png
│
└─templates
        download.html
        recommend.html
```
[BollywoodMovieDetail.csv](https://github.com/fiveheartone/python_project_Xinyi/blob/master/movie_recommend/files/BollywoodMovieDetail.csv): downloaded from https://github.com/calci/bollywood-movie-dataset/blob/master/BollywoodMovieDetail.csv

[BollywoodMovieRank.csv](https://github.com/fiveheartone/python_project_Xinyi/blob/master/movie_recommend/files/BollywoodMovieRank.csv): the output of movie_scraping.py.

[movie_scraping.py](https://github.com/fiveheartone/python_project_Xinyi/blob/master/movie_recommend/src/movie_scraping.py): to scrape data from IMDB website with version ChromeDriver 115.0.5790.90.

[handling_file.py](https://github.com/fiveheartone/python_project_Xinyi/blob/master/movie_recommend/src/handling_file.py): to handle the scraped BollywoodMovieRank.csv and fuzzy match the genres and numbers which are taken from the users. Click Recommend titles and the type situations are saved in [project_output.pdf](https://github.com/fiveheartone/python_project_Xinyi/blob/master/project_output.pdf).

## Resources
[BollywoodMovieDetail.csv](https://github.com/calci/bollywood-movie-dataset/blob/master/BollywoodMovieDetail.csv)
[Flask Document](https://flask.palletsprojects.com/en/2.3.x/)
[Selenium with Python](https://selenium-python.readthedocs.io/index.html)
[HTML Tutorial](https://www.w3schools.com/html/)
