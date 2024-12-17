import beets_vocadb.abstract_plugin
from beets_vocadb.instance_config import InstanceConfig

class TouhouDBPlugin(
    beets_vocadb.abstract_plugin.AbstractVocaDBPlugin,
    instance_config=InstanceConfig(
        name="TouhouDB",
        base_url="https://touhoudb.com/",
        api_url="https://touhoudb.com/api/",
        subcommand="tdbsync",
    )
):
    pass
