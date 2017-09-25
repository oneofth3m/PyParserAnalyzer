from __future__ import absolute_import
from py.GenerateComponents import GenerateComponents

import unittest

class TestGenerateComponents(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(TestGenerateComponents, self).__init__(*args, **kwargs)
    self.generate_components = GenerateComponents()

  def test_one(self):
    self.assertEqual(self.generate_components.one, 1)
