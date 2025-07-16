#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import TEXT, Float, Integer, String, JSON, Enum, BigInteger
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from common.model import Base, id_key


class ExamQuestion(Base):
    """考试题目表"""

    __tablename__ = 'exam_question'

    id: Mapped[id_key] = mapped_column(init=False)
    exam_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('sys_exam.id'), nullable=False, comment='对应的exam的id')
    question_type: Mapped[str] = mapped_column(
        Enum('single_choice', 'multiple_choice', 'true_false', 'short_answer', 'essay', name='question_type_enum'),
        nullable=False,
        comment='题目的类型'
    )
    question_content: Mapped[str] = mapped_column(
        LONGTEXT().with_variant(TEXT, 'postgresql'), 
        nullable=False, 
        comment='题目的内容'
    )
    points: Mapped[float] = mapped_column(Float, nullable=False, comment='题目的分数')
    sequence: Mapped[int] = mapped_column(Integer, nullable=False, comment='题目的序号')
    options: Mapped[dict | None] = mapped_column(
        JSON, 
        default=None, 
        comment='For multiple choice questions'
    )
    correct_answer: Mapped[str | None] = mapped_column(
        LONGTEXT().with_variant(TEXT, 'postgresql'), 
        default=None, 
        comment='题目的正确答案'
    )