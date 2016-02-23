#!/usr/bin/env python

import sys
sys.path = [ "src" ] + sys.path
import unittest

from pyocr import cuneiform
from pyocr import pyocr
from pyocr import tesseract_sh

from tests import tests_cuneiform
from tests import tests_tesseract

if __name__ == '__main__':
    for tool in pyocr.TOOLS:
        print("- OCR: %s" % tool.get_name())
        available = tool.is_available()
        print("  is_available(): %s" % (str(available)))
        if available:
            print("  get_version(): %s" % (str(tool.get_version())))
            print("  get_available_languages(): ")
            print("    " + ", ".join(tool.get_available_languages()))
        print("")
    print("")

    print("OCR tool found:")
    for tool in pyocr.get_available_tools():
        print("- %s" % tool.get_name())
    if tesseract_sh.is_available():
        print("---")
        print("Tesseract:")
        unittest.TextTestRunner().run(tests_tesseract.get_all_tests())
    if cuneiform.is_available():
        print("---")
        print("Cuneiform:")
        unittest.TextTestRunner().run(tests_cuneiform.get_all_tests())

