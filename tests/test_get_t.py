import unittest
import sys
from pathlib import Path
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
print(sys.path)

from src.colorvector import get_t

class TestGetT(unittest.TestCase):
    
    def test_get_t(self):
        self.assertEqual(get_t(3), [0,.5,1])

unittest.main()

