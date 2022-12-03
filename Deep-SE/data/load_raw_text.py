import pandas
import os


def normalize(seqs):
    for i, s in enumerate(seqs):
        words = s.split()
        if len(words) < 1:
            seqs[i] = 'null'

    return seqs


def load_pretrain(path):
    data = pandas.read_csv(path).values
    return normalize(data[:, 1].astype('str')), normalize(data[:, 2].astype('str'))


def load(path):
    def cut_of90(labels):
        # [Vali]: this method performs the 90th percentile transformation, which is used by the original study.
        #         However, we only used it for replication purpose for some RQs in our study.
        val_y = list(set(labels))
        val_y.sort()
        l_dict = dict()
        for i, val in enumerate(val_y): l_dict[int(val)] = i

        count_y = [0] * len(val_y)
        for label in labels:
            count_y[l_dict[int(label)]] += 1

        n_samples = len(labels)
        s, threshold = 0, 0
        for i, c in enumerate(count_y):
            s += c
            if s * 10 >= n_samples * 9:
                threshold = val_y[i]
                break
        for i, l in enumerate(labels):
            labels[i] = min(threshold, l)

        return labels.astype('float32')

    if not os.path.isfile(path):
        raise Exception('expected file not found! file= ' + path)
    data = pandas.read_csv(path)

    # the following line drops created column which is only present in Tawosi dataset. This column contains the creation
    # date-time of each bug, which is used to sort the issues but is not needed here.
    data = data.drop(['created'], axis=1, errors='ignore')
    data = data.values

    title = normalize(data[:, 1].astype('str'))
    description = normalize(data[:, 2].astype('str'))
    labels = data[:, 3].astype('float32')

    # to use the 90th percentile transformation toggle the comment in the following two statements
    # return title, description, cut_of90(labels)
    return title, description, labels
