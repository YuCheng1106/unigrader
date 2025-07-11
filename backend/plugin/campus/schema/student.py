#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pydantic import ConfigDict, Field
from app.admin.schema.user import AddUserParam, UserInfoSchemaBase, GetUserInfoDetail
from common.schema import SchemaBase


class StudentSchemaBase(SchemaBase):
    """学生信息基础模型"""
    student_number: str | None = Field(default=None, description='学生学号')
    school_id: int = Field(default=None, description='学校 ID')


class AddStudentParam(AddUserParam, StudentSchemaBase):
    """添加学生参数"""
    pass


class UpdateStudentParam(StudentSchemaBase, UserInfoSchemaBase):
    pass


class GetStudentInfoDetail(GetUserInfoDetail, StudentSchemaBase):
    """学生信息详情"""
    user_id: int = Field(description='用户 ID')


class GetStudentInfoWithRelationDetail(GetStudentInfoDetail, StudentSchemaBase):
    """学生信息关联详情"""

    model_config = ConfigDict(from_attributes=True)


class GetCurrentStudentInfoWithRelationDetail(GetStudentInfoWithRelationDetail):
    """当前学生信息关联详情"""

    model_config = ConfigDict(from_attributes=True)
    pass

class CreateStudentParam(SchemaBase):
    """创建学生参数"""
    user_id: int = Field(description='用户 ID')
    student_number: str = Field(description='学生学号')
    school_id: int = Field(description='学校 ID')


class DeleteStudentParam(SchemaBase):
    """删除学生参数"""
    pks: list[int] = Field(description='学生 ID 列表')