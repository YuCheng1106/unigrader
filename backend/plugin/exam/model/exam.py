#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import TEXT, String, ForeignKey, BigInteger
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column

from common.model import Base, id_key


class Exam(Base):
    """测验表"""

    __tablename__ = 'sys_exam'

    id: Mapped[id_key] = mapped_column(init=False)
    name: Mapped[str] = mapped_column(String(50), comment='标题')
    subject: Mapped[str] = mapped_column(String(50), comment='标题')
    banji: Mapped[str] = mapped_column(String(255), comment='标题')
    creator_id: Mapped[int | None] = mapped_column(
        BigInteger, ForeignKey('sys_user.id', ondelete='SET NULL'), comment='创建者 ID'
    )
    status: Mapped[int] = mapped_column(comment='状态（0：隐藏、1：显示）')
    paper_file: Mapped[str | None] = mapped_column(String(255), default=None, comment='试卷文件链接')
    answer_file: Mapped[str | None] = mapped_column(String(255), default=None, comment='标答文件链接')
    answer_card: Mapped[str | None] = mapped_column(String(255), default=None, comment='答题卡对应链接')
    remark: Mapped[str | None] = mapped_column(
        LONGTEXT().with_variant(TEXT, 'postgresql'), default=None, comment='备注'
    )
