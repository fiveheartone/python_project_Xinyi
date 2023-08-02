"""
scraping movie rating and viewers number from link: https://www.imdb.com/title/{id}/ratings/?ref_=tt_ov_rt
saving all(movie id, score(movie rating) and viewers(voted number)) as BollywoodMovieRank.csv
"""
import csv
import pandas as pd

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_score():
    options = Options()
    # in oder to use headless status
    # options.add_argument("--headless")
    # options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
    driver = webdriver.Chrome(service=Service(r'movie_recommend\src\chromedriver.exe'), options=options)
    movie_detail_df = pd.read_csv(r'movie_recommend\files\BollywoodMovieDetail.csv').dropna(subset=['imdbId', 'title', 'genre'])
    scrape_details = []
    for per_index, per_row in movie_detail_df.iterrows():
        id = str(per_row['imdbId']).strip()
        title = str(per_row['title']).strip()
        if str(per_row['releaseYear']).strip() != 'nan' and str(per_row['releaseYear']).strip() != '':
            title = title + "(" + str(per_row['releaseYear']).strip() + ")"
        driver.get(f"https://www.imdb.com/title/{id}/ratings/?ref_=tt_ov_rt")
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@data-testid="rating-button__aggregate-rating__score"]')))
            try:
                score_whole = driver.find_element(By.XPATH, '//div[@data-testid="rating-button__aggregate-rating__score"]').text
                score = score_whole.replace('/10', '').strip()
            except Exception:
                score = ''
            try:
                rank_num = driver.find_element(By.XPATH, '//div[@data-testid="rating-button__aggregate-rating__score"]/following-sibling::div').text.strip()
            except Exception:
                rank_num = ''
        except TimeoutException:
            score = "T/A"
            rank_num = "T/A"
        except NoSuchElementException:
            score = "N/A"
            rank_num = "N/A"
        scrape_details.append([id, title, str(per_row['genre']).strip(), score, rank_num])

    with open(r'movie_recommend\files\BollywoodMovieRank.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['imdbId', 'title', 'genre', 'score', 'viewers'])
        writer.writerows(scrape_details)
