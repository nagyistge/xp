import unittest
from flex.pipeline import get_pipeline, USE_FILE_PREFIX
import flex.pipeline as pipeline
import os, os.path

BASE_PATH = os.path.dirname(__file__)

def get_complete_filename(fname):
	return os.path.join(BASE_PATH,'pipelines',fname)

class BlockArgStringTestCase(unittest.TestCase):

	def test_basic1(self):
		p = get_pipeline(get_complete_filename('argstr_basic1'),
						default_prefix=USE_FILE_PREFIX)
		p.unmark_all_tasks()
		p.run()

		fname = get_complete_filename('argstr_basic1_a1.txt')

		self.assertTrue(os.path.exists(fname))
		os.remove(fname)

class AwkTestCase(unittest.TestCase):

	def test_awk1(self):
		p = get_pipeline(get_complete_filename('awk1'),
						default_prefix=USE_FILE_PREFIX)
		p.unmark_all_tasks()
		p.run()

		fname = get_complete_filename('awk1_out.txt')

		self.assertTrue(os.path.exists(fname))
		os.remove(fname)

class GnuplotTestCase(unittest.TestCase):
	
	def test_basic1(self):
		
		p = get_pipeline(get_complete_filename('gpl_basic1'),default_prefix=USE_FILE_PREFIX)
		p.unmark_all_tasks()
		p.run()

		self.assertTrue(os.path.exists(get_complete_filename('gpl_basic1_output1.png')))
		self.assertTrue(os.path.exists(get_complete_filename('output2.png')))

		os.remove(get_complete_filename('gpl_basic1_output1.png'))
		os.remove(get_complete_filename('output2.png'))

