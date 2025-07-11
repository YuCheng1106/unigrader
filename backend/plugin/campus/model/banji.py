#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from common.model import Base, id_key


class Banji(Base):
    """Class/班级 information table"""

    __tablename__ = 'sys_banji'

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        comment='Class name'
    )
    academic_year: Mapped[Optional[str]] = mapped_column(
        String(20),
        comment='Academic year the class belongs to'
    )
    description: Mapped[Optional[str]] = mapped_column(
        Text,
        comment='Class description'
    )
    deleted_at: Mapped[Optional[datetime]] = mapped_column(
        comment='Soft delete timestamp'
    )