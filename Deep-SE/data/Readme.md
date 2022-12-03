# *data* Module

This module contains the scripts for data preparation and preprocessing for Deep-SE.


## How to run

Run `python data/run_script.py` to split the dataset files to train-validation-test sets and tokenises the textual information to be used by Deep-SE.

This script defined three dictionaries (one per each dataset, namely, Tawosi Dataset, Choet Dataset, and Porru Dataset). There is also a list for Pre-training datasets (`dataPres`).

Change line 79 to select the dataset that the script should use.
Change line 80 if the path to the dataset is different from the dataset coming with this package. 

## Examples

**Run script on the *Tawosi Dataset***

To run the script on the Tawosi dataset, you need to change line 79 to:

`datasetDict_ = 'Tawosi_Dataset' `

then, execute `python data/run_script.py` from the command line. This will split the dataset files and perform tokenization.

**Run script on the *Pre-training datasets***

To run the script on Pre-training datasets, you need to change line 79 to:

`datasetDict_ = 'Pretrain_Dataset'`

then, execute `python data/run_script.py` from the command line.


## The scripts

**load_raw_text.py**

This script loads the data file and returns the normalised title, description, and story points as separated lists.
After reading the data file, it tries to drop `'created'` column. This column exists in the Tawosi dataset only, and used for ordering the issues and selecting issues for augmentation.

This script also performs a transformation on the distribution of the story points (described in our paper).
To toggle between using the transformation or discarding it, please, toggle the comment char in lines 58 and 59, before running the script.  

**divide_data_sortdate.py**

This script receives two arguments, the first one is the path to the data, and the second one is the data file name.
It expects the data file to be sorted, since **no** ordering is done in the script. The datasets included in this replication package are all sorted based on issue creation date-time.
After reading the first column of the file (i.e., issueKey) to find the number of issues in the file, it starts dividing the issues in three sets with a rate of 60%-20%-20%.
Basically, the script produces a text file in `files/` directory inside the current directory (i.e., the directory of the script) with '\_3sets.txt' suffix (for example, MESOS_deep-se_3sets.txt).
This file will guide the preprocessing script to divide the data set.

**preprocess_storypoint.py**

This script receives three arguments, the first one is the path to the data, the second one is the project name (i.e., data file name), and the third onee is the repository name which is actually the name of the pre-training file. The third argument is optional.

The script reads the data file and looks for a file with the project name and '\_3sets.txt' suffix created in the previous step. If found, the file is used to split the dataset.
Then the `preprocess.py` script is used to tokenise the titles and the descriptions of the issues for each of the splits.
Finally all the chunks of the data are bundled together and stored as a single pickled file named '[project_name].pkl.gz' inside `files/` directory in the the current path.

**preprocess.py**

This script uses `tokenizer.perl` to tokenise the set of sentences. If tokeniser did not work, consider changing the tokeniser command at line 6: 

`tokenizer_cmd = ['/usr/bin/perl', 'tokenizer.perl', '-l', 'en', '-q', '-']`

The first argument of the command is the path to Perl installation directory, which needs to be corrected based on your OS and customised installations.
The `tokenizer.perl` script is included in the package in the current directory.

**preprocess_pretrain.py**

This script receives two arguments, the first is the path to the pre-training data, and the second is the data file name, which is the name of the repository.
After reading the file, it divides the issues in a 2-1 ratio, using two-third for training and one-third for validation purpose.
After tokenisation, it produces and stores inside `files/` directory in the current directory two files, one with `.pkl.gz` extension which contains the tokenised text for pre-training, and the other with `.dict.pkl.gz` extension which contains a dictionary build upon the pre-training text and used by `preprocess_storypoint.py`, in case pre-training used for Deep-SE.
