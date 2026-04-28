import re

def normalize_title(title):
    title = title.lower()
    title = re.sub(r"\(.*?\)", "", title) #remove text in parentheses
    title = re.sub(r"feat\.|featuring", "", title) #remove 'feat.' or 'featuring' -> can look into it later
    title = re.sub(r'[^a-z0-9\s]', '', title) #delete punctuation
    title = re.sub(r'\s+', ' ', title).strip() #remove extra spaces
    return title