#!/usr/bin/env python

# Run in terminal by executing `./runTests.py`
# If won't execute in Terminal, execute `chmod +x runTests.py` first.

import unittest

loader = unittest.TestLoader()
tests = loader.discover('tests/')
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)