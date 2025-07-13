#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import TEXT, String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column

from common.model import Base, id_key


class Banji(Base):
    """班级表"""

    __tablename__ = 'sys_banji'

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(50), comment='班级名称')
    remark: Mapped[str | None] = mapped_column(
        LONGTEXT().with_variant(TEXT, 'postgresql'), default=None, comment='备注'
    )