import json

def textCleaner(nlp, link):
    # Actualizamos algunas palabras al nlp
    stop_worlds = ['a', 'o']

    for letra in stop_worlds:
        nlp.vocab[letra].is_stop = True

    with open(link, encoding='utf-8') as file:
        data = json.load(file)

    result = data['result']

    for review in result['reviews']:
        # Eliminamos tildes
        text = review['text'].lower().translate(str.maketrans('áéíóú', 'aeiou'))
        
        doc = nlp(text)

        complete = ''
        
        for token in doc:
            if not token.is_punct and not token.is_stop:
                complete = complete + token.lemma_ + ' '

        review['text'] = complete

    return result