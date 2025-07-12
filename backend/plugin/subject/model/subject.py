#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from common.model import Base, id_key


class Subject(Base):
    """学科模型"""

    __tablename__ = 'sys_subject'

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(255), comment='学科名称')
    remark: Mapped[str | None] = mapped_column(Text, default=None, comment='备注')