#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import TYPE_CHECKING, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common.model import Base

if TYPE_CHECKING:
    from app.admin.model import User


class Student(Base):
    """student information table"""

    __tablename__ = 'sys_student'

    user_id: Mapped[int] = mapped_column(
        ForeignKey('sys_user.id', ondelete='CASCADE'),
        primary_key=True
    )
    school_id: Mapped[int] = mapped_column(
        ForeignKey('sys_school.id', ondelete='CASCADE'), primary_key=True
    )

    student_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        comment='student identification number'
    )

    # Relationship with User
    user: Mapped[Optional['User']] = relationship(init=False)