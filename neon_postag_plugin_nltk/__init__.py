from ovos_plugin_manager.postag import PosTagger

from nltk import pos_tag


class NltkPosTagger(PosTagger):
    def __init__(self, config=None):
        super().__init__(config)
        # TODO allow defining your own model
        # see https://github.com/NeonJarbas/modelhub/tree/models/models/nltk

    def postag(self, spans, lang=None):
        lang = lang or self.lang
        # TODO need 3 lang code
        # return pos_tag(tokens, tagset="universal", lang=lang)
        tokens = [t for (s, e, t) in spans]
        return pos_tag(tokens, tagset="universal")
