import sys
import os
import numpy
from sklearn.metrics import mean_absolute_error, median_absolute_error
import preprocess

args = preprocess.arg_passing(sys.argv)

expName = args['-exp']
project = args['-project']

actualFile = expName + '/log/ar/' + project + "_actual.csv"
estimateFile = expName + '/log/ar/' + project + '_estimate.csv'


actual = numpy.genfromtxt(actualFile, delimiter=',')
estimate = numpy.genfromtxt(estimateFile, delimiter=',')

# Save absolute error in log/ar
ar_outputFileName = expName + '/log/ar/' + project + '_absolute_error.csv'
numpy.savetxt(ar_outputFileName, (numpy.absolute(actual - estimate)), delimiter=",", fmt='%1.4f')

MAE = mean_absolute_error(actual, estimate)
MdAE = median_absolute_error(actual, estimate)

print project + "," + str(MAE) + "," + str(MdAE) + '\n'

if not os.path.exists(expName + '/log/performance_all.csv'):
    with open(expName + '/log/performance_all.csv', 'w') as myoutput:
        myoutput.write('Project, MAE, MdAE\n')
with open(expName + '/log/performance_all.csv', 'a') as myoutput:
    myoutput.write(project + "," + str(MAE) + "," + str(MdAE) + '\n')