#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class SubmissionAnswerSchemaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int = Field(..., description='对应的用户id')
    exam_id: int = Field(..., description='对应的考试id')
    submission_id: int = Field(..., description='对应的提交id')
    exam_question_id: int = Field(..., description='对应的考试题目id')
    answer_content: str = Field(..., description='答案的内容')
    is_correct: bool | None = Field(default=None, description='答案是否正确')
    score: float | None = Field(default=None, description='答案获得的分数')
    feedback: str | None = Field(default=None, description='老师的批语')
    graded_by_id: int | None = Field(default=None, description='被谁批改的用户id')
    submitted_at: datetime = Field(..., description='提交的答案的时间')
    graded_at: datetime | None = Field(default=None, description='批改的时间')


class CreateSubmissionAnswerParam(SubmissionAnswerSchemaBase):
    """创建提交答案参数"""
    pass


class UpdateSubmissionAnswerParam(BaseModel):
    """更新提交答案参数"""
    model_config = ConfigDict(from_attributes=True)

    answer_content: str | None = Field(default=None, description='答案的内容')
    is_correct: bool | None = Field(default=None, description='答案是否正确')
    score: float | None = Field(default=None, description='答案获得的分数')
    feedback: str | None = Field(default=None, description='老师的批语')
    graded_by_id: int | None = Field(default=None, description='被谁批改的用户id')
    submitted_at: datetime | None = Field(default=None, description='提交的答案的时间')
    graded_at: datetime | None = Field(default=None, description='批改的时间')


class DeleteSubmissionAnswerParam(BaseModel):
    """删除提交答案参数"""
    pks: list[int] = Field(..., description='提交答案ID列表')


class GetSubmissionAnswerDetail(SubmissionAnswerSchemaBase):
    """获取提交答案详情"""
    id: int = Field(..., description='提交答案ID')
    created_time: datetime = Field(..., description='创建时间')
    updated_time: datetime | None = Field(default=None, description='更新时间')