import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')  

def tokenize_words(text):
    words = word_tokenize(text)
    print("Tokenized words:")
    for word in words:
        print(word)

def tokenize_sentences(text):
    sentences = sent_tokenize(text)
    print("Tokenized sentences:")
    for sentence in sentences:
        print(sentence)

def split_text(text):
    print("Output using split function:")
    print(text.split())

def main():
    # user_text = input("Enter some text: ")
    user_text = "NLTK is a leading platform for building Python programs to work with human language data. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project."
    choice = input("Choose one of the following options:\n"
                   "1. Print tokenized words\n"
                   "2. Print tokenized sentences\n"
                   "3. Print output using split function\n"
                   "Enter your choice (1/2/3): ")

    if choice == '1':
        tokenize_words(user_text)
    elif choice == '2':
        tokenize_sentences(user_text)
    elif choice == '3':
        split_text(user_text)
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
main()