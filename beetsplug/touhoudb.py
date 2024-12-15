from beets.plugins import BeetsPlugin
from beetsplug.vocadb_template import get_vocadb_plugin

class TouhouDBPlugin(
    get_vocadb_plugin(
        name="TouhouDB",
        base_url="https://touhoudb.com/",
        api_url="https://touhoudb.com/api/",
        subcommand="tdbsync",
    )
):
    pass
