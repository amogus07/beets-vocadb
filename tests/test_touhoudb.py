from beetsplug.touhoudb import TouhouDBPlugin
from tests._abstract_test_plugin import AbstractTestVocaDBPlugin


class TestTouhouDBPlugin(AbstractTestVocaDBPlugin):
    @property
    def plugin(cls):
        return TouhouDBPlugin()
