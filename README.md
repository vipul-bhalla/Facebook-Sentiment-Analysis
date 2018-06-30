# Facebook-Sentiment-Analysis
```
Facebook's Post Sentiment Analysis based on comments of that particular post. 
```
```
Requirements:
```

1. Hardware: Ram 8 Gb+
2. Free Disk Space: 10 Mb
3. Software: Python 3.6 and above.

```
Dependencies:
```

1. Flask 0.12.2
2. Requests 2.18.4
3. Nltk 3.2.5
4. Random
5. Pickle
6. Statistics 1.0.3.5
7. Sklearn
8. String
9. Wordcloud 1.3.1
10. Matplotlib 2.1.1
11. Sumy 0.7.0

```
Process:
```

1. Download the project and install all the mentioned requirements and dependencies.
2. Having install all the above, from your ide run training_model.py
3. After successfully execution of training_model.py, run front_end.py
4. On successful exection of front_end.py, local url would be given, go to that url through
your browser.
5. Search Box on Index page appears, in it paste the url of any facebook post then press
enter.
6. You’ll be directed to result page, where result of the sentiment analysis of the given fb
post comments will be shown.
7. Apart from the positive negative sentiment tally, summary of each sentiment along with
word cloud is also shown.
8. Cool Enjoy.

```
Work Flow:
```

1. File training_model.py trains the classifier on classified movie reviews training data, to be
used in classification of new request.
2. front_end.py provides the user end interface based on flask.
3. fetch_comments.py will be called from front_end.py on users request, this will fetch the
comments from fb using graph api for the given post url.
4. model_back.py will be called after all the comments being fetched, it will classify the new
requests i.e. , the comments fetched from fb.
5. model_result.py will be called from front_end.py it will call the model_back.py to classify
each comment from scrape_data.txt based on relevant features from relevant_feature.py
6. Results generated in model_result.py will be sent to front_end.py from where it can be
displayed on the user end, taking the help of wordc.py, sum.py and sumn.py in form of word
cloud registration, positive and negative summary generation respectively.
