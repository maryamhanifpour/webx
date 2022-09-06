#############
**webx** repository structure:
#############

====================================================
webx: a program that monitors web sites and reports their availability. This tool is intended as a
monitoring tool for web site administrators for detecting problems on their sites.

the list http websites to monitore should be provided in a config file.
Each site to monitore should have a unique key, the value of the key is the metadata used to monitore.
At the momen there is no config file schema validation implemented.

webx also measures response time in miliseconds. A note on response time:

Response time depends on network bandwidth and location of the server sending the request. These two factors are
ignored here. In reality one should measure response time from different geo location or regions and consolidate logs
in one datalake location. 

====================================================


*************
requirements and installation:
*************

**webx** uses python3, and there is a command line interface for it when installed.
To install **webx** it is recommended to create virtual environment first.


-------------------
Creating a Source Distribution and Wheel:
-------------------

python setup.py sdist bdist_wheel

-------------------
install the package:
-------------------

Create a python 3 virtual environment 

pip install dist/webx-0.0.1.tar.gz 

webx --ConfigFilePath  webConfigFile.json 

or to write result to /tmp folder

webx --ConfigFilePath  webConfigFile.json --logPath /tmp




*************
Unit tests:
*************

There is only one sample unit test to check if a site is not reachable the output is 'faile'
otherwise it is 'pass'
>>> $pytest -v

>>> collected 3 items                                                                                                  
>>> unit/test_reachablity_response.py::test_reachability_response[item0] PASSED                                  [ 33%]
>>> unit/test_reachablity_response.py::test_reachability_response[item1] PASSED                                  [ 66%]
>>> unit/test_reachablity_response.py::test_not_reachability_response[item0] PASSED                              [100%]


*************
visualization:
*************

In case you want to visualize and compare response latency, I have provided a small module yet not packaged it as a part of this solution.
The module is meant to demonstrate a sample to do simple visualization on a small scale data. In a production system
I recommend consolidating logs in a central location and indexing them in an OpenSearch cluster, and implementing a Kibana dashboard on top of it.  

To make the visualization work navigate to the  view/ directory, install the requirements.txt. Edit app.py and provide the path to the output of main webx tool,
then run 

python app.py 

 navigate to localhost and provided port to see the dash sahboard.

