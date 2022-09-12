import string
import nltk.corpus
from lxml import etree
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag


def extract_terms(text):
    words = word_tokenize(text.lower())
    lemmatizer = [WordNetLemmatizer().lemmatize(word) for word in words]
    filtered = [word for word in lemmatizer if
                word not in list(string.punctuation) and nltk.corpus.stopwords.words('english')]
    lemmatized = [pos_tag([word])[0][0] for word in filtered if pos_tag([word])[0][1] == 'NN']
    nouns = [(lemmatized.count(i), i) for i in set(lemmatized)]
    return [i[1] for i in sorted(nouns, reverse=True)[:5]]


for e in etree.parse('news.xml').getroot()[0]:
    title, article = e
    print(title.text)
    print('key terms:', *extract_terms(article.text), sep=' ')
