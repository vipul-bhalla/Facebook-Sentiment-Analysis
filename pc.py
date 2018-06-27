from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import string
pl=[]
nl=[]

class pos_neg_key:

    def ext(self):

        for line in open("po.txt", "r", encoding="utf8"):
            # print(line)
            # line=" My daughter's want to see you so badly so I signed up for your verified fan and got the code and I wanted to purchase the lowest priced tickets but within a matter of a short time those were apparently sold out, now in am trying with every other person and within seconds the cheapest seats are gone.  I cannot afford even the second lowest price so I think this is ridiculous and you are just money hungry.  We went to another popular concert earlier this year and the tickets were not this expensive.  Now I have Donnell my daughter's that they cannot go and all because you can't make your tickets less expensive.  Absolutely ridiculous!"
            sentence = ""
            tokenizer = RegexpTokenizer(r'\w+')
            tokens = tokenizer.tokenize(line)
            table = str.maketrans('', '', string.punctuation)
            tokens = [w.translate(table) for w in tokens]
            tokens = [word for word in tokens if word.isalpha()]
            stop_words = set(stopwords.words('english'))
            tokens = [w for w in tokens if not w in stop_words]
            tokens = [word.lower() for word in tokens if len(word) > 1]
            for token in tokens:
                sentence = sentence + " " + token
            pl.append(sentence)

        with open('po_extract.txt', 'wb+') as f:
            for l in pl:
                f.write(l.encode("utf-8") + "".encode("ascii"))

        for line in open("ne.txt", "r", encoding="utf8"):
            # print(line)
            # line=" My daughter's want to see you so badly so I signed up for your verified fan and got the code and I wanted to purchase the lowest priced tickets but within a matter of a short time those were apparently sold out, now in am trying with every other person and within seconds the cheapest seats are gone.  I cannot afford even the second lowest price so I think this is ridiculous and you are just money hungry.  We went to another popular concert earlier this year and the tickets were not this expensive.  Now I have Donnell my daughter's that they cannot go and all because you can't make your tickets less expensive.  Absolutely ridiculous!"
            sentence = ""
            tokenizer = RegexpTokenizer(r'\w+')
            tokens = tokenizer.tokenize(line)
            table = str.maketrans('', '', string.punctuation)
            tokens = [w.translate(table) for w in tokens]
            tokens = [word for word in tokens if word.isalpha()]
            stop_words = set(stopwords.words('english'))
            tokens = [w for w in tokens if not w in stop_words]
            tokens = [word.lower() for word in tokens if len(word) > 1]
            for token in tokens:
                sentence = sentence + " " + token
            nl.append(sentence)

        with open('ne_extract.txt', 'wb+') as f:
            for l in nl:
                f.write(l.encode("utf-8") + "".encode("ascii"))
