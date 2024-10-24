from dataclasses import dataclass
from .entity import ENSEntity


@dataclass
class User(ENSEntity):
    id: int|None
    first_name: str
    last_name: str|None
    contacts: dict
