from beetsplug.utaitedb import UtaiteDBPlugin
from tests._abstract_test_plugin import AbstractTestVocaDBPlugin


class TestUtaiteDBPlugin(AbstractTestVocaDBPlugin):
    @property
    def plugin(cls):
        return UtaiteDBPlugin()
