import os

mode = 'lstm2vec'  # 'lstm2vec' for lstm 2 vector and 'pretrain' for pretraining

Choet_Dataset = {
    'MESOS': 'Apache',
    'USERGRID': 'Apache',
    'TISTUD': 'Appcelerator',
    'APSTUD': 'Appcelerator',
    'TIMOB': 'Appcelerator',
    'BAM': 'Atlassian',
    'CLOV': 'Atlassian',
    'JRESERVER': 'Atlassian',
    'DURACLOUD': 'Duraspace',
    'DM': 'Lsstcorp',
    'MDL': 'Moodle',
    'MULE': 'Mulesoft',
    'MULESTUDIO': 'Mulesoft',
    'XD': 'Spring'
}

Porru_Dataset = {
    'MESOS': 'Apache',
    'TISTUD': 'Appcelerator',
    'APSTUD': 'Appcelerator',
    'TIMOB': 'Appcelerator',
    'DNN': 'DNNSoftware',
    'MULE': 'Mulesoft',
    'NEXUS': 'Sonatype',
    'XD': 'Spring'
}

Tawosi_Dataset = {
    'MESOS': 'Apache',
    'ALOY': 'Apache',
    'TISTUD': 'Appcelerator',
    'APSTUD': 'Appcelerator',
    'CLI': 'Appcelerator',
    'DAEMON': 'Appcelerator',
    'TIDOC': 'Appcelerator',
    'TIMOB': 'Appcelerator',
    'CLOV': 'Atlassian',
    'CONFCLOUD': 'Atlassian',
    'CONFSERVER': 'Atlassian',
    'DNN': 'DNNSoftware',
    'DURACLOUD': 'Duraspace',
    'FAB': 'Hyperledger',
    'STL': 'Hyperledger',
    'DM': 'Lsstcorp',
    'COMPASS': 'MongoDB',
    'SERVER': 'MongoDB',
    'EVG': 'MongoDB',
    'MDL': 'Moodle',
    'MULE': 'Mulesoft',
    'NEXUS': 'Sonatype',
    'XD': 'Spring'
}

Pretrain_Dataset = [
    'Apache',
    'Appcelerator',
    'Duraspace',
    'Atlassian',
    'Moodle',
    'Lsstcorp',
    'Mulesoft',
    'Spring',
    'DNNSoftware',
    'Hyperledger',
    'MongoDB',
    'Sonatype'
]

datasetDict = Choet_Dataset  # Choet_Dataset | Tawosi_Dataset | Porru_Dataset | Pretrain_Dataset

dims = ['50']
maxlen = '100'
vocab = '5000'  # vocab size. for large dataset, the vocab size should be set 5k - 10k.

flag = ''  # 'THEANO_FLAGS=\'floatX=float32,device=gpu\' '

if mode == 'pretrain':
    for dim in dims:
        for dataPre in datasetDict:
            command = flag + 'python lstm2vec_pretrain.py -data ' + dataPre + \
                      ' -saving lstm2v_' + dataPre + '_dim' + dim + \
                      ' -vocab ' + vocab + ' -dim ' + dim + ' -len ' + maxlen
            print command
            os.system(command)

elif mode == 'lstm2vec':
    for dim in dims:
        for project, repo in datasetDict.items():
            if repo == 'Lsstcorp':
                vocab = '800'
            elif repo == 'Mulesoft':
                vocab = '1600'
            else:
                vocab = '5000'
            command = flag + 'python lstm2vec.py -dataPre ' + repo + ' -data ' + project + \
                      '_deep-se -vocab ' + vocab + ' -dim ' + dim + ' -len ' + maxlen + \
                      ' -saving lstm2v_' + project + '_deep-se_' + repo + '_dim' + dim
            print command
            os.system(command)
