#import sys, os
#sys.path.append(os.getcwd())
import os


def test_versionpy():
	"""
	This is a test for version.py
	"""
	# Get version and release info, which is all stored in LIMEaid/version.py
	ver_file = os.path.join('LIMEaid', 'version.py')

	with open(ver_file) as f:
		exec(f.read())

	assert(1==1)
