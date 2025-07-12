#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Annotated

from fastapi import APIRouter, Depends, Path

from common.pagination import DependsPagination, PageData, paging_data
from common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base
from common.security.jwt import DependsJwtAuth
from common.security.permission import RequestPermission
from common.security.rbac import DependsRBAC
from database.db import CurrentSession
from plugin.exam.schema.exam import CreateExamParam, DeleteExamParam, GetExamDetail, UpdateExamParam
from plugin.exam.service.exam_service import exam_service

router = APIRouter()


@router.get('/{pk}', summary='获取测验详情', dependencies=[DependsJwtAuth])
async def get_exam(pk: Annotated[int, Path(description='测验 ID')]) -> ResponseSchemaModel[GetExamDetail]:
    exam = await exam_service.get(pk=pk)
    return response_base.success(data=exam)


@router.get(
    '',
    summary='分页获取所有测验',
    dependencies=[
        DependsJwtAuth,
        DependsPagination,
    ],
)
async def get_exams_paged(db: CurrentSession) -> ResponseSchemaModel[PageData[GetExamDetail]]:
    exam_select = await exam_service.get_select()
    page_data = await paging_data(db, exam_select)
    return response_base.success(data=page_data)


@router.post(
    '',
    summary='创建测验',
    dependencies=[
        Depends(RequestPermission('sys:exam:add')),
        DependsRBAC,
    ],
)
async def create_exam(obj: CreateExamParam) -> ResponseModel:
    await exam_service.create(obj=obj)
    return response_base.success()


@router.put(
    '/{pk}',
    summary='更新测验',
    dependencies=[
        Depends(RequestPermission('sys:exam:edit')),
        DependsRBAC,
    ],
)
async def update_exam(pk: Annotated[int, Path(description='测验 ID')], obj: UpdateExamParam) -> ResponseModel:
    count = await exam_service.update(pk=pk, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()


@router.delete(
    '',
    summary='批量删除测验',
    dependencies=[
        Depends(RequestPermission('sys:exam:del')),
        DependsRBAC,
    ],
)
async def delete_exams(obj: DeleteExamParam) -> ResponseModel:
    count = await exam_service.delete(obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()
