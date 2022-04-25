import unittest
import sys
from pathlib import Path
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
print(sys.path)

from src.colorvector import get_vector

class TestGetVector(unittest.TestCase):
    
    def test_get_vector(self):
        self.assertEqual(get_vector([0,0,0], [255,255,255]), (255, 255, 255))

unittest.main()

