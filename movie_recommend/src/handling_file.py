"""
handling BollywoodMovieRank.csv, fuzzy match the category(genre), then order the movies based on viewers or score
"""
import pandas as pd
import re
from fuzzywuzzy import process


def handle_file(number, category):
    movie_rank = pd.read_csv(r'movie_recommend\files\BollywoodMovieRank.csv')
    movie_rank = movie_rank.loc[(movie_rank["viewers"] != 'T/A') & (movie_rank["viewers"] != 'N/A')]
    movie_rank["viewers"] = movie_rank["viewers"].apply(lambda x: int(float(re.findall(r'[0-9.]*', x)[0])*1000) if "K" in x or "k" in x else int(x))
    movie_genre = movie_rank["genre"].str.split('|', expand=True).stack().reset_index(level=1, drop=True).rename('genres')
    movie_rank_genres = movie_rank.drop("genre", axis=1).join(movie_genre)
    movie_rank_genres = movie_rank_genres[["title", "score", "viewers", "genres"]]
    movie_rank_genres["genres"] = movie_rank_genres["genres"].apply(lambda x: str(x).strip())
    genres_list = set(movie_rank_genres['genres'].to_list())
    extracted_genre = process.extractBests(str(category).strip(), list(genres_list), score_cutoff=80)

    if len(extracted_genre) == 0:
        result = f"Sorry! We didn't find the category! \nTrying to input: \n{','.join(list(genres_list))}"
    elif len(extracted_genre) == 1:
        output_movie_rank_genres = movie_rank_genres.loc[movie_rank_genres['genres'] == extracted_genre[0][0]]
        output_score = output_movie_rank_genres.sort_values(by=['score', 'viewers'], ascending=False)[["title","score","viewers"]]
        output_viewer = output_movie_rank_genres.sort_values(by=['viewers', 'score'], ascending=False)[["title","viewers", "score"]]
        if len(output_movie_rank_genres) >= number:
            result = f"For {extracted_genre[0][0]}, recommend the best movies based on IMDB:\nBy Voting:\n" \
                     f"{output_score[:number].to_html(index=False,  justify='center')} By Watching Viewers: \n{output_viewer[:number].to_html(index=False,  justify='center')}"
        else:
            result = f"For {extracted_genre[0][0]}, recommend the best movies based on IMDB:\nBy Voting:{output_score.to_html(index=False, justify='center')}" \
                     f"By Watching Viewers: {output_viewer.to_html(index=False, justify='center')}"
    else:
        extracted_genre_list = [per_extracted_genre[0] for per_extracted_genre in extracted_genre]
        result = f"Which category are you trying to search? {','.join(extracted_genre_list)}?"

    return result
