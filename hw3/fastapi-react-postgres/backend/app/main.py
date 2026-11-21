import os
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from pydantic import BaseModel, ConfigDict
from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker

DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)


class ItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as session:
        if not session.scalar(select(Item.id).limit(1)):
            session.add_all([Item(name="First item"), Item(name="Second item")])
            session.commit()
    yield
    engine.dispose()


app = FastAPI(title="FastAPI + React + PostgreSQL Demo", lifespan=lifespan)


def get_db():
    with SessionLocal() as session:
        yield session


@app.get("/api/items", response_model=list[ItemRead])
def get_items(db: Session = Depends(get_db)):
    return db.scalars(select(Item).order_by(Item.id)).all()

class ItemCreate(BaseModel):
    name: str


@app.post("/api/items", status_code=201)
def create_item(
    item: ItemCreate,
    db: Session = Depends(get_db),
):
    db_item = Item(name=item.name)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return {
        "id": db_item.id,
        "name": db_item.name,
    }