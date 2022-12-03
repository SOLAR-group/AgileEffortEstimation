# *Classification* Module

This module contains the scripts for Deep-SE.


## How to run

Run `python exp_script.py`. 
To select the dataset which you wish to run the script on, please change line 62.
A variable named 'exp' is defined at line 63 which is used to create a distinct directory (named with the value of this variable) to store the results of the experiments, so that the results of a new experiment would not overwrite the previous ones

There is an option for using pre-trained weights for the lower layers of Deep-SE or simply initializing them with random numbers. You can change this at line 71. Variable 'pretrains' is a list which can accept multiple options and the script will run Deep-SE with all the options given in the list.
In this list, 'x' means *use random weights* and 'finetune_lm' means *use pre-trained weights for LSTM*.

All the other variables have been set by the best values reported in the original study as they have performed a tuning on the parameters.