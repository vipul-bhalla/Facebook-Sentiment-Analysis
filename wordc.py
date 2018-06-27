from wordcloud import WordCloud
import matplotlib.pyplot as plt

class wrdcld:
    def gen_neg_cloud(self):

        textn = open("ne_extract.txt", "r", encoding="utf8").read()
        if textn:
            wordcloudn = WordCloud().generate(textn)
            plt.imshow(wordcloudn, interpolation='bilinear')
            plt.axis("off")
            return(plt.show())
        else:
            return 0

    def gen_pos_cloud(self):

        textp = open("po_extract.txt", "r", encoding="utf8").read()
        if textp:
            wordcloudp = WordCloud().generate(textp)
            plt.imshow(wordcloudp, interpolation='bilinear')
            plt.axis("off")
            return(plt.show())
        else:
            return 0

