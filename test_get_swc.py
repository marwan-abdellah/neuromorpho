#!/usr/bin/env python
from neuromorpho import *
import unittest

class TestGetSWCMethod(unittest.TestCase):
  def test_get_swc(self):
    get_swc_by_neuron_index(1)
    num_lines = sum(1 for line in open('cnic_001.CNG.swc'))
    self.assertTrue(num_lines == 1281, "SWC file incomplete")

if __name__ == '__main__':
    unittest.main()