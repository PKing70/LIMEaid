import sys
sys.path.insert(0, '../controller')
import version


def test_versionpy():
    """
    This is a test for version.py
    """
    # Get version and release info, which is all stored in LIMEaid/version.py
    version

    assert(1 == 1)
