import nltk
import string
import collections
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

postags = ['NN', 'NNS', 'NNP', 'NNPS']

class relevant(object):

    def find_relevant(self):

        l = []
        for line in open("scrape_data.txt", "r", encoding="utf8"):
            # print(line)
            x = ""
            tokens = word_tokenize(line)
            words_postags = nltk.pos_tag(tokens)
            table = str.maketrans('', '', string.punctuation)
            tokens = [w.translate(table) for w in tokens]
            tokens = [word for word in tokens if word.isalpha()]

            stop_words = set(stopwords.words('english'))
            tokens = [w for w in tokens if not w in stop_words]
            tokens = [word.lower() for word in tokens if len(word) > 1]
            # print(tokens)
            for word_postag in words_postags:
                if word_postag[0] in tokens:
                    l.append(word_postag)
                # print(word_postag)
                if word_postag[0] in tokens and word_postag[1] in postags:
                    l.append(word_postag)

        tags = []
        words = [] 
        # fds = []
        # fdsw = []
        for i in l:
            tags.append(i[1])
            words.append(i[0])
            # print(fd)
        # print(fd)
        #fds = nltk.FreqDist(fd) #freq dist of postags
        # fds.tabulate()

        #fdsw = nltk.FreqDist(fdw) #freq dist of words
        # fdsw.tabulate()

        most_common = collections.Counter(words).most_common() #most common words along with its frequecy
        # print(most_common)

        freq_sum_word = 0 # Frequency of particular word-> sum
        total_num_words = 0 # sum of num of words till particular frequency sum
        freq_sum_word_chk = 0 # Frequency of particular word-> sum

        for freq_dist in most_common:
            freq_sum_word =freq_sum_word +freq_dist[1]
            # print(k[0])
        # print(s)
        for freq_dist in most_common:
            total_num_words =total_num_words + 1
            freq_sum_word_chk = freq_sum_word_chk + freq_dist[1]
            if freq_sum_word_chk > (freq_sum_word /3):
                break
        # print(s1)
        most_common_final=collections.Counter(words).most_common(total_num_words)

        return most_common_final
