#from codebase.model import getcollegedatasets as gcd


def test_basic_pass():
	"""
	This is a basic pass test case scenario to make sure coverage banner works
	"""
	assert(1==1)
		
def test_getmostrecentcohorts():
	"""
	This is a placeholder to test get most recent cohorts dataset
	"""
	scorecard = gcd.getmostrecentcohorts()
	assert(1<=scorecard.shape[0])

def test_getsalariesbyregion():
	"""
	This is a placeholder to test get most recent cohorts dataset
	"""
	salaries = gcd.getsalariesbyregion()
	assert(1<=salaries.shape[0])
