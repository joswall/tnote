"""Main test class for tnote"""

import os
import json
import datetime

import tnote.tnote as tn

def setup():
	"""TODO"""

def testProcessTags():
	assert "a,b,cee,test tag" == tn.processTags("a,a, a , b , cee, test tag")

def cleanup():
	"""TODO"""

setup()
testProcessTags()
cleanup()
