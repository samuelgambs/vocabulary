import re
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer


class NLP():

    primary_text = None
    second_text = None

    def __init__(self, primary_text, second_text):
        self.primary_text = primary_text
        self.second_text = second_text

    def remove_stopwords(self, text):
        stops = set(stopwords.words("portuguese"))
        words = re.split('\s|(?<!\d)[,.-](?!\d)', text.lower())
        words = ' '.join([w for w in words if not w in stops])
        return words

    def convert_text_to_list_and_remove_stopwords(self):
        text_list = []
        text_list.append(self.remove_stopwords(self.primary_text))
        text_list.append(self.remove_stopwords(self.second_text))
        return text_list

    def set_frequecy_words(self, list_text, gram):

        result = {}
        count_vec = CountVectorizer(ngram_range=(gram, gram),
                                    stop_words="english")

        count_data = count_vec.fit_transform(list_text)
        cv_dataframe = pd.DataFrame(
            count_data.toarray(), columns=count_vec.get_feature_names())

        result["vector_isolade"] = cv_dataframe
        result["vocabulary_isolade"] = count_vec.get_feature_names()

        return result

    def process(self):

        list_text = self.convert_text_to_list_and_remove_stopwords()
        text_isolated = self.set_frequecy_words(list_text, 1)
        text_two_sequence = self.set_frequecy_words(list_text, 2)

        return text_isolated, text_two_sequence
