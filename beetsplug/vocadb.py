import beets_vocadb.abstract_plugin
from beets_vocadb.instance_config import InstanceConfig

class VocaDBPlugin(
    beets_vocadb.abstract_plugin.AbstractVocaDBPlugin,
    instance_config=InstanceConfig(
        name="VocaDB",
        base_url="https://vocadb.net/",
        api_url="https://vocadb.net/api/",
        subcommand="vdbsync"
    )
):
    pass
