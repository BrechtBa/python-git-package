import unittest

import {packagename}

class Test{packagename_caps}(unittest.TestCase):

    def test_version(self):
        self.assertGreater( len({packagename}.__version__), 0 )

if __name__ == '__main__':
    unittest.main()
