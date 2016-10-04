.. python-git-package documentation master file, created by python-git-package.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

python-git-package
==================

:Release:  |version|
:Date:  |today|

A scaffoling tool for python packages

Installation
------------
* run ``pip install python-git-package``


Users guide
-----------
This package can be used for scaffolding new packages.
The command ``pgp init`` creates a new package in the current folder.
The command ``pgp doc`` builds the docs using sphinx.
The command ``pgp release`` creates a new release.



Initializing a new package
^^^^^^^^^^^^^^^^^^^^^^^^^^
When running ``pgp init``, the uses is asked a series of questions on the details the new package (package name, license, author,...).
A new package layout is then created as follows:

.. code:: bash
    
    mypackage
     |-- .git
     |-- doc
     |    |--source
     |        |-- _static
     |        |-- _templates
     |        |-- conf.py
     |        |-- index.rst
     |        |-- mypackage.rst
     |
     |-- examples
     |-- mypackage
     |    |-- __init__.py
     |    |-- __version__.py
     |    |-- mypackage.py
     |
     |-- tests
     |    |-- all.py
     |    |-- test_mypackage.py
     |
     |-- .gitignore
     |-- LICENSE
     |-- MANIFEST.in
     |-- README.rst
     |-- setup.py

All files are populated with basic content so the notorious task of manually creating ``setup.py`` or ``manifest.in`` is taken out of the users task.

Furthermore, the init command initializes a git repository with two branches, ``master`` and ``dev`` in the package folder.
The ``master`` branch is intended for published releases only.
It should allwats point to the latest release.
The ``dev`` branch is used for develloping the package.

When the init command is invoked in a directory which allready has content, an attempt to get information from this content is made.


Building documentation
^^^^^^^^^^^^^^^^^^^^^^
The command ``pgp doc`` builds the documentation using sphinx.
The resulting html folder is also zipped to html.zip for easy upload to PyPi.


Preparing a release
^^^^^^^^^^^^^^^^^^^
To ease the process of creating a new release the command ``pgp release`` can be issued.
This command checks the current version of the package from the __version__.py file and asks for a new version (which must be higher than the old one).
The version file is updated to the new version and a release commit is automatically created in the current branch.
The current branch is then merged with the master branch and the commit is tagged using the version number.
If a ``doc`` folder is present, the docs are built.
Finally, the original branch is checked out.

The release is now ready to be pushed, or to create a distribution


Contents:

.. toctree::
   :maxdepth: 2

   python_git_package
   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

