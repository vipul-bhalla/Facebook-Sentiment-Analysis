from model_back import sentiment
from relevant_features import relevant
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import string
result_dict={}
result_list=[]

relevant_noun=relevant()

class modelResult:
    def output(self):
        positive = 0
        negative = 0
        total = 0
        c = 0
        poslines=[]
        neglines=[]

        representatives = relevant_noun.find_relevant()
        noun_sentiments = {}
        stop_words = set(stopwords.words('english'))
        stop_words.remove('no')
        stop_words.remove('nor')
        stop_words.remove('not')
        for nouns in representatives:
            l = []
            for line in open("scrape_data.txt", "r", encoding="utf8"):
                # print(line)
                sentence = ""
                tokenizer = RegexpTokenizer(r'\w+')
                tokens = tokenizer.tokenize(line)
                tokens = [word.lower() for word in tokens if len(word) > 1]
                table = str.maketrans('', '', string.punctuation)
                tokens = [w.translate(table) for w in tokens]
                tokens = [word for word in tokens if word.isalpha()]
                # stop_words = set(stopwords.words('english'))
                tokens = [w for w in tokens if not w in stop_words]
                # tokens = [word.lower() for word in tokens if len(word) > 1]
                # print(tokens)
                if nouns[0] in tokens:
                    # print(nouns[0])
                    for token in tokens:
                        sentence = sentence + " " + token
                    # print(sentence)
                    # print(x)
                    qsent=sentiment(sentence)
                    # print(qsent)

                    # print(qsent[0])
                    if qsent[0]=="pos":
                        if line not in poslines:
                            poslines.append(line)
                    if qsent[0]=="neg":
                        if line not in neglines:
                            neglines.append(line)
                        # with open('ne.txt', 'ab+') as f:
                        #     f.write(line.encode("utf-8") + "".encode("ascii"))
                    l.append(qsent)
            noun_sentiments[nouns[0]] = l
        # print(noun_sentiments)
        for key, values in noun_sentiments.items():
            key_list=[]
            pos = 0
            neg = 0
            t = len(values)
            if t > 0:
                # print(key)
                for value in values:
                    if value[0] == 'pos':
                        pos = pos + 1
                    if value[0] == 'neg':
                        neg = neg + 1
                positive = positive + pos
                negative = negative + neg
                total = total + t
                print("Positive %", (pos / t) * 100)
                print("Negative %", (neg / t) * 100)
                print("------------------------")
                key_list.append((pos/t)*100)
                key_list.append((neg/t)*100)
                print("####################")
                print(key_list)
            if c<5:
                result_dict[key]=key_list
            c=c+1
        result_list.append(result_dict)
        print("**************************")
        print("Overall relevant sentiment")
        print("Positive %", (positive / total) * 100)
        print("Negative %", (negative / total) * 100)
        # print(poslines)
        # print(neglines)

        with open('po.txt', 'wb+') as f:
            for pl in poslines:
                f.write(pl.encode("utf-8") + "".encode("ascii"))

        with open('ne.txt', 'wb+') as f:
            for nl in neglines:
                f.write(nl.encode("utf-8") + "".encode("ascii"))
        temp=[]
        temp.append((positive/total)*100)
        temp.append((negative/total)*100)
        result_dict["Overall"]=temp
        return result_dict

# mr=modelResult()
# print(mr.output())

