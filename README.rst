====================================================
webx: a program that monitors web sites and reports their availability. This tool is intended as a
monitoring tool for web site administrators for detecting problems on their sites.
====================================================


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