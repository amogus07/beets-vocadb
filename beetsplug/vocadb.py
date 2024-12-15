from beets.plugins import BeetsPlugin
from beetsplug.vocadb_template import get_vocadb_plugin

class VocaDBPlugin(
    get_vocadb_plugin(
        name="VocaDB",
        base_url="https://vocadb.net/",
        api_url="https://vocadb.net/api/",
        subcommand="vdbsync",
    )
):
    pass
