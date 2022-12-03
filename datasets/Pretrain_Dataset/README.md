# Pretrain Dataset

This directory consists 13-1\*=12 dataset files, one files per each repository.
The files named after their repository name as "[repository name].csv" e.g. Apache.csv, which is the set of up to 50,000 issues collected from Appache repository, regardless of their value of Story Point (i.e., the majority of the issues may have missing SP value). The title and description of these issues are used to pre-train a domain-based language model.

\* <sub>One of the repositories has been removed from the public domain, therefore, we refrain from publishing the source data for that repository in accordance with The General Data Protection Regulation. </sub>


The following table shows the list of projects and the repositories where the project was collected from.   

## Project list

| Repository   | File               |
|--------------|--------------------|
| Apache       | Apache.csv         |
| Appcelerator | Appcelerator.csv   |
| Atlassian    | Atlassian.csv      |
| DNNSoftware  | DNNSoftware.csv    |
| Duraspace    | Duraspace.csv      |
| Hyperledger  | Hyperledger.csv    |
| Lsstcorp	   | Lsstcorp.csv       |
| MongoDB      | MongoDB.csv        |
| Moodle       | Moodle.csv         |
| Mulesoft     | Mulesoft.csv       |
| Sonatype     | Sonatype.csv       |
| Spring       | Spring.csv         |


## Content of the files ##

- Each csv file for Deep-SE approach contains 4 columns: *issuekey*, *title*, *description*, and *storypoint*. 

- Each csv file for TF/IDF-SE approach contains more than 4 columns: starting with *issue key*, *storypoint*, *context*, *codesnippet*, and a set of one-hot columns for issue type (header starting with t\_) and then component(s) ((header starting with c\_)). 

- The issues are sorted based on issue's creation time (i.e. the former issues was created before the latter issues).







