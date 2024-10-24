from typing import Protocol
from .entities import ENSEntity, Notification, User


class DatabaseProtocol(Protocol):
    async def create(self, entity: ENSEntity) -> int: ...
    
    async def select_notifications(self, addresser_id: int) -> list[Notification]: ...
    
    async def get_user(self, id: int) -> User: ...
