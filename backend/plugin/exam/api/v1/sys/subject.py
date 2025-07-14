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
from plugin.exam.schema.subject import CreateSubjectParam, DeleteSubjectParam, GetSubjectDetail, UpdateSubjectParam
from plugin.exam.service.subject_service import subject_service

router = APIRouter()


@router.get('/{pk}', summary='获取学科详情', dependencies=[DependsJwtAuth])
async def get_subject(pk: Annotated[int, Path(description='学科 ID')]) -> ResponseSchemaModel[GetSubjectDetail]:
    subject = await subject_service.get(pk=pk)
    return response_base.success(data=subject)


@router.get(
    '',
    summary='分页获取所有学科',
    dependencies=[
        DependsJwtAuth,
        DependsPagination,
    ],
)
async def get_subjects_paged(db: CurrentSession) -> ResponseSchemaModel[PageData[GetSubjectDetail]]:
    subject_select = await subject_service.get_select()
    page_data = await paging_data(db, subject_select)
    return response_base.success(data=page_data)


@router.post(
    '',
    summary='创建学科',
    dependencies=[
        Depends(RequestPermission('sys:subject:add')),
        DependsRBAC,
    ],
)
async def create_subject(obj: CreateSubjectParam) -> ResponseModel:
    await subject_service.create(obj=obj)
    return response_base.success()


@router.put(
    '/{pk}',
    summary='更新学科',
    dependencies=[
        Depends(RequestPermission('sys:subject:edit')),
        DependsRBAC,
    ],
)
async def update_subject(pk: Annotated[int, Path(description='学科 ID')], obj: UpdateSubjectParam) -> ResponseModel:
    count = await subject_service.update(pk=pk, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()


@router.delete(
    '',
    summary='批量删除学科',
    dependencies=[
        Depends(RequestPermission('sys:subject:del')),
        DependsRBAC,
    ],
)
async def delete_subjects(obj: DeleteSubjectParam) -> ResponseModel:
    count = await subject_service.delete(obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()