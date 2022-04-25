import unittest
import sys
from pathlib import Path
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
print(sys.path)

from src.colorvector import get_palette

class TestGetPalette(unittest.TestCase):
    
    def test_get_palette(self):
        self.assertEqual(get_palette([0,0,0], [255,255,255], 3), [(0, 0, 0), (128, 128, 128), (255, 255, 255)])

unittest.main()

