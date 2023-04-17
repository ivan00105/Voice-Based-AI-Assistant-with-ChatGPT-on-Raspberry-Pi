import spacy

nlp = spacy.load("en_core_web_sm")

def is_time_sensitive(text):
    doc = nlp(text)
    
    current_or_recent_keywords = [
        "now", "current", "today", "recent", "latest", "just", "happening",
        "breaking", "new", "up-to-date", "update", "moment", "currently"
    ]

    for token in doc:
        if token.lower_ in current_or_recent_keywords:
            if "subj" in token.dep_ or "obj" in token.dep_:
                return True
        
        if token.ent_type_ == "DATE":
            try:
                year = int(token.text)
                if year > 2021:
                    return True
            except ValueError:
                pass

    return False
