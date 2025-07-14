#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import DateTime, Float, Integer, String, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from common.model import Base, id_key


class Submission(Base):
    """提交表"""

    __tablename__ = 'submission'

    id: Mapped[id_key] = mapped_column(init=False)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('sys_user.id'), nullable=False, comment='对应的用户id')
    exam_id: Mapped[int] = mapped_column(Integer, ForeignKey('exam.id'), nullable=False, comment='对应的考试id')
    start_time: Mapped[datetime | None] = mapped_column(DateTime, default=None, comment='开始时间')
    end_time: Mapped[datetime | None] = mapped_column(DateTime, default=None, comment='结束时间')
    total_score: Mapped[float | None] = mapped_column(Float, default=None, comment='总分')
    status: Mapped[str] = mapped_column(
        Enum('not_started', 'in_progress', 'submitted', 'graded', name='submission_status_enum'),
        default='not_started',
        nullable=False,
        comment='提交状态'
    )

    __table_args__ = (
        UniqueConstraint('user_id', 'exam_id', name='uq_user_exam'),
    )