import beets_vocadb.abstract_plugin
from beets_vocadb.instance_config import InstanceConfig

class TouhouDBPlugin(beets_vocadb.abstract_plugin.AbstractVocaDBPlugin):
    @property
    def vocadb_config(cls):
        return InstanceConfig(
        name="TouhouDB",
        base_url="https://touhoudb.com/",
        api_url="https://touhoudb.com/api/",
        subcommand="tdbsync",
    )
