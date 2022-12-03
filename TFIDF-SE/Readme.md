# TF/IDF-SE

TF/IDF-SE is written in Python 2. In the following you can find how to run it.

## Requirements and Dependencies
This package is tested with Python 2.7.18.
To run TF/IDF-SE, you need to install the following packages first:
- Numpy (tested with version 1.16.6 -> `pip install numpy==1.16.6`)
- Pandas (tested with version 0.24.2 -> `pip install pandas==0.24.2`)
- SciKit-learn (tested with version 0.18.2 -> `pip install scikit-learn==0.18.2`)

## How to Run

The dataset files are stored in `../datasets` directory.

Run `python run_script.py` to split the dataset, preprocess the text, and run the method.
To select the dataset which you wish to run the script on, please change line 44 in `run_script.py` accordingly.
A variable named 'exp' is defined at line 43 which is used to create a distinct directory (named with the value of this variable) to store the results of the experiment, so that the results of a new experiment would not overwrite the previous ones.

## The Scripts

**divide_data_sortdate.py**

This script receives two arguments, the first is the path to the data, and the second is the data file name.
It expects the data file to be sorted, since __no__ ordering is done in the script.
After reading the first column of the file (i.e., issueKey) to find the number of issues in the file, it starts dividing the issues in three sets with a rate of 60%-20%-20%.
Basically, the script produces a text file in the current directory (i.e., the directory of the script) with '\_3sets.txt' suffix (for example, MESOS_3sets.txt).
This file will guide the preprocessing script to divide the data set.

**preprocess.py**

This script receives two arguments, the first is the path to the data and the second is the project name (i.e., data file name).

The script reads the data file and looks for a file with the project name and '\_3sets.txt' suffix in the current directory. If found, the file is used to split the dataset.
Then, `tokenizer.perl` is used to tokenise the set of sentences. If tokeniser did not work, consider changing the tokeniser command at line 10: 

`tokenizer_cmd = ['/usr/bin/perl', 'tokenizer.perl', '-l', 'en', '-q', '-']`

The first argument of the command is the path to Perl installation directory, which needs to be corrected based on the OS and customised installations.
The `tokenizer.perl` script is included in the package in the current directory.
Once done, this script produces and stores in the `data` directory inside the current directory two files, one with `.pkl.gz` extension which contains the tokenised text, and the other with `.dict.pkl.gz` extension which contains a dictionary build upon the training set. This is dictionary is used to vectorise the text in all three train, validation, and test sets.

**tfidf_se_method.py**

This script runs the TF/IDF-SE method.
It loads the data produced by the preprocess.py script. Then creates a pipe line consisting of a featuree selection and the classification unit (i.e., Support Vector Classification) and uses the training set to build the model. Then uses the model to estimatee the classes (i.e., story points) for the issues in the test set and stores the actual and estimated values in separate files. 

**measurement.py**

This script simply reads the actual and estimated story points from the files created by the tfidf_se_method.py script and produce the another file containing the absolute errors of the estimations in the same directory. It also computes and writes/appends the MAE and MdAE of the estimations per project in a single file named `performance_all.csv` inside the experiment results directory (i.e., `[exp]/log/performance_all.csv`).


