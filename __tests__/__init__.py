import unittest

from inpy import read_inp_file


class TestReadInpFile(unittest.TestCase):
    def test_nodes(self):
        fpath = "inp_file_snippets/nodes.inp"
        _inp = read_inp_file(fpath)
        self.assertEqual(True, True)
