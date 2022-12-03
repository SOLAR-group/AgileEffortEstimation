import os

Choet_dataset = {
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

Porru_dataset = {
    'MESOS': 'Apache',
    'TISTUD': 'Appcelerator',
    'APSTUD': 'Appcelerator',
    'TIMOB': 'Appcelerator',
    'DNN': 'DNNSoftware',
    'MULE': 'Mulesoft',
    'NEXUS': 'Sonatype',
    'XD': 'Spring'
}

Tawosi_dataset = {
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

datasetDict = Choet_dataset # Tawosi_dataset | Prrru_dataset
exp = 'rq1_1'

model = 'seq'
dims = ['50']  #all parameters are set based on the tuning performed by Choetkiertikul et al. and reported in the original study

nnet_models = ['highway']  # ['dense', 'highway']
seq_models = ['lstm']      # ['gru', 'lstm', 'rnn']
regs = ['inphid']          # ['x', 'inp', 'hid', 'inphid'] # 'x' means no dropout
pretrains = ['finetune_lm']          # ['x', 'finetune', 'fixed'] should use finetune_lm or fixed_lm for using lstm
                           # 'x' means no pretraining,
                           # 'finetune' means embedding matrix is initialized by pretrained parameters
                           # 'fixed' means using pretrained embedding matrix as input features
                           # add '_lm' if using 'lstm' for pretraining, default: 'bilinear' for pretraining
pools = ['mean']           # ['mean', 'max', 'last']
maxlen = '100'
hdls = ['10']

# Running script:
if model == 'seq':
    for project, repository in datasetDict.items():
        for nnet in nnet_models:
            for seq in seq_models:
                for dim in dims:
                    for reg in regs:
                        for pretrain in pretrains:
                            for pool in pools:
                                for hidd in hdls:
                                    project = project + '_deep-se'
                                    cmd = 'python training.py -data ' + project + ' -exp ' + exp + ' -dataPre ' + repository + \
                                          ' -nnetM ' + nnet + ' -seqM ' + seq + ' -dim ' + dim + \
                                          ' -reg ' + reg + ' -pretrain ' + pretrain + ' -pool ' + pool + ' -len ' + maxlen
                                    cmd += ' -saving ' + project + '_' + seq + '_' + nnet + '_dim' + dim + \
                                           '_reg' + reg + '_pre' + pretrain + '_pool' + pool + ' -hiddenLayer ' + hidd
                                    # file name e.g. MESOS_deep-se_lstm_highway_dim100_reginphid_prefixed_lm_poolmean.txt
                                    print cmd
                                    os.system(cmd)