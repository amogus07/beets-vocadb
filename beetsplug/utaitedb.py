import beets_vocadb.abstract_plugin
from beets_vocadb.instance_config import InstanceConfig

class UtaiteDBPlugin(beets_vocadb.abstract_plugin.AbstractVocaDBPlugin):
    @property
    def vocadb_config(cls):
        return InstanceConfig(
            name="UtaiteDB",
            base_url="https://utaiteadb.net/",
            api_url="https://utaitedb.net/api/",
            subcommand="udbsync",
        )
