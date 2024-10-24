from dataclasses import dataclass
from .entity import ENSEntity


@dataclass
class Notification(ENSEntity):
    id: int
    addresser_id: int
    addressee_id: int
    template: str
