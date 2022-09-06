====================================================
webx: a program that monitors web sites and reports their availability. This tool is intended as a
monitoring tool for web site administrators for detecting problems on their sites.
====================================================


-------------------
Unit tests:
-------------------
>>> $pytest -v

>>> collected 3 items                                                                                                  
>>> unit/test_reachablity_response.py::test_reachability_response[item0] PASSED                                  [ 33%]
>>> unit/test_reachablity_response.py::test_reachability_response[item1] PASSED                                  [ 66%]
>>> unit/test_reachablity_response.py::test_not_reachability_response[item0] PASSED                              [100%]




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


In case you want to visualize and compare response latency, I have provided a small module yet not packaged it as a part of this solution.
The module is meant to demonstrate a sample to do simple visualization on a small scale data. In a production system
I recommend consolidating logs in a central location and indexing them in an OpenSearch cluster, and implementing a Kibana dashboard on top of it.  

To make the visualization work navigate to the  view/ directory, install the requirements.txt. Edit app.py and provide the path to the output of main webx tool,
then run 

python app.py 

 navigate to localhost and provided port to see the dash sahboard.

