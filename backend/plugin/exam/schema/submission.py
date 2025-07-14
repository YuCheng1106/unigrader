#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class SubmissionSchemaBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int = Field(..., description='对应的用户id')
    exam_id: int = Field(..., description='对应的考试id')
    start_time: datetime | None = Field(default=None, description='开始时间')
    end_time: datetime | None = Field(default=None, description='结束时间')
    total_score: float | None = Field(default=None, description='总分')
    status: Literal['not_started', 'in_progress', 'submitted', 'graded'] = Field(
        default='not_started', description='提交状态'
    )


class CreateSubmissionParam(SubmissionSchemaBase):
    """创建提交参数"""
    pass


class UpdateSubmissionParam(BaseModel):
    """更新提交参数"""
    model_config = ConfigDict(from_attributes=True)

    start_time: datetime | None = Field(default=None, description='开始时间')
    end_time: datetime | None = Field(default=None, description='结束时间')
    total_score: float | None = Field(default=None, description='总分')
    status: Literal['not_started', 'in_progress', 'submitted', 'graded'] | None = Field(
        default=None, description='提交状态'
    )


class DeleteSubmissionParam(BaseModel):
    """删除提交参数"""
    pks: list[int] = Field(..., description='提交ID列表')


class GetSubmissionDetail(SubmissionSchemaBase):
    """获取提交详情"""
    id: int = Field(..., description='提交ID')
    created_time: datetime = Field(..., description='创建时间')
    updated_time: datetime | None = Field(default=None, description='更新时间')