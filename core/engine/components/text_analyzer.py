from pyarabic.araby import tokenize, strip_tashkeel
from arabicstopwords.arabicstopwords import is_stop
import qalsadi.lemmatizer

from tashaphyne import stemming

stem = stemming.ArabicLightStemmer()
lemmer = qalsadi.lemmatizer.Lemmatizer()


def remove_tashkeel(text):
    return strip_tashkeel(text)


def tokenize_text(text):
    return tokenize(text)


def lemmatize_text(text):
    return lemmer.lemmatize_text(text)


def remove_stop_word(text: list):
    non_stop_words = []
    for word in text:
        if not is_stop(word):
            non_stop_words.append(word)
    return non_stop_words


def process_text_lemm(text):
    processed_text = remove_tashkeel(text)
    processed_text = lemmatize_text(processed_text)
    # processed_text = tokenize_text(processed_text)
    # processed_text = remove_stop_word(processed_text)
    return ",".join(processed_text)


def process_text_stemm(text):
    processed_text = remove_tashkeel(text)

    tokens = []
    for token in stem.tokenize(processed_text):
        tokens.append(stem.light_stem(token))

    return " ".join(tokens)



class TextAnalyser:
    def __init__(self):
        self.stem = stemming.ArabicLightStemmer()
        self.lemmer = qalsadi.lemmatizer.Lemmatizer()

    def remove_tashkeel(self,text):
        return strip_tashkeel(text)

    def tokenize_text(self,text):
        return tokenize(text)

    def lemmatize_text(self, text):
        return self.lemmer.lemmatize_text(text)

    def remove_stop_word(self, text: list):
        non_stop_words = []
        for word in text:
            if not is_stop(word):
                non_stop_words.append(word)
        return non_stop_words

    def process_text_lemm(self, text):
        processed_text = self.remove_tashkeel(text)
        processed_text = self.lemmatize_text(processed_text)
        # processed_text = tokenize_text(processed_text)
        # processed_text = remove_stop_word(processed_text)
        return ",".join(processed_text)

    def process_text_stemm(self, text):
        processed_text = self.remove_tashkeel(text)

        tokens = []
        for token in self.stem.tokenize(processed_text):
            tokens.append(stem.light_stem(token))

        return " ".join(tokens)

