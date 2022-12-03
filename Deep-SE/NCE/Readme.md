# *NCE* Module

This module contains the scripts for pre-trainng the lower layers of Deep-SE (i.e., the embedding and LSTM layers).


## How to run

**Training the language models**

To train the pre-training language models, run `python NCE/exp_lstm2v.py` after you made the following changes in the script:

- set `mode = 'pretrain'` at line 3
- set `datasetDict = Pretrain_Dataset` at line 80
- set Theano flags (if needed) at line 86

This will use the pre-training data files (must be produced by data module described [here](../data/Readme.md#examples)) and will train a language model which is able to predict the next token based on the context learned from the issues appeared in the repository. This model will be used be the next step to pre-train the lower layers of Deep-SE.

This stage can be time consuming, so we include in the package ([here](bestModels/)) the pre-trained language models, which can be directly used in the next stage.


**Pre-Training the lower layer**

To pre-trainng the lower layers of Deep-SE, run `python NCE/exp_lstm2v.py` after you made the following changes in the script:

- set `mode = 'lstm2vec'` at line 3
- select preferred dataset by changing line 80 (for example, `datasetDict = Tawosi_Dataset`)
- set Theano flags (if needed) at line 86

This configuration will use the pre-trained language models to tune weights for the lower layers of Deep-SE using the data from the project. This will produce a file inside the data directory of current path (i.e., `NCE/data/`) with 'lstm2v_' preifix and '\_dim50.pkl.gz' suffix. This file contains the initialization weights for the lower layers of Deep-SE.


