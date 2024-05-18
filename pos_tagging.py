import nltk
nltk.download('universal_tagset')

def pos_tagging(input_text):
    # Tokenize the input text
    words = nltk.word_tokenize(input_text)
    
    # Apply part-of-speech tagging using two different tagsets
    pos_tags_universal = nltk.pos_tag(words, tagset='universal')
    pos_tags_default = nltk.pos_tag(words)

    return pos_tags_universal, pos_tags_default

def main():
    input_text = input("Enter a sentence: ")

    pos_tags_universal, pos_tags_default = pos_tagging(input_text)

    print("\nPart-of-speech tagging with Universal Tagset:")
    print(pos_tags_universal)

    print("\nPart-of-speech tagging with Default Tagset:")
    print(pos_tags_default)

if __name__ == "__main__":
    # Download NLTK resources if not already downloaded
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    
    main()

#NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project    