#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common.model import Base, id_key

if TYPE_CHECKING:
    from app.admin.model import User


class Subject(Base):
    """学科模型"""

    __tablename__ = 'sys_subject'

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(255), comment='学科名称')
    remark: Mapped[str | None] = mapped_column(Text, default=None, comment='备注')

    # 多对多关系
    teachers: Mapped[list[User]] = relationship(
        init=False, secondary='teacher_subject', back_populates='teaching_subjects'
    )