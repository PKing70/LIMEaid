import sys
sys.path.insert(0, '../LIMEaid/LIMEaid')
import version


def test_versionpy():
    """
    This is a test for version.py
    """
    # Get version and release info, which is all stored in LIMEaid/version.py
    version
    print('Testing now...')

    assert(1 == 1)
