import spacy

#English language model for SpaCy
nlp = spacy.load("en_core_web_sm")

def is_time_sensitive(text):
    
    #analyze the text using SpaCy
    doc = nlp(text)
    
    #define a list of keywords that might indicate time-sensitive information
    current_or_recent_keywords = [
        "now", "current", "today", "recent", "latest", "just", "happening",
        "breaking", "new", "up-to-date", "update", "moment", "currently"
    ]

    #iterate through tokens in the analyzed text
    for token in doc:
        #check if the token is one of the keywords
        if token.lower_ in current_or_recent_keywords:
            #check if the token is the subject or the object of a verb
            if "subj" in token.dep_ or "obj" in token.dep_:
                return True
        
        #check if the token is a DATE entity
        if token.ent_type_ == "DATE":
            try:
                #convert the token text to an integer
                year = int(token.text)
                #consider it time-sensitive if the year > 2021
                if year > 2021:
                    return True
            except ValueError:
                #if the token text cannot be converted to an integer, continue to the next token
                pass

    #return False if no time-sensitive information is found
    return False
