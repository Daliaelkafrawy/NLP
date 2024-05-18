import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_stopwords(text):
    # Download stopwords if not already downloaded
    nltk.download('stopwords')
    nltk.download('punkt')

    # Tokenize the text
    words = word_tokenize(text)

    # Get the list of English stopwords
    stop_words = set(stopwords.words('english'))

    # Remove stopwords from the text
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Join the filtered words back into a single string
    filtered_text = ' '.join(filtered_words)

    return filtered_text

def main():
    # Ask user to input text
    text = input("Enter the text: ")

    # Remove stopwords from the text
    filtered_text = remove_stopwords(text)

    # Print the filtered text
    print("\nFiltered Text:")
    print(filtered_text)

if __name__ == "__main__":
    main()

##NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project    