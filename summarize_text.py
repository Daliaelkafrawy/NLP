import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist


def summarize_text(text, num_sentences=2):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words("english"))
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Calculate word frequencies
    freq_dist = FreqDist(words)

    # Assign scores to sentences based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                if len(sentence.split(' ')) < 30: # Avoid very long sentences
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = freq_dist[word]
                    else:
                        sentence_scores[sentence] += freq_dist[word]

    # Get the top N sentences based on scores
    top_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)[:num_sentences]

    # Construct the summary
    summary = ""
    for sentence, _ in top_sentences:
        summary += sentence + " "

    return summary


# Example usage
text = "When mice are kept at high population densities, their behaviour changes in a number of ways. Aggressive activity within populations of mice rises as density increases. Cannibalism of young also goes up, and so does aberrant sexual activity. Communal nesting, frequent in natural mouse populations, increases abnormally. In one example, 58 mice one to three days old (from several litters) were found in one nest, most unusual communal living. None survived because most of the mothers deserted them immediately after birth."

summary = summarize_text(text)

print("Summary:")

print(summary)