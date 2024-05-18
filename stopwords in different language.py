import nltk
from nltk.corpus import stopwords

def get_stopwords(language):
    nltk.download('stopwords')
    try:
        return stopwords.words(language)
    except:
        return []

if __name__ == "__main__":
    languages = ['english', 'spanish', 'french', 'german', 'italian']
    
    for lang in languages:
        lang_stopwords = get_stopwords(lang)
        if lang_stopwords:
            print(f"Common stopwords in {lang}:")
            print(lang_stopwords)
            print("\n")
        else:
            print(f"Stopwords for {lang} are not available.\n")
