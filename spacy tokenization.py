import spacy

def tokenize_sentences(text, model_name='fr_core_news_sm'):  # Use the full model name
    # Load SpaCy model
    nlp = spacy.load(model_name)

    # Process the text
    doc = nlp(text)

    # Tokenize the text into sentences
    sentences = [sent.text for sent in doc.sents]

    return sentences

def main():
    # Ask user to input text
    text = input("Enter the text to tokenize: ")

    # Ask user for model name
    model_name = input("Enter the model name (e.g., 'fr_core_news_sm' for French, 'de_core_news_sm' for German): ")

    # Tokenize the text into sentences using SpaCy
    sentences = tokenize_sentences(text, model_name)

    # Print the tokenized sentences
    print("\nTokenized Sentences:")
    for i, sent in enumerate(sentences, 1):
        print(f"Sentence {i}: {sent}")

if __name__ == "__main__":
    main()


#NLTK est une plateforme leader pour construire des programmes Python permettant de travailler avec des données de langage humain. NLTK est disponible pour Windows, Mac OS X et Linux. Le meilleur de tout, NLTK est un projet gratuit, open source et communautaire.