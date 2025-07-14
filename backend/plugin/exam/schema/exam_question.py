#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Dict, Any

from pydantic import ConfigDict, Field

from common.schema import SchemaBase


class ExamQuestionSchemaBase(SchemaBase):
    """考试题目基础模型"""

    exam_id: int = Field(description='对应的exam的id')
    question_type: str = Field(description='题目的类型')
    question_content: str = Field(description='题目的内容')
    options: Dict[str, Any] | None = Field(None, description='For multiple choice questions')
    correct_answer: str | None = Field(None, description='题目的正确答案')
    points: float = Field(description='题目的分数')
    sequence: int = Field(description='题目的序号')


class CreateExamQuestionParam(ExamQuestionSchemaBase):
    """创建考试题目参数"""
    pass


class UpdateExamQuestionParam(ExamQuestionSchemaBase):
    """更新考试题目参数"""
    pass


class DeleteExamQuestionParam(SchemaBase):
    """删除考试题目参数"""

    pks: list[int] = Field(description='考试题目 ID 列表')


class GetExamQuestionDetail(ExamQuestionSchemaBase):
    """考试题目详情"""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description='考试题目 ID')
    created_time: datetime = Field(description='创建时间')
    updated_time: datetime | None = Field(None, description='更新时间')