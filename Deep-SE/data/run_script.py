import os

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


dataPres = [
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

datasetDict_ = 'Porru_Dataset'  # 'Choet_Dataset' | 'Tawosi_Dataset' | 'Porru_Dataset' | 'Pretrain_Dataset'
data_path = '../../datasets/' + datasetDict_ + '/'

if datasetDict_ == 'Pretrain_Dataset':
    # Preprocess pre-train data: load, divide, and build dictionary and produce pickled data ready for pre-training
    for dataPre in dataPres:
        cmd = 'python preprocess_pretrain.py -path ' + data_path + ' -repo ' + dataPre
        print cmd
        os.system(cmd)
else:
    if datasetDict_ == 'Choet_Dataset':
        datasetDict = Choet_Dataset
    elif datasetDict_ == 'Tawosi_Dataset':
        datasetDict = Tawosi_Dataset
    elif datasetDict_ == 'Porru_Dataset':
        datasetDict = Porru_Dataset

    #  Divide the datasets to train-validation-test sets. It produces text files in which each bug is labelled with
    #  one of the three sets. This file is used by preprocess_storypoint.py to split the datasets.
    for project, repo in datasetDict.items():
        print project + ' ' + repo
        cmd = 'python divide_data_sortdate.py -path ' + data_path + ' -project ' + project + '_deep-se'
        print cmd
        os.system(cmd)

    # Preprocess the datasets for story point estimation: load, divide, and produce pickled data ready for training
    for project, repo in datasetDict.items():
        print project + ' ' + repo
        # Use the following statement for Deep-SE With pre-training
        cmd = 'python preprocess_storypoint.py -path ' + data_path + ' -project ' + project + '_deep-se -repo ' + repo
        # Use the following statement for Deep-SE Without pre-training
        # cmd = 'python preprocess_storypoint.py -path ' + data_path + ' -project ' + project + '_deep-se'
        print cmd
        os.system(cmd)








