#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import DateTime, Float, Integer, String, Boolean, Text, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from common.model import Base, id_key


class SubmissionAnswer(Base):
    """提交答案表"""

    __tablename__ = 'submission_answer'

    id: Mapped[id_key] = mapped_column(init=False)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('sys_user.id'), nullable=False, comment='对应的用户id')
    exam_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('sys_exam.id'), nullable=False, comment='对应的考试id')
    submission_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('submission.id'), nullable=False, comment='对应的提交id')
    exam_question_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('exam_question.id'), nullable=False, comment='对应的考试题目id')
    answer_content: Mapped[str] = mapped_column(Text, nullable=False, comment='答案的内容')
    submitted_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, comment='提交的答案的时间')
    is_correct: Mapped[bool | None] = mapped_column(Boolean, default=None, comment='答案是否正确')
    score: Mapped[float | None] = mapped_column(Float, default=None, comment='答案获得的分数')
    feedback: Mapped[str | None] = mapped_column(Text, default=None, comment='老师的批语')
    graded_by_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey('sys_user.id'), default=None, comment='被谁批改的用户id')
    graded_at: Mapped[datetime | None] = mapped_column(DateTime, default=None, comment='批改的时间')