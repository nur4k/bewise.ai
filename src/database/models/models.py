# 1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса.

from sqlalchemy import Column, DateTime, String, Text, Integer

from src.database.base import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
