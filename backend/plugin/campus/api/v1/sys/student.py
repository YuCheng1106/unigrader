#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Annotated

from fastapi import APIRouter, Depends, Path, Request

from app.admin.schema.user import AddUserParam, GetUserInfoWithRelationDetail
from app.admin.service.user_service import user_service
from common.exception import errors
from common.pagination import DependsPagination, PageData, paging_data
from common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base
from common.security.jwt import DependsJwtAuth
from common.security.permission import RequestPermission
from common.security.rbac import DependsRBAC
from database.db import CurrentSession
from plugin.campus.schema.student import DeleteStudentParam, GetStudentInfoWithRelationDetail, \
    UpdateStudentParam, AddStudentParam, CreateStudentParam
from plugin.campus.service.student_service import student_service
from plugin.campus.utils.generate_student_number import generate_student_id

router = APIRouter()


@router.get('/{pk}', summary='获取学生信息详情', dependencies=[DependsJwtAuth])
async def get_student(pk: Annotated[int, Path(description='学生信息 ID')]) -> ResponseSchemaModel[GetStudentInfoWithRelationDetail]:
    student = await student_service.get(pk=pk)
    return response_base.success(data=student)


@router.get(
    '',
    summary='分页获取所有学生信息',
    dependencies=[
        DependsJwtAuth,
        DependsPagination,
    ],
)
async def get_students_paged(db: CurrentSession) -> ResponseSchemaModel[PageData[GetStudentInfoWithRelationDetail]]:
    student_select = await student_service.get_select()
    page_data = await paging_data(db, student_select)
    return response_base.success(data=page_data)


@router.post(
    '',
    summary='创建学生信息',
    dependencies=[
        Depends(RequestPermission('sys:student:add')),
        DependsRBAC,
    ],
)
async def create_student(request: Request, obj: AddStudentParam) -> ResponseSchemaModel[GetUserInfoWithRelationDetail]:
    if obj.student_number is not None:
        if await student_service.check_student_number(student_number=obj.student_number, school_id=obj.school_id):
            raise errors.ConflictError(msg='该学校中学号已存在')
    else:
        while True:
            student_number = generate_student_id()
            student_check = await student_service.check_student_number(student_number=student_number, school_id=obj.school_id)
            if not student_check:
                break
        obj.student_number = student_number
    obj.nickname = obj.username or '<UNK>'
    obj.username = f'{obj.school_id}-{obj.student_number}-{obj.username}'

    await user_service.create(request=request,
        obj=AddUserParam(username=obj.username, nickname=obj.nickname, dept_id=obj.dept_id, roles=obj.roles, password=obj.password))
    data = await user_service.get_userinfo(username=obj.username)
    await student_service.create(obj=CreateStudentParam(user_id=data.id, student_number=obj.student_number, school_id=obj.school_id))
    return response_base.success(data=data)


@router.put(
    '/{pk}',
    summary='更新学生信息',
    dependencies=[
        Depends(RequestPermission('sys:student:edit')),
        DependsRBAC,
    ],
)
async def update_student(pk: Annotated[int, Path(description='学生信息 ID')], obj: UpdateStudentParam) -> ResponseModel:
    count = await student_service.update(pk=pk, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()


@router.delete(
    '',
    summary='批量删除学生信息',
    dependencies=[
        Depends(RequestPermission('sys:student:del')),
        DependsRBAC,
    ],
)
async def delete_students(obj: DeleteStudentParam) -> ResponseModel:
    count = await student_service.delete(obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()
