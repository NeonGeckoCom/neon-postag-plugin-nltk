import unittest
from quebra_frases import span_indexed_word_tokenize
from neon_postag_plugin_nltk import NltkPosTagger


class TestNltkPosTagger(unittest.TestCase):

    def test_postag(self):
        solver = NltkPosTagger()
        tokens = span_indexed_word_tokenize("Once upon a time there was a free and open voice assistant")
        self.assertEqual(solver.postag(tokens),
                         [('Once', 'ADV'),
                          ('upon', 'ADP'), # 'SCONJ'
                          ('a', 'DET'),
                          ('time', 'NOUN'),
                          ('there', 'DET'), # 'PRON'
                          ('was', 'VERB'), # 'AUX'
                          ('a', 'DET'),
                          ('free', 'ADJ'),
                          ('and', 'CONJ'),
                          ('open', 'ADJ'),
                          ('voice', 'NOUN'),
                          ('assistant', 'NOUN')])

