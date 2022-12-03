import numpy
from subprocess import Popen, PIPE

chosen_frequency = 30
# tokenizer.perl is from Moses: https://github.com/moses-smt/mosesdecoder/tree/master/scripts/tokenizer
tokenizer_cmd = ['/usr/bin/perl', 'tokenizer.perl', '-l', 'en', '-q', '-']


def arg_passing(argv):
    i = 1
    arg_dict = {}
    while i < len(argv) - 1:
        arg_dict[argv[i]] = argv[i+1]
        i += 2
    return arg_dict


def tokenize(sentences):
    print 'Tokenizing..',
    text = "\n".join(sentences)
    tokenizer = Popen(tokenizer_cmd, stdin=PIPE, stdout=PIPE)
    tok_text, _ = tokenizer.communicate(text)
    toks = tok_text.split('\n')[:-1]
    print 'Done'
    return toks


def build_dict(sentences):
    sentences = tokenize(sentences)
    print 'Building dictionary..'
    wordcount = dict()
    for ss in sentences:
        words = ss.strip().lower().split()
        for w in words:
            if w not in wordcount:
                wordcount[w] = 1
            else:
                wordcount[w] += 1

    counts = wordcount.values()
    keys = wordcount.keys()

    sorted_idx = numpy.argsort(counts)[::-1]
    counts = numpy.array(counts)

    print 'number of words in dictionary:', len(keys)

    worddict = dict()

    for idx, ss in enumerate(sorted_idx):
        worddict[keys[ss]] = idx+1  # leave 0 (UNK)

    pos = 0
    for i, c in enumerate(sorted_idx):
        if counts[c] >= chosen_frequency: pos = i

    print numpy.sum(counts), ' total words, ', pos, 'words with frequency >=', chosen_frequency

    return worddict


def grab_data(title, description, dictionary):
    title = tokenize(title)
    description = tokenize(description)

    seqs = [[None] * len(title), [None] * len(description)]
    for i, sentences in enumerate([title, description]):
        for idx, ss in enumerate(sentences):
            words = ss.strip().lower().split()
            seqs[i][idx] = [dictionary[w] if w in dictionary else 0 for w in words]
            if len(seqs[i][idx]) == 0:
                print 'len 0: ', i, idx

    return seqs[0], seqs[1]