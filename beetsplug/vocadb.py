import beets_vocadb.abstract_plugin
from beets_vocadb.instance_config import InstanceConfig

class VocaDBPlugin(beets_vocadb.abstract_plugin.AbstractVocaDBPlugin):
    @property
    def vocadb_config(cls):
        return InstanceConfig(
            name="VocaDB",
            base_url="https://vocadb.net/",
            api_url="https://vocadb.net/api/",
            subcommand="vdbsync"
        )
