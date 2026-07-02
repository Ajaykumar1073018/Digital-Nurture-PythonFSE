from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

# SQLite async URL
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./courses.db"

# Create the async engine and session factory
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

# Dependency function to inject DB sessions into our endpoints
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session