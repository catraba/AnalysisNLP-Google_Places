import json
import re
from datetime import datetime, timedelta

def Analyzer(link):
    with open(link) as file:
        data = json.load(file)

    result = data['result']

    today = datetime.today()

    # Media de puntuaciones
    media = result['rating']


    # Cantidad de puntuaciones por nota
    reviews = result['reviews']
    all_scores = [i['rating'] for i in reviews] 
    count_scores = {i: all_scores.count(i) for i in range(1, 6)}

    
    # Puntuación media por año
    rev_by_year = {}

    for review in reviews:
        time = review['relative_time_description']

        
        if 'days' in time:
            pattern = re.search('[0-9]', time)
            prox = today - timedelta(days=int(pattern[0]))

            if prox.year in rev_by_year:
                rev_by_year[prox.year].append(review['rating'])

            else:
                rev_by_year[prox.year] = [review['rating']]

        
        elif 'weeks' in time:
            pattern = re.search('[0-9]', time)
            prox = today - timedelta(weeks=int(pattern[0]))

            if prox.year in rev_by_year:
                rev_by_year[prox.year].append(review['rating'])

            else:
                rev_by_year[prox.year] = [review['rating']]

        
        
        elif 'months' in time:
            pattern = re.search('[0-9]', time)
            prox = today - timedelta(weeks=int(pattern[0]) * 4)

            if prox.year in rev_by_year:
                rev_by_year[prox.year].append(review['rating'])

            else:
                rev_by_year[prox.year] = [review['rating']]


        elif 'years' in time:
            pattern = re.search('[0-9]', time)
            prox = today - timedelta(weeks=int(pattern[0]) * 52)


            if prox.year in rev_by_year:
                rev_by_year[prox.year].append(review['rating'])

            else:
                rev_by_year[prox.year] = [review['rating']]


    for year in rev_by_year:
        media = sum(rev_by_year[year]) / len(rev_by_year[year])

        rev_by_year[year] = round(media, 2)


    js = {'media': media,
          'cantidad_puntuaciones': count_scores,
          'reviews_by_year': rev_by_year}

    return js