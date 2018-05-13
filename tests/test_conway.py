from .context import conway
from conway import Molecule
import unittest

class MoleculeTester(unittest.TestCase):

    def setUp(self):
        self.molecule = Molecule()

    def test_neighbours(self):

        assert 2 <= len(self.molecule.neighbours) <= 3
