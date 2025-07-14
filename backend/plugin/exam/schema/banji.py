#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime

from pydantic import ConfigDict, Field

from common.schema import SchemaBase


class BanjiSchemaBase(SchemaBase):
    """班级基础模型"""

    name: str = Field(description='班级名称')
    remark: str | None = Field(None, description='备注')


class CreateBanjiParam(BanjiSchemaBase):
    """创建班级参数"""
    pass


class UpdateBanjiParam(BanjiSchemaBase):
    """更新班级参数"""
    pass


class DeleteBanjiParam(SchemaBase):
    """删除班级参数"""

    pks: list[int] = Field(description='班级 ID 列表')


class GetBanjiDetail(BanjiSchemaBase):
    """班级详情"""

    model_config = ConfigDict(from_attributes=True)

    id: int = Field(description='班级 ID')
    created_time: datetime = Field(description='创建时间')
    updated_time: datetime | None = Field(None, description='更新时间')