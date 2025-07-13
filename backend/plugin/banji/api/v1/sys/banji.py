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
from plugin.banji.schema.banji import CreateBanjiParam, DeleteBanjiParam, GetBanjiDetail, UpdateBanjiParam
from plugin.banji.service.banji_service import banji_service

router = APIRouter()


@router.get('/{pk}', summary='获取班级详情', dependencies=[DependsJwtAuth])
async def get_banji(pk: Annotated[int, Path(description='班级 ID')]) -> ResponseSchemaModel[GetBanjiDetail]:
    banji = await banji_service.get(pk=pk)
    return response_base.success(data=banji)


@router.get(
    '',
    summary='分页获取所有班级',
    dependencies=[
        DependsJwtAuth,
        DependsPagination,
    ],
)
async def get_banjis_paged(db: CurrentSession) -> ResponseSchemaModel[PageData[GetBanjiDetail]]:
    banji_select = await banji_service.get_select()
    page_data = await paging_data(db, banji_select)
    return response_base.success(data=page_data)


@router.post(
    '',
    summary='创建班级',
    dependencies=[
        Depends(RequestPermission('sys:banji:add')),
        DependsRBAC,
    ],
)
async def create_banji(obj: CreateBanjiParam) -> ResponseModel:
    await banji_service.create(obj=obj)
    return response_base.success()


@router.put(
    '/{pk}',
    summary='更新班级',
    dependencies=[
        Depends(RequestPermission('sys:banji:edit')),
        DependsRBAC,
    ],
)
async def update_banji(pk: Annotated[int, Path(description='班级 ID')], obj: UpdateBanjiParam) -> ResponseModel:
    count = await banji_service.update(pk=pk, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()


@router.delete(
    '',
    summary='批量删除班级',
    dependencies=[
        Depends(RequestPermission('sys:banji:del')),
        DependsRBAC,
    ],
)
async def delete_banjis(obj: DeleteBanjiParam) -> ResponseModel:
    count = await banji_service.delete(obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()