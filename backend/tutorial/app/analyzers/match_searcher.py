from spacy.matcher import Matcher


def matchSearcher(nlp, data, word):
    matcher = Matcher(nlp.vocab)

    rates = []
    adjetives = []

    pattern = [{'LOWER': word}]
    matcher.add('matchSearcher', [pattern])

    reviews = data['reviews']

    for review in reviews:
        text = review['text']
        rate = review['rating']

        doc = nlp(text)
        matches = matcher(doc)

        for match_id, start, end in matches:
            rates.append(rate)

            adjetive = doc[start + 1]

            if adjetive.pos_ == 'ADJ':
                adjetives.append(adjetive.text)

    media = round(sum(rates) / len(rates), 2)
    count_words = {}

    for word in adjetives:
        count_words[word] = adjetives.count(word)

    js = {'media': media,
          'count_words': count_words}

    return js