# Porru Dataset

This directory consists 16 dataset files, two files per each of the 26 projects:
- 8 files with "\_deep-se" suffix are prepared to be used by Deep-SE.
- 8 files with "\_tfidf-se" suffix are prepared to be used by TF/IDF-SE.

These 8 files are collected from 6 open source repositories by Choetkiertikul et al. [1] up until August, 2016.
The files named after their project key as "[project key]\_[approach].csv" e.g. MESOS_deep-se.csv, which is the set of issues collected from Appache repository Mesos project, and contains the features that Deep-SE needs for prediction. 

The following table shows the list of projects and the repositories where the project was collected from.   

Project list

| Repository   | Project                           | Key        | File for Deep-SE          | File for TF/IDF-SE        |
|--------------|-----------------------------------|------------|---------------------------|---------------------------|
| Apache       | Mesos                             | MESOS      | MESOS_deeep-se.csv        | MESOS_tfidf-se.csv        |
| Appcelerator | Appcelerator studio               | TISTUD     | TISTUD_deeep-se.csv       | TISTUD_tfidf-se.csv       |
| Appcelerator | Aptana studio                     | APSTUD     | APSTUD_deeep-se.csv       | APSTUD_tfidf-se.csv       |
| Appcelerator | Titanium                          | TIMOB      | TIMOB_deeep-se.csv        | TIMOB_tfidf-se.csv        |
| DNNSoftware  | DNN                               | DNN        | DNN_deeep-se.csv          | DNN_tfidf-se.csv          |
| Mulesoft     | Mule                              | MULE       | MULE_deeep-se.csv         | MULE_tfidf-se.csv         |
| Sonatype     | Sonatype’s Nexus                  | NEXUS      | NEXUS_deeep-se.csv        | NEXUS_tfidf-se.csv        |
| Spring       | Spring XD                         | XD         | XD_deeep-se.csv           | XD_tfidf-se.csv           |

## Information on the content of the files ##

- Each csv file for Deep-SE approach contains 4 columns: *issuekey*, *title*, *description*, and *storypoint*. 

- Each csv file for TF/IDF-SE approach contains more than 4 columns: starting with *issue key*, *storypoint*, *context*, *codesnippet*, and a set of one-hot columns for issue type (header starting with t\_) and then component(s) ((header starting with c\_)). 

- The issues are sorted based on issue's creation time (i.e. the former issues was created before the latter issues).

[1] Choetkiertikul, Morakot, Hoa Khanh Dam, Truyen Tran, Trang Pham, Aditya Ghose, and Tim Menzies. "A deep learning model for estimating story points." IEEE Transactions on Software Engineering 45, no. 7 (2018): 637-656.






