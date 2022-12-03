# Deep-SE

Deep-SE is written in Python 2 and is organized in three modules, *data*, *NEC*, and *classification*.

## Requirements and Dependencies
This package is tested with Python 2.7.18.
To run Deep-SE, you need to install the following packages first:
- Keras version 1.0.6 (`pip install keras==1.0.6`)
- Theano version 0.9.0 (`pip install theano==0.9.0`)
- Numpy (tested with version 1.16.6 -> `pip install numpy==1.16.6`)
- Pandas (tested with version 0.24.2 -> `pip install pandas==0.24.2`)
- SciKit-learn (tested with version 0.18.2 -> `pip install scikit-learn==0.18.2`)

You can install all the required dependencies by running the following command at the current directory:

`pip install -r requirements.txt` 

You also need to tell Keras to use Theano in its back-end. This can be done by setting "backend" attribute in keras settings json file to "theano". If you are on a UNIX like system (MacOS X or Linux), you can find keras.json file under `/home/[your username]/.keras/`. If there is no such directory or file, you can create one. For more help on this, click here: [how to switch backend with keras from tensorflow to theano](https://stackoverflow.com/questions/42177658/how-to-switch-backend-with-keras-from-tensorflow-to-theano). 


## How to Run

The dataset files are stored in `../datasets` directory.

Run `python data/run_script.py` to split the dataset files to train-validation-test sets and tokenises the textual information to be used by Deep-SE in later steps.
For detailed information regarding how the *data* module works and how to configure it for different datasets, please refer to [data/Readme.md](data/Readme.md).

If you wish to use pre-training, after running `python data/run_script.py` with setting the dataset to Pretrain_Dataset, run `python NCE/exp_lstm2v.py` with `mode` set to `lstm2vec` at line 3 of the script.
You also need to set the preferred dataset by changing line 80.
For more information on this module please refer to [NCE/Readme.md](NCE/Readme.md).


Now you can run `python classification/exp_script.py` to perform issue story point estimation using Deep-SE.
For more information on this module please refer to [classification/Readme.md](classification/Readme.md).
