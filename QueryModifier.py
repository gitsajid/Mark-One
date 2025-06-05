from Interactions.SpeechToText import STT

import query_library
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def SingleCommandModification(query, commands):
    for cmd in commands:
        query = query.replace(cmd, "")
        
    return query.strip()

def QueryFilter(query):
    filtered_query = query
    
    if any(word in query_library.wh_questions for word in query.split()):
        filtered_query = query + "?"
        
    elif any(query.startswith(verb) for verb in query_library.verbs):
        filtered_query = query + "?"
        
    return filtered_query.strip()

def PreProcess(query):
    query = re.sub(r"[^\w\s]", "", query.lower())
    tokens = word_tokenize(query)
    
    return " ".join([lemmatizer.lemmatize(token) for token in tokens])



if __name__ == "__main__":
    q = STT()
    p = QueryFilter(q)
    print(p)