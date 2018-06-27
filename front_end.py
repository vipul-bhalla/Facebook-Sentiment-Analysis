from flask import Flask, redirect, url_for
from flask import request
import requests
from flask import render_template
from fetch_comments import fetchComments
from model_result import modelResult
from preview import preview
from pc import pos_neg_key
from wordc import wrdcld
from sum import pos_sum
from sumn import neg_sum
ps = pos_sum()
ns = neg_sum()

wc=wrdcld()
pnkey=pos_neg_key()
l=['photos','videos','posts']
fc=fetchComments()
mr=modelResult()
ep=preview()

class FlaskIgnite:

    app = Flask(__name__)

    @app.route('/')
    def my_form():
        return render_template("index.html")

    @app.route('/result', methods=['POST'])
    def result():
        # p={}
        text = request.form['text']
        query = text.split("/")
        for i in query:
            if i in l:
                initial = text.split(i+"/")
                slash=initial[1].split("/")
                initial[1]=slash[0]
                if i!="photos":
                    postid=initial[1]
                    print(postid)
                else:
                    postid=query[6]
                    print(postid)
                z = initial[0] + i
                break

        url = 'https://graph.facebook.com/' + query[
            3] + '?&access_token=xxxxxxxxx'
        # print(url)
        r = requests.get(url)
        dict = r.json()

        pageid = dict['id']
        print(pageid)
        #-----------------------------------

        fc.extract(pageid, postid)
        x = mr.output()
        y = ep.extractpreview(pageid, postid)


        # print(ps.psum())
        # print(ns.nsum())

        pnkey.ext()

        return render_template("try.html", tfr=x, pre=y, psummary=ps.psum(), nsummary=ns.nsum())

    @app.route("/pcloud", methods=['POST'])
    def pos_cloud():
        pc = wc.gen_pos_cloud()

        return redirect(url_for('result'),code=304)

    @app.route("/ncloud", methods=['POST'])
    def neg_cloud():
        nc = wc.gen_neg_cloud()

        return redirect(url_for('result'), code=304)


    if __name__ == '__main__':
        app.run()


Ignite=FlaskIgnite()
Ignite.my_form()
Ignite.result()

