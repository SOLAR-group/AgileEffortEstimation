# Tawosi Dataset

This directory consists 46 files, two files per each of the 26-3\*=23 projects:
- 23 files with "\_deep-se" suffix are prepared to be used by Deep-SE.
- 23 files with "\_tfidf-se" suffix are prepared to be used by TF/IDF-SE.

\* <sub>One of the repositories including three projects has been removed from the public domain during the time that the manuscript for this study [1] was under revision. Therefore, although the paper reports the results for all 26 projects, the replication package includes 23 projects as we refrain from publishing the data for the three remaining projects in accordance with The General Data Protection Regulation.</sub> 

These 23 files are collected from 12 open source repositories by Tawosi et al. up until August, 2020.
The files named after their project key as "[project key]\_[approach].csv" e.g. MESOS_deep-se.csv, which is the set of issues collected from Appache repository Mesos project, and contains the features that Deep-SE needs for prediction. The following table shows the list of projects and the repositories where the project was collected from.   

## Project list

| Repository   | Project                           | Key        | File for Deep-SE          | File for TF/IDF-SE        |
|--------------|-----------------------------------|------------|---------------------------|---------------------------|
| Apache       | Mesos                             | MESOS      | MESOS_deeep-se.csv        | MESOS_tfidf-se.csv        |
| Apache       | Alloy                             | ALOY       | ALOY_deeep-se.csv         | ALOY_tfidf-se.csv         |
| Appcelerator | Appcelerator studio               | TISTUD     | TISTUD_deeep-se.csv       | TISTUD_tfidf-se.csv       |
| Appcelerator | Aptana studio                     | APSTUD     | APSTUD_deeep-se.csv       | APSTUD_tfidf-se.csv       |
| Appcelerator | Command-Line Interface            | CLI        | CLI_deeep-se.csv          | CLI_tfidf-se.csv          |
| Appcelerator | Daemon                            | DAEMON     | DAEMON_deeep-se.csv       | DAEMON_tfidf-se.csv       |
| Appcelerator | Documentation                     | TIDOC      | TIDOC_deeep-se.csv        | TIDOC_tfidf-se.csv        |
| Appcelerator | Titanium                          | TIMOB      | TIMOB_deeep-se.csv        | TIMOB_tfidf-se.csv        |
| Atlassian    | Clover                            | CLOV       | CLOV_deeep-se.csv         | CLOV_tfidf-se.csv         |
| Atlassian    | Confluence Cloud                  | CONFCLOUD  | CONFCLOUD_deeep-se.csv    | CONFCLOUD_tfidf-se.csv    |
| Atlassian    | Confluence Server and Data Center | CONFSERVER | CONFSERVER_deeep-se.csv   | CONFSERVER_tfidf-se.csv   |
| DNNSoftware  | DNN                               | DNN        | DNN_deeep-se.csv          | DNN_tfidf-se.csv          |
| Duraspace    | Duracloud                         | DURACLOUD  | DURACLOUD_deeep-se.csv    | DURACLOUD_tfidf-se.csv    |
| Hyperledger  | Fabric                            | FAB        | FAB_deeep-se.csv          | FAB_tfidf-se.csv          |
| Hyperledger  | Sawtooth                          | STL        | STL_deeep-se.csv          | STL_tfidf-se.csv          |
| Lsstcorp     | Data management                   | DM         | DM_deeep-se.csv           | DM_tfidf-se.csv           |
| MongoDB      | Compass                           | COMPASS    | COMPASS_deeep-se.csv      | COMPASS_tfidf-se.csv      |
| MongoDB      | Core Server                       | SERVER     | SERVER_deeep-se.csv       | SERVER_tfidf-se.csv       |
| MongoDB      | Evergreen                         | EVG        | EVG_deeep-se.csv          | EVG_tfidf-se.csv          |
| Moodle       | Moodle                            | MDL        | MDL_deeep-se.csv          | MDL_tfidf-se.csv          |
| Mulesoft     | Mule                              | MULE       | MULE_deeep-se.csv         | MULE_tfidf-se.csv         |
| Sonatype     | Sonatype’s Nexus                  | NEXUS      | NEXUS_deeep-se.csv        | NEXUS_tfidf-se.csv        |
| Spring       | Spring XD                         | XD         | XD_deeep-se.csv           | XD_tfidf-se.csv           |

## Content of the files 

- Each csv file for Deep-SE approach contains 4 columns: *issuekey*, *created*, *title*, *description*, and *storypoint*. 

- Each csv file for TF/IDF-SE approach contains more than 4 columns: starting with *issuekey*, *created*, *storypoint*, *context*, *codesnippet*, and a set of one-hot columns for issue type (header starting with t\_) followed by component(s) (header starting with c\_). 

- The issues are sorted based on issue's creation time (i.e. the former issues was created before the latter issues).

[1] Vali Tawosi, Rebecca Moussa, and Federica Sarro. "Agile Effort Estimation: Have We Solved the Problem Yet? Insights From A Replication Study." IEEE Transactions on Software Engineering, no. TBA (2022): pp. TBA.
