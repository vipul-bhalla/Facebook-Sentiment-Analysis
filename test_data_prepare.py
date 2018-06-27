import pickle
from nltk.tokenize import word_tokenize
import random

class test_data:

    def data(self):

        documents_f = open("test_data_prepare/documents.pickle", "rb")
        documents = pickle.load(documents_f)
        documents_f.close()

        word_features5k_f = open("test_data_prepare/word_features5k.pickle", "rb")
        word_features = pickle.load(word_features5k_f)
        word_features5k_f.close()

        def find_features(document):
            words = word_tokenize(document)
            features = {}
            for w in word_features:
                features[w] = (w in words)

            return features

        featuresets = [(find_features(rev), category) for (rev, category) in documents]

        random.shuffle(featuresets)

        return(featuresets)

