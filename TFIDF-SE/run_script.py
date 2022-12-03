import os

Porru_Dataset = [
    'MESOS',
    'TISTUD',
    'APSTUD',
    'TIMOB',
    'DNN',
    'MULE',
    'NEXUS',
    'XD'
]

Tawosi_Dataset = [
    'MESOS',
    'ALOY',
    'TISTUD',
    'APSTUD',
    'CLI',
    'DAEMON',
    'TIDOC',
    'TIMOB',
    'CLOV',
    'CONFCLOUD',
    'CONFSERVER',
    'DNN',
    'DURACLOUD',
    'FAB',
    'STL',
    'DM',
    'COMPASS',
    'SERVER',
    'EVG',
    'MDL',
    'MULE',
    'NEXUS',
    'XD'
    ]

exp = 'rq2_2'
datasetDict_ = 'Porru_Dataset'  # 'Tawosi_Dataset' | 'Porru_Dataset'
data_path = '../datasets/' + datasetDict_ + '/'

if datasetDict_ == 'Tawosi_Dataset':
    datasetList = Tawosi_Dataset
elif datasetDict_ == 'Porru_Dataset':
    datasetList = Porru_Dataset

for project in datasetList:
    cmd = 'python divide_data_sortdate.py -path ' + data_path + ' -project ' + project + '_tfidf-se'
    print cmd
    os.system(cmd)

for project in datasetList:
    cmd = 'python preprocess.py -path ' + data_path + ' -project ' + project + "_tfidf-se"
    print cmd
    os.system(cmd)

# run TF/IDF-SE model
for project in datasetList:
    cmd = 'python tfidf_se_method.py -exp ' + exp + ' -project ' + project + '_tfidf-se'
    print cmd
    os.system(cmd)

    print 'compute error'
    cmd = 'python measurement.py -exp ' + exp + ' -project ' + project + '_tfidf-se'
    os.system(cmd)
