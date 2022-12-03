import numpy
import os
import sys
import pandas
from sklearn import metrics


def main():
    args = sys.argv
    input_path = args[1]
    output_path = args[1] + 'baselines/'
    dataset = args[2]
    exp = ['pt', 'et', 'rt']  # target values should be listed alongside each other in this order
    data_train = pandas.read_csv(input_path + dataset + '-train.csv').values
    data_test = pandas.read_csv(input_path + dataset + '-test.csv').values

    for experiment in exp:
        index_in_file = 6 + exp.index(experiment)  # 2 is the offset of the target values in the file.
        # train_labels = data_train[:, index_in_file].astype('float32')
        # test_labels = data_test[:, index_in_file].astype('float32')
        train_labels = numpy.divide(data_train[:, index_in_file].astype('float32'), 1440)
        test_labels = numpy.divide(data_test[:, index_in_file].astype('float32'), 1440)
        do_baselines(experiment, output_path, dataset, train_labels, test_labels)


def do_baselines(experiment, path, dataset, train_y, test_y):
    root_path = experiment + path
    if not os.path.exists(root_path):
        os.makedirs(root_path)
    if os.path.exists(root_path + '/' + dataset + '_rg_mae.txt'):
        rg_f = open(root_path + '/' + dataset + '_rg_mae.txt')
        mae_rguess = float(rg_f.read())
    else:
        mae_rguess = mae_random_guess(train_y, test_y)
        with open(root_path + '/' + dataset + '_rg_mae.txt', 'w') as f:
            f.write('%.4f' % mae_rguess)
            f.close()
    mean_mae, mean_mdae, mean_sa = mean_baseline(dataset, mae_rguess, root_path, test_y, train_y)
    median_mae, median_mdae, median_sa = median_baseline(dataset, mae_rguess, root_path, test_y, train_y)

    with open(root_path + '/' + dataset + '_baseline.txt', 'w') as f:
        f.write('mae_rguess, '
                'mean train, mean_mae, mean_mdae, mean_sa, '
                'median_train, median_mae, median_mdae, median_sa\n')
        f.write('%.4f,%.4f,%.4f,%.4f,%.4f,%.4f,%.4f,%.4f,%.4f'
                % (mae_rguess,
                   numpy.mean(train_y), mean_mae, mean_mdae, mean_sa,
                   numpy.median(train_y), median_mae, median_mdae, median_sa))
        f.close()
    return mae_rguess


def mae_random_guess(sample, target):
    mae_r = []
    for i in range(1000):
        r_guess = numpy.random.choice(a=sample, size=len(target))
        mae_r = numpy.append(mae_r, metrics.mean_absolute_error(target, r_guess))
    return numpy.mean(mae_r)


def median_baseline(dataset, mae_rguess, path, test_y, train_y):
    median_list = [numpy.median(train_y)] * len(test_y)
    median_mae = metrics.mean_absolute_error(test_y, median_list)
    median_mdae = metrics.median_absolute_error(test_y, median_list)
    median_sa = (1 - (median_mae / mae_rguess)) * 100
    print 'median_train = %.5f' % numpy.median(train_y)
    print 'median_mae   = %.5f' % median_mae
    print 'median_mdae  = %.5f' % median_mdae
    print 'median_sa    = %.5f' % median_sa
    with open(path + '/' + dataset + '_median.txt', 'w') as median_f:
        ar = numpy.abs(numpy.subtract(test_y, median_list))
        for i in ar:
            median_f.write('%.5f' % i)
            median_f.write('\n')
        median_f.close()
    return median_mae, median_mdae, median_sa


def mean_baseline(dataset, mae_rguess, path, test_y, train_y):
    print('%s: mae_rguess = %f' % (dataset, mae_rguess))
    mean_list = [numpy.mean(train_y)] * len(test_y)
    mean_mae = metrics.mean_absolute_error(test_y, mean_list)
    mean_mdae = metrics.median_absolute_error(test_y, mean_list)
    mean_sa = (1 - (mean_mae / mae_rguess)) * 100
    print 'mean train = %.5f' % numpy.mean(train_y)
    print 'mean_mae   = %.5f' % mean_mae
    print 'mean_mdae  = %.5f' % mean_mdae
    print 'mean_sa    = %.5f' % mean_sa
    with open(path + '/' + dataset + '_mean.txt', 'w') as mean_f:
        ar = numpy.abs(numpy.subtract(test_y, mean_list))
        for i in ar:
            mean_f.write('%.5f' % i)
            mean_f.write('\n')
        mean_f.close()
    return mean_mae, mean_mdae, mean_sa


if __name__ == '__main__':
    main()
