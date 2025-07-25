#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import TYPE_CHECKING

from sqlalchemy import TEXT, String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common.model import Base, id_key
from plugin.exam.model.m2m import sys_user_banji

if TYPE_CHECKING:
    from app.admin.model import User
    from plugin.exam.model.exam import Exam


class Banji(Base):
    """班级表"""

    __tablename__ = 'sys_banji'

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(50), comment='班级名称')
    remark: Mapped[str | None] = mapped_column(
        LONGTEXT().with_variant(TEXT, 'postgresql'), default=None, comment='备注'
    )
    
    # 班级用户多对多
    users: Mapped[list[User]] = relationship(init=False, secondary=sys_user_banji, back_populates='banjis')