#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from common.model import Base, id_key


class School(Base):
    """School information table"""

    __tablename__ = 'sys_school'

    id: Mapped[id_key] = mapped_column(init=False)
    uuid: Mapped[str] = mapped_column(
        String(24),
        unique=True,
        nullable=False,
        comment='Unique identifier for the school'
    )
    name: Mapped[str] = mapped_column(
        String(225),
        nullable=False,
        comment='School name'
    )
    description: Mapped[Optional[str]] = mapped_column(
        Text,
        comment='School description'
    )
    deleted_at: Mapped[Optional[datetime]] = mapped_column(
        comment='Soft delete timestamp'
    )