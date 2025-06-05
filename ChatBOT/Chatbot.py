import nltk
from nltk.stem import WordNetLemmatizer
import pandas
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from dotenv import dotenv_values
from colorama import Fore

from QueryModifier import PreProcess
from Interactions.SpeechToText import STT
from Interactions.TextToSpeech import TTS

chats_file_path = r"ChatBOT\chats.json"
processed_data_file_path = r"ChatBOT\processed_data.json"
model_file_path = r"ChatBOT\tfidf_model.pkl"

nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

env_vars = dotenv_values(".evn")
MarkOne = env_vars.get("MarkedName")
Username = env_vars.get("Username")

# LOAD DATA
try:
    with open(chats_file_path, "r") as f:
        data = json.load(f)
    
except (FileNotFoundError, json.JSONDecodeError):
    data = []
    
data_frame = pandas.DataFrame(data)

# HANDLE EMPTY DATA
if data_frame.empty:
    data_frame = pandas.DataFrame(columns=["input", "output"])
    
data_frame["processed_input"] = data_frame["input"].apply(PreProcess)
data_frame["processed_output"] = data_frame["output"].apply(PreProcess)

# SAVE PROCESSED DATA
data_frame.to_json(processed_data_file_path, indent=4)

# MODEL
vectorizer = TfidfVectorizer()

if not data_frame.empty:
    X = vectorizer.fit_transform(data_frame["processed_input"])
else:
    X = None
    
def Get_Response(user_input):
    global X, vectorizer, data_frame
    
    processed_input = PreProcess(user_input)
    
    if X is None or X.shape[0] == 0:
        print(Fore.RED + "No data to compare with yet.")
        return
    
    input_vector = vectorizer.transform([processed_input])
    similarities = cosine_similarity(input_vector, X)
    best_score = similarities.max()
    best_match_idx = similarities.argmax()
    
    if best_score > 0.6:
        response = data_frame.iloc[best_match_idx]["output"]
        TTS(response)
        
    # IF THERE IS NO REPLY FOR THE QUERY
    else:
        response = "I don't have the answer to this query at this moment."
        print(Fore.RED + response)
        TTS(response)
        
        # IT WILL ASK FOR AN SUGGESTION FOR THAT QUERY
        TTS("Do you wanna suggest any?")
        
        want = STT()
        want = want.lower().strip()
        
        if want in ["yes", "sure", "of course"]:
            print(Fore.GREEN + "Recording your suggestion: ")
            suggested_answer = STT()
            
            pre_words = [
                "well you can say",
                "you should say",
                "the answer can be",
                "the answer is"
            ]
            
            for pre_w in pre_words:
                user_answer = suggested_answer.replace(pre_w, "")
            
            # APPEND TO ORIGINAL DATASET
            new_entry = {"input": user_input, "output": user_answer}
            data.append(new_entry)
            
            # SAVE TO FILE
            with open(chats_file_path, "w") as f:
                json.dump(data, f, indent=4)
                
            # UPDATE THE MODEL
            data_frame.loc[len(data_frame)] = [user_input, user_answer, PreProcess(user_input), PreProcess(user_answer)]
            X = vectorizer.fit_transform(data_frame["processed_input"])
                
            feedback = "Thanks for your feedback."
            print(Fore.BLUE + feedback)
            TTS(feedback)
        
        else:
            print("Thanks for your feedback.")
            TTS("Thanks for your feedback.")
            
    return data_frame.iloc[best_match_idx]["output"]

# SAVE MODEL
with open(model_file_path, "wb") as f:
    pickle.dump(vectorizer, f)
    
    
# TESTING
def main():
    while True:
        usr_in = STT()
        print(Fore.GREEN + "Me: ", usr_in)
        
        if usr_in.lower() == "exit":
            exit()
            
        res = Get_Response(user_input=usr_in)
        
        if res:
            print(Fore.BLUE + "Response: ", res)