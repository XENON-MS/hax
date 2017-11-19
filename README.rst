hax - Handy Analysis tools for XENON
====================================

Documentation (newer): `http://hax.readthedocs.org/en/latest/`

Tools for common analysis tasks on pax processed data, such as:

* Finding datasets of a particular source / type in the XENON1T runs database [PLANNED]
* Looping over every event in one or more root files
* Make and load 'mini-trees' containing reduced data (e.g. cut booleans, or basic extracted data)
* Load a big TChain containing the main trees and mini-trees for several datasets [Experimental]


Installation
============
You probably want to run this library in an analysis facility (Xecluster/Stockholm/Chicago).

Setup as usual by running 'python setup.py develop' or, if you want to hide the code, 'python setup.py install'.

Pax, pyROOT and root_numpy are prerequisites: follow the usual pax installation procedure, then do `conda install root_numpy`.
