#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query

from common.pagination import DependsPagination, paging_data
from common.response.response_schema import ResponseModel, response_base
from common.security import DependsJwtAuth
from database.db import CurrentSession
from plugin.exam.schema.submission import (
    CreateSubmissionParam,
    DeleteSubmissionParam,
    GetSubmissionDetail,
    UpdateSubmissionParam,
)
from plugin.exam.service.submission_service import submission_service

router = APIRouter()


@router.get('/{pk}', summary='获取提交详情', dependencies=[DependsJwtAuth])
async def get_submission(
    pk: Annotated[int, Path(description='提交ID')],
) -> ResponseModel[GetSubmissionDetail]:
    submission = await submission_service.get(pk=pk)
    return await response_base.success(data=submission)


@router.get('', summary='获取提交列表（分页）', dependencies=[DependsJwtAuth])
async def get_pagination_submissions(
    db: CurrentSession,
    page: DependsPagination,
    user_id: Annotated[int | None, Query(description='用户ID')] = None,
    exam_id: Annotated[int | None, Query(description='考试ID')] = None,
    status: Annotated[str | None, Query(description='提交状态')] = None,
) -> ResponseModel[list[GetSubmissionDetail]]:
    select = await submission_service.get_select(user_id=user_id, exam_id=exam_id, status=status)
    page_data = await paging_data(db, select, page)
    return await response_base.success(data=page_data)


@router.get('/user/{user_id}', summary='根据用户ID获取提交列表', dependencies=[DependsJwtAuth])
async def get_submissions_by_user(
    user_id: Annotated[int, Path(description='用户ID')],
) -> ResponseModel[list[GetSubmissionDetail]]:
    submissions = await submission_service.get_by_user_id(user_id=user_id)
    return await response_base.success(data=submissions)


@router.get('/exam/{exam_id}', summary='根据考试ID获取提交列表', dependencies=[DependsJwtAuth])
async def get_submissions_by_exam(
    exam_id: Annotated[int, Path(description='考试ID')],
) -> ResponseModel[list[GetSubmissionDetail]]:
    submissions = await submission_service.get_by_exam_id(exam_id=exam_id)
    return await response_base.success(data=submissions)


@router.get('/user/{user_id}/exam/{exam_id}', summary='根据用户ID和考试ID获取提交', dependencies=[DependsJwtAuth])
async def get_submission_by_user_exam(
    user_id: Annotated[int, Path(description='用户ID')],
    exam_id: Annotated[int, Path(description='考试ID')],
) -> ResponseModel[GetSubmissionDetail | None]:
    submission = await submission_service.get_by_user_exam(user_id=user_id, exam_id=exam_id)
    return await response_base.success(data=submission)


@router.post('', summary='创建提交', dependencies=[DependsJwtAuth])
async def create_submission(
    obj: CreateSubmissionParam,
) -> ResponseModel[GetSubmissionDetail]:
    submission = await submission_service.create(obj=obj)
    return await response_base.success(data=submission)


@router.put('/{pk}', summary='更新提交', dependencies=[DependsJwtAuth])
async def update_submission(
    pk: Annotated[int, Path(description='提交ID')],
    obj: UpdateSubmissionParam,
) -> ResponseModel[int]:
    count = await submission_service.update(pk=pk, obj=obj)
    return await response_base.success(data=count)


@router.delete('', summary='删除提交', dependencies=[DependsJwtAuth])
async def delete_submission(
    obj: DeleteSubmissionParam,
) -> ResponseModel[int]:
    count = await submission_service.delete(obj=obj)
    return await response_base.success(data=count)