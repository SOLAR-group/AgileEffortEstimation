import gzip
import numpy
import cPickle as pkl
import load_raw_text
import preprocess
import sys
import os

def main():
    # load pretrain text:
    args = preprocess.arg_passing(sys.argv)
    path = args['-path']
    repo = args['-repo']

    pretrain_path = path + repo + '.csv'
    pre_title, pre_descr = load_raw_text.load_pretrain(pretrain_path)
    print 'number of datapoints:', len(pre_title)

    n_train = len(pre_title) * 2 // 3
    ids = numpy.arange(len(pre_title))
    numpy.random.shuffle(ids)
    train_ids = ids[:n_train]
    valid_ids = ids[n_train:]
    train = numpy.concatenate([pre_title[train_ids], pre_descr[train_ids]])
    valid = numpy.concatenate([pre_title[valid_ids], pre_descr[valid_ids]])
    dictionary = preprocess.build_dict(train)
    pre_train, pre_valid = preprocess.grab_data(train, valid, dictionary)
    if not os.path.exists('files/'):
        os.makedirs('files/')
    f_pre = gzip.open('files/' + repo + '.pkl.gz', 'wb')
    pkl.dump((pre_train, pre_valid, pre_valid), f_pre, -1)
    f_pre.close()
    print 'saved the output at files/' + repo + '.pkl.gz'

    f = gzip.open('files/' + repo + '.dict.pkl.gz', 'wb')
    pkl.dump(dictionary, f, -1)
    f.close()
    print 'saved the output at files/' + repo + '.dict.pkl.gz'


if __name__ == '__main__':
    main()
