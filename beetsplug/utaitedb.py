from beets.plugins import BeetsPlugin
from beetsplug.vocadb_template import get_vocadb_plugin

class UtaiteDBPlugin(
    get_vocadb_plugin(
        name="UtaiteDB",
        base_url="https://utaiteadb.net/",
        api_url="https://utaitedb.net/api/",
        subcommand="udbsync",
    )
):
    pass
