#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common.model import Base, id_key

if TYPE_CHECKING:
    from plugin.dict.model import DictType


class DictData(Base):
    """字典数据表"""

    __tablename__ = 'sys_dict_data'

    id: Mapped[id_key] = mapped_column(init=False)
    type_code: Mapped[str] = mapped_column(String(32), comment='对应的字典类型编码')
    label: Mapped[str] = mapped_column(String(32), comment='字典标签')
    value: Mapped[str] = mapped_column(String(32), comment='字典值')
    sort: Mapped[int] = mapped_column(default=0, comment='排序')
    status: Mapped[int] = mapped_column(default=1, comment='状态（0停用 1正常）')
    remark: Mapped[str | None] = mapped_column(
        LONGTEXT().with_variant(TEXT, 'postgresql'), default=None, comment='备注'
    )

    # 字典类型一对多
    type_id: Mapped[int] = mapped_column(
        ForeignKey('sys_dict_type.id', ondelete='CASCADE'), default=0, comment='字典类型关联ID'
    )
    type: Mapped[DictType] = relationship(init=False, back_populates='datas')
