# Facebook-Sentiment-Analysis
```
<p>Facebook's Post Sentiment Analysis based on comments of that particular post.</p> 
```
```
<p>Requirements:</p>
```

Hardware: Ram 8Gb+
Free Disk Space: 10Mb
Software: Python 3.6 and above.

```
<p>Dependencies:</p>
```

Flask 0.12.2
Requests 2.18.4
Nltk 3.2.5
Random
Pickle
Statistics 1.0.3.5
Sklearn
String
Wordcloud 1.3.1
Matplotlib 2.1.1
Sumy 0.7.0

```
<p>Process:</p>
```

1: Download the project and install all the mentioned requirements and dependencies.
2: Having install all the above, from your ide run training_model.py
3: After successfully execution of training_model.py, run front_end.py
4: On successful exection of front_end.py, local url would be given, go to that url through
your browser.
5: Search Box on Index page appears, in it paste the url of any facebook post then press
enter.
6: You’ll be directed to result page, where result of the sentiment analysis of the given fb
post comments will be shown.
7: Apart from the positive negative sentiment tally, summary of each sentiment along with
word cloud is also shown.
8: Cool Enjoy.

```
<p>Work Flow:</p>
```

1: File training_model.py trains the classifier on classified movie reviews training data, to be
used in classification of new request.
2: front_end.py provides the user end interface based on flask.
3: fetch_comments.py will be called from front_end.py on users request, this will fetch the
comments from fb using graph api for the given post url.
4: model_back.py will be called after all the comments being fetched, it will classify the new
requests i.e. , the comments fetched from fb.
5: model_result.py will be called from front_end.py it will call the model_back.py to classify
each comment from scrape_data.txt based on relevant features from relevant_feature.py
6: Results generated in model_result.py will be sent to front_end.py from where it can be
displayed on the user end, taking the help of wordc.py, sum.py and sumn.py in form of word
cloud registration, positive and negative summary generation respectively.
