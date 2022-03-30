import unittest

from neon_postag_plugin_nltk import NltkPosTagger


class TestNltkPosTagger(unittest.TestCase):

    def test_postag(self):
        solver = NltkPosTagger()
        tokens = "Once upon a time there was a free and open voice assistant".split()
        self.assertEqual(solver.postag(tokens),
                         [('Once', 'ADV'),
                          ('upon', 'ADP'),
                          ('a', 'DET'),
                          ('time', 'NOUN'),
                          ('there', 'DET'),
                          ('was', 'VERB'),
                          ('a', 'DET'),
                          ('free', 'ADJ'),
                          ('and', 'CONJ'),
                          ('open', 'ADJ'),
                          ('voice', 'NOUN'),
                          ('assistant', 'NOUN')])

