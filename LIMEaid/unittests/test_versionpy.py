#import sys, os
#sys.path.append(os.getcwd())
from LIMEaid.LIMEaid import version

def test_versionpy():
	"""
	This is a test for version.py
	"""
	# Get version and release info, which is all stored in LIMEaid/version.py
	version

	assert(1==1)
