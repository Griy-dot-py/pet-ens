from .database import DatabaseProtocol
from .notificator import NotificatorProtocol
from .entities import User, Notification


class ENS:
    def __init__(self, db: DatabaseProtocol, notificator: NotificatorProtocol):
        self.__db = db
        self.__notificator = notificator
    
    async def add_user(self, user: User) -> int:
        id = await self.__db.create(user)
        return id
        
    async def set_notification(self, notification: Notification) -> int:
        id = await self.__db.create(notification)
        return id
    
    async def notify_all(self, user_id: int) -> int:
        user = await self.__db.get_user(user_id)
        notifications = await self.__db.select_notifications(user_id)
        await self.__notificator(user, notifications)
