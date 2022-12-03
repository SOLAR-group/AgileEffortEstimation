import numpy
import prepare_data
import sys

args = prepare_data.arg_passing(sys.argv)
numpy.random.seed(args['-seed'])

from keras.optimizers import *
from keras.objectives import *
from create_model import *
from baselines import *
################################# LOAD DATA #######################################################
dataset = args['-data']
data_path = '../data/files/' + dataset + '.pkl.gz'
dataPre = args['-dataPre']
seq_model = args['-seqM']
nnet_model = args['-nnetM']
saving = args['-saving']
hid_dim = args['-dim']
vocab_size = args['-vocab']
pool = args['-pool']
pretrain = args['-pretrain']
max_len = args['-len']
hidden_layer = args['-hiddenLayer']
exp = args['-exp']


if pretrain == 'x':
    emb_weight = None
elif 'w2v' in pretrain:
    pretrain_path = 'word2vec_' + args['-data'] + '_dim' + str(hid_dim) + '.pkl'
    emb_weight = prepare_data.load_w2v_weight(pretrain_path)
else:
    if 'lm' in pretrain:
        lm = 'lm'
    else: 
        lm = ''
    pretrain_path = 'lstm2v_' + args['-dataPre'] + '_dim' + str(hid_dim)
    emb_weight = prepare_data.load_weight(pretrain_path)

if 'inp' in args['-reg']: 
    dropout_inp = True
else: 
    dropout_inp = False
if 'hid' in args['-reg']: 
    dropout_hid = True
else: 
    dropout_hid = False

train_t, train_d, train_y, valid_t, valid_d, valid_y, test_t, test_d, test_y = prepare_data.load(data_path)
train_t, train_tmask, train_d, train_dmask = prepare_data.prepare_data(train_t, train_d, vocab_size, max_len)
valid_t, valid_tmask, valid_d, valid_dmask = prepare_data.prepare_data(valid_t, valid_d, vocab_size, max_len)
test_t, test_tmask, test_d, test_dmask = prepare_data.prepare_data(test_t, test_d, vocab_size, max_len)

print ('ntrain: %d, n_valid: %d, n_test: %d' % (len(train_y), len(valid_y), len(test_y)))

if not os.path.exists('bestModels/'):
    os.makedirs('bestModels/')
if not os.path.exists('models/'):
    os.makedirs('models/')
if not os.path.exists(exp + '/log/ar'):
    os.makedirs(exp + '/log/ar')

mae_rg = do_baselines(exp, '/log/ar', dataset, train_y, test_y)

if train_y.dtype == 'float32':
    n_classes = -1
    loss = mean_squared_error
elif max(train_y) > 1:
    n_classes = max(train_y) + 1
    loss = sparse_categorical_crossentropy
else:
    n_classes = 1
    loss = binary_crossentropy

###################################### BUILD MODEL##################################################
print 'Building model...'

if 'fixed' in pretrain:
    train_t, train_d, valid_t, valid_d, test_t, test_d = prepare_data.to_features([train_t, train_d,
                                                                                   valid_t, valid_d,
                                                                                   test_t, test_d], emb_weight)
    # n_classes, inp_len, emb_dim,
    # seq_model='lstm', nnet_model='highway', pool_mode='mean',
    # dropout_inp=False, dropout_hid=True):

    model = create_fixed(n_classes=n_classes, inp_len=train_t.shape[1], emb_dim=hid_dim,
                         seq_model=seq_model, nnet_model=nnet_model, pool_mode=pool,
                         dropout_inp=dropout_inp, dropout_hid=dropout_hid)
else:
    # n_classes, vocab_size, inp_len, emb_dim,
    # seq_model='lstm', nnet_model='highway', pool_mode='mean',
    # dropout_inp=False, dropout_hid=True
    model = create_model(n_classes=n_classes, vocab_size=vocab_size + 1, inp_len=train_t.shape[-1], emb_dim=hid_dim,
                         seq_model=seq_model, nnet_model=nnet_model, pool_mode=pool,
                         dropout_inp=dropout_inp, dropout_hid=dropout_hid, emb_weight=emb_weight,
                         hidden_layer=hidden_layer)

model.summary()
json_string = model.to_json()
fModel = open('models/' + saving + '.json', 'w')
fModel.write(json_string)

opt = RMSprop(lr=0.01)
model.compile(optimizer=opt, loss=loss)

train_y = numpy.expand_dims(train_y, -1)

fParams = 'bestModels/' + saving + '.hdf5'
fResult = saving + '.txt'

if n_classes == -1: 
    type = 'linear'
elif n_classes == 1:
    type = 'binary'
else:
    type = 'multi'

saveResult = SaveResult([[valid_t, valid_tmask, valid_d, valid_dmask], valid_y,
                         [test_t, test_tmask, test_d, test_dmask], test_y],
                        metric_type=type, expName=exp, fileResult=fResult, fileParams=fParams,train_label=train_y,
                        mae_r_guess=mae_rg)

callbacks = [saveResult, NanStopping()]
his = model.fit([train_t, train_tmask, train_d, train_dmask], train_y,
                validation_data=([valid_t, valid_tmask, valid_d, valid_dmask], numpy.expand_dims(valid_y, -1)),
                nb_epoch=1000, batch_size=100, callbacks=callbacks)