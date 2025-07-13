#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pydantic import ConfigDict, Field

from common.schema import SchemaBase


class SubjectSchemaBase(SchemaBase):
    """学科基础模式"""

    name: str = Field(..., description='学科名称')
    remark: str | None = Field(None, description='备注')


class CreateSubjectParam(SubjectSchemaBase):
    """创建学科参数"""

    pass


class UpdateSubjectParam(SubjectSchemaBase):
    """更新学科参数"""

    pass


class DeleteSubjectParam(SchemaBase):
    """删除学科参数"""

    ids: list[int] = Field(..., description='学科 ID 列表')


class GetSubjectDetail(SubjectSchemaBase):
    """获取学科详情"""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., description='学科 ID')