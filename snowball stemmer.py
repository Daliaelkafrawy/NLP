import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize

# Ensure you have the required datasets
nltk.download('punkt')

# Initialize the Snowball Stemmer for English
snowball = SnowballStemmer(language='english')

# Sample text
text = "The quick brown foxes were jumping over the lazy dogs."

# Tokenize the text
tokens = word_tokenize(text)

# Perform stemming
stemmed_tokens = [snowball.stem(token) for token in tokens]

# Output the results
print("Original Tokens:", tokens)
print("Stemmed Tokens:", stemmed_tokens)
