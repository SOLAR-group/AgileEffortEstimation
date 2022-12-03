# Choet Dataset

This directory consists 14 csv files from 16-2\*=14 projects collected from 9-1\*=8 open source repositories by Choetkiertikul et al. [1] up until August, 2016. The files named after their project key as "[project key]\_[approach].csv" e.g. MESOS_deep-se.csv, which is the set of issues collected from Appache repository Mesos project, and contains the features that Deep-SE needs for prediction.

\* <sub>One of the repositories including two projects has been removed from the public domain, therefore, we refrain from publishing the source data for these two projects in accordance with The General Data Protection Regulation. </sub>

The following table shows the list of projects and the repositories where the project was collected from.   

## Project list

| Repository   | Project                    | Key        | File                   |
|--------------|----------------------------|------------| -----------------------|
| Apache       | Mesos                      | MESOS      | MESOS_deep-se.csv      |
| Apache       | Usergrid                   | USERGRID   | USERGRID_deep-se.csv   |
| Appcelerator | Appcelerator studio        | TISTUD     | TISTUD_deep-se.csv     |
| Appcelerator | Aptana studio              | APSTUD     | APSTUD_deep-se.csv     |
| Appcelerator | Titanium                   | TIMOB      | TIMOB_deep-se.csv      |
| Atlassian    | Bamboo                     | BAM        | BAM_deep-se.csv        |
| Atlassian    | Clover                     | CLOV       | CLOV_deep-se.csv       |
| Atlassian    | Jira Server and Data Center| JRESERVER  | JRESERVER_deep-se.csv  |
| Duraspace    | Duracloud                  | DURACLOUD  | DURACLOUD_deep-se.csv  |
| Lsstcorp     | Data management            | DM         | DM_deep-se.csv         |
| Moodle       | Moodle                     | MDL        | MDL_deep-se.csv        |
| Mulesoft     | Mule                       | MULE       | MULE_deep-se.csv       |
| Mulesoft     | Mule studio                | MULESTUDIO | MULESTUDIO_deep-se.csv |
| Spring       | Spring XD                  | XD         | XD_deep-se.csv         |

## Content of the files

Each csv file contains 4 columns: issue key, title, description, and story point. The issues are sorted based on issue's creation time (i.e. the former issues was created before the latter issues).


[1] Choetkiertikul, Morakot, Hoa Khanh Dam, Truyen Tran, Trang Pham, Aditya Ghose, and Tim Menzies. "A deep learning model for estimating story points." IEEE Transactions on Software Engineering 45, no. 7 (2018): 637-656.

