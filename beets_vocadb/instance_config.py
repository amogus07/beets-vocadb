from typing import NamedTuple

class InstanceConfig(NamedTuple):
    name: str
    base_url: str
    api_url: str
    subcommand: str
