import sys
from time import time

import numpy as np
from sklearn.externals import joblib
from sklearn.metrics import precision_score 

from pyleml import LEML

def main():
    print 'Loading data'
    sys.stdout.flush()
    X = joblib.load('./test_data/bibtex-train.pkl')
    labels = joblib.load('./test_data/bibtex-Y-train.pkl')
    X_test = joblib.load('./test_data/bibtex-test.pkl')
    labels_test = joblib.load('./test_data/bibtex-Y-test.pkl')
    print X.shape, labels.shape, X.getformat(), labels.getformat()

    print 'Training LEML'
    sys.stdout.flush()
    t0 = time()
    leml = LEML.get_instance('parallel', num_factors=64, num_iterations=25, reg_param=1., verbose=True)
    leml.fit(X.tocsc(), labels.tocsc().astype('float'))
    print 'Train time', time() - t0, 'seconds'
    sys.stdout.flush()
    preds = leml.predict(X_test)
    preds_top_k = preds.argsort()[:,::-1]
    preds_top_k = preds_top_k[:,:1]
    new_preds = np.zeros((preds.shape[0], preds.shape[1]))
    new_preds[np.arange(preds.shape[0]).repeat(1),preds_top_k.flatten()] = 1
    print 'Precision @ 1:', precision_score(labels_test.toarray(), new_preds, average='samples')

    preds_top_k = preds.argsort()[:,::-1]
    preds_top_k = preds_top_k[:,:3]
    new_preds = np.zeros((preds.shape[0], preds.shape[1]))
    new_preds[np.arange(preds.shape[0]).repeat(3),preds_top_k.flatten()] = 1
    print 'Precision @ 3:', precision_score(labels_test.toarray(), new_preds, average='samples')

    preds_top_k = preds.argsort()[:,::-1]
    preds_top_k = preds_top_k[:,:5]
    new_preds = np.zeros((preds.shape[0], preds.shape[1]))
    new_preds[np.arange(preds.shape[0]).repeat(5),preds_top_k.flatten()] = 1
    print 'Precision @ 5:', precision_score(labels_test.toarray(), new_preds, average='samples')


if __name__ == '__main__':
    main()
