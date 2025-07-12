#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

from pydantic import ConfigDict, Field

from common.enums import StatusType
from common.schema import SchemaBase


class ExamSchemaBase(SchemaBase):
    """测验基础模型"""

    name: str = Field(description='标题')
    remark: str | None = Field(None, description='信息来源')
    subject: str = Field(description='所属学科')
    banji: str = Field(description='所属班级')
    status: StatusType = Field(StatusType.enable.value, description='状态（0：隐藏、1：显示）')
    paper_file: str | None = Field(None, description='试卷文件')
    answer_file: str | None = Field(None, description='试卷标答')

class CreateExamParam(ExamSchemaBase):
    """创建测验参数"""
    creator_id: int = Field(description='创建者 ID')


class UpdateExamParam(ExamSchemaBase):
    """更新测验参数"""


class DeleteExamParam(SchemaBase):
    """删除测验参数"""

    pks: list[int] = Field(description='测验 ID 列表')


class GetExamDetail(ExamSchemaBase):
    """测验详情"""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description='测验 ID')
    created_time: datetime = Field(description='创建时间')
    updated_time: datetime | None = Field(None, description='更新时间')
