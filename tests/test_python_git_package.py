#!/usr/bin/env/ python
################################################################################
#    Copyright 2016 Brecht Baeten
#    This file is part of python-git-package.
#    
#    python-git-package is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    
#    python-git-package is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    
#    You should have received a copy of the GNU General Public License
#    along with python-git-package.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

import unittest
import os
import shutil
import subprocess

import python_git_package


class TestPythonGitPackage(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()

    def make_dir(self):
        try:
            shutil.rmtree('test-package')
        except:
            pass
        os.mkdir('test-package')
        os.chdir('test-package')

    def remove_dir(self):
        try:
            os.chdir(self.cwd)
            shutil.rmtree('test-package')
        except:
            pass

    def test_version(self):
        self.assertGreater(len(python_git_package.__version__), 0)

    def test_init(self):
        self.make_dir()
        python_git_package.init()
        self.remove_dir()

    def test_doc(self):
        self.make_dir()
        python_git_package.init()
        python_git_package.doc()
        self.remove_dir()

    def test_release(self):
        self.make_dir()
        python_git_package.init()
        python_git_package.release()
        self.remove_dir()


if __name__ == '__main__':
    unittest.main()
