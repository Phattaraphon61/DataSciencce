
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.datasets import fetch_20newsgroups
import numpy as np

categories = ['comp.graphics','comp.sys.mac.hardware','sci.electronics']

train = fetch_20newsgroups(subset='train', categories=categories)

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(train.data, train.target)

from joblib import dump
dump(model, 'chatgroup.model')
dump(train, 'train.model')

print(round((model.score(train.data, train.target)*100),2),'%')