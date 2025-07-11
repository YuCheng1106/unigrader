#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common.model import Base, id_key

if TYPE_CHECKING:
    from app.admin.model import User


class Teacher(Base):
    """Teacher information table"""

    __tablename__ = 'sys_teacher'

    user_id: Mapped[int] = mapped_column(
        ForeignKey('sys_user.id', ondelete='CASCADE'),
        primary_key=True
    )
    school_id: Mapped[int] = mapped_column(
        ForeignKey('sys_school.id', ondelete='CASCADE')
    )
    teacher_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        comment='Teacher identification number'
    )
    hire_date: Mapped[Date] = mapped_column(
        Date,
        nullable=True,
        comment='Date when the teacher was hired'
    )

    # Relationship with User
    user: Mapped['User'] = relationship()