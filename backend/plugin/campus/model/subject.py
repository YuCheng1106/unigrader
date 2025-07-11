#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from common.model import Base, id_key


class Subject(Base):
    """Subject/科目 information table"""

    __tablename__ = 'sys_subject'

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        comment='Subject name'
    )
    description: Mapped[Optional[str]] = mapped_column(
        Text,
        comment='Subject description'
    )
    deleted_at: Mapped[Optional[datetime]] = mapped_column(
        comment='Soft delete timestamp'
    )