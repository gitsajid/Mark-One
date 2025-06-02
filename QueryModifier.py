from Interactions.SpeechToText import STT
from Interactions.TextToSpeech import TTS
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
    for word in query.split(" "):
        if word in query_library.questions:
            filtered_query = "Asking" + ", " + query + "?"
        else:
            filtered_query = query
            
    return filtered_query

def PreProcess(query):
    query = re.sub(r"[^\w\s]", "", query.lower())
    tokens = word_tokenize(query)
    
    return " ".join([lemmatizer.lemmatize(token) for token in tokens])



if __name__ == "__main__":
    q = STT()
    p = QueryFilter(q)
    print(p)