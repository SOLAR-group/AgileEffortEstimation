import gzip
import cPickle
import numpy
import sys
import os
import preprocess
from sklearn.feature_selection import f_classif

args = preprocess.arg_passing(sys.argv)

expName = args['-exp']
project = args['-project']

f = gzip.open('files/' + project + '.pkl.gz', 'rb')

train_context, train_code, train_binaryfeats, train_y, \
valid_context, valid_code, valid_binaryfeats, valid_y, \
test_context, test_code, test_binaryfeats, test_y = numpy.array(cPickle.load(f))


def listtostring(word_id):
    str_id = []
    for i in range(len(word_id)):
        str_id.append(' '.join(map(str, word_id[i])))
    return str_id


def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0, size):
        list_of_objects.append(list())  # different object reference each time
    return list_of_objects


print 'convert word id to text...'

train_context = numpy.array(train_context)
train_code = numpy.array(train_code)
train_binaryfeats = numpy.array(train_binaryfeats)
train_y = numpy.array(train_y)

test_context = numpy.array(test_context)
test_code = numpy.array(test_code)
test_binaryfeats = numpy.array(test_binaryfeats)
test_y = numpy.array(test_y)

from sklearn.feature_extraction.text import TfidfVectorizer

# build TfidfVectorizer for monogram and bi-gram for contexts
tfidf_vectorizer = TfidfVectorizer(stop_words=None, lowercase=False, ngram_range=[1, 2])
tfidf_vectorizer.fit(listtostring(train_context))
train_context_tfidf = tfidf_vectorizer.transform(listtostring(train_context)).toarray()
test_context_tfidf = tfidf_vectorizer.transform(listtostring(test_context)).toarray()

# build TfidfVectorizer for monogram and bi-gram for codedsnippet
tfidf_vectorizer = TfidfVectorizer(stop_words=None, lowercase=False, ngram_range=[1, 2])
tfidf_vectorizer.fit(listtostring(train_code))
train_code_tfidf = tfidf_vectorizer.transform(listtostring(train_code)).toarray()
test_code_tfidf = tfidf_vectorizer.transform(listtostring(test_code)).toarray()

# concat all features
train_x = numpy.concatenate((train_context_tfidf, train_code_tfidf, train_binaryfeats), axis=1)
test_x = numpy.concatenate((test_context_tfidf, test_code_tfidf, test_binaryfeats), axis=1)

# #############################################################################
# Create a feature-selection transform and an instance of SVM that we
# combine together to have an full-blown estimator

from sklearn.pipeline import Pipeline
from sklearn import svm, feature_selection

transform = feature_selection.SelectKBest(score_func=f_classif, k=50)
clf = Pipeline([('feat_select', transform), ('classifier', svm.SVC())])
clf.fit(train_x, numpy.floor(train_y))
predict = clf.predict(test_x)

if not os.path.exists(expName + '/log/ar/'):
    os.makedirs(expName + '/log/ar/')
numpy.savetxt(expName + '/log/ar/' + project + "_actual.csv", test_y, delimiter=",")
numpy.savetxt(expName + '/log/ar/' + project + "_estimate.csv", predict, delimiter=",")
print 'output is saved at ' + expName + '/log/ar/'
