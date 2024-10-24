from typing import Protocol
from .entities import User, Notification


class NotificatorProtocol(Protocol):
    async def __call__(self, addresser: User, notifications: list[Notification]): ...
