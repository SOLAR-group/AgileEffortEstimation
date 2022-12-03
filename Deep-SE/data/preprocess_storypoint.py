import gzip
import sys
import os
import cPickle
import numpy
import load_raw_text
import preprocess


def main():
    # load training data:
    args = preprocess.arg_passing(sys.argv)
    path = args['-path']
    project = args['-project']
    if '-repo' in args.keys():
        repo = args['-repo']
    else:
        repo = ''

    data_path = path + project + '.csv'
    title, description, labels = load_raw_text.load(data_path)

    if not os.path.isfile('files/' + project + '_3sets.txt'):
        raise Exception('expected file not found! file= files/' + project + '_3sets.txt')
    f = open('files/' + project + '_3sets.txt', 'r')
    train_ids, valid_ids, test_ids = [], [], []
    count = -2
    for line in f:
        if count == -2:
            count += 1
            continue

        count += 1
        ls = line.split()
        if ls[0] == '1': train_ids.append(count)
        if ls[1] == '1': valid_ids.append(count)
        if ls[2] == '1': test_ids.append(count)

    print 'ntrain, nvalid, ntest: ', len(train_ids), len(valid_ids), len(test_ids)

    train_title, train_description, train_labels = title[train_ids], description[train_ids], labels[train_ids]
    valid_title, valid_description, valid_labels = title[valid_ids], description[valid_ids], labels[valid_ids]
    test_title, test_description, test_labels = title[test_ids], description[test_ids], labels[test_ids]

    if repo == '':
        # Use Deep-SE without pre-training
        dictionary = preprocess.build_dict(numpy.concatenate([train_title, train_description]))
    else:
        # Use Deep-SE with pre-training
        if not os.path.isfile('files/' + repo + '.dict.pkl.gz'):
            raise Exception('expected file not found! file= files/' + repo + '.dict.pkl.gz\nRepo name (for pre-training) is provided but the file is not!')
        f_dict = gzip.open('files/' + repo + '.dict.pkl.gz', 'rb')
        dictionary = cPickle.load(f_dict)

    train_t, train_d = preprocess.grab_data(train_title, train_description, dictionary)
    valid_t, valid_d = preprocess.grab_data(valid_title, valid_description, dictionary)
    test_t, test_d = preprocess.grab_data(test_title, test_description, dictionary)

    f = gzip.open('files/' + project + '.pkl.gz', 'wb')
    cPickle.dump((train_t, train_d, train_labels,
              valid_t, valid_d, valid_labels,
              test_t, test_d, test_labels), f, -1)
    f.close()
    print 'saved the output at files/' + project + '.pkl.gz'


if __name__ == '__main__':
    main()
