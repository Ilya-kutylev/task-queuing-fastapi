from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config import settings

# create async engine for interaction with database
engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)

# create async session for interaction with database
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
