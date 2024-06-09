from .model import async_session
from .model import User
from sqlalchemy import select


async def check_user(tg):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.id == tg))
        return user


async def new_user(tg, number):
    async with async_session() as session:
        session.add(User(tg=tg, number=number))
        await session.commit()
