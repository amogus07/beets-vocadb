from beetsplug.vocadb import VocaDBPlugin
from tests._abstract_test_plugin import AbstractTestVocaDBPlugin


class TestVocaDBPlugin(AbstractTestVocaDBPlugin):
    @property
    def plugin(cls):
        return VocaDBPlugin()
