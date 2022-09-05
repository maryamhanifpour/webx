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