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

import python_git_package

class TestPython_Git_Package(unittest.TestCase):

    def test_version(self):
        self.assertGreater( len(python_git_package.__version__), 0 )

if __name__ == '__main__':
    unittest.main()
