#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query

from common.pagination import DependsPagination, PageData, paging_data
from common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base
from common.security.jwt import DependsJwtAuth
from common.security.permission import RequestPermission
from common.security.rbac import DependsRBAC
from database.db import CurrentSession
from plugin.exam.schema.exam_question import CreateExamQuestionParam, DeleteExamQuestionParam, GetExamQuestionDetail, UpdateExamQuestionParam
from plugin.exam.service.exam_question_service import exam_question_service

router = APIRouter()


@router.get('/{pk}', summary='获取考试题目详情', dependencies=[DependsJwtAuth])
async def get_exam_question(pk: Annotated[int, Path(description='考试题目 ID')]) -> ResponseSchemaModel[GetExamQuestionDetail]:
    exam_question = await exam_question_service.get(pk=pk)
    return response_base.success(data=exam_question)


@router.get(
    '',
    summary='分页获取考试题目',
    dependencies=[
        DependsJwtAuth,
        DependsPagination,
    ],
)
async def get_exam_questions_paged(
    db: CurrentSession,
    exam_id: Annotated[int | None, Query(description='考试 ID')] = None
) -> ResponseSchemaModel[PageData[GetExamQuestionDetail]]:
    exam_question_select = await exam_question_service.get_select(exam_id=exam_id)
    page_data = await paging_data(db, exam_question_select)
    return response_base.success(data=page_data)


@router.get(
    '/by-exam/{exam_id}',
    summary='根据考试ID获取题目列表',
    dependencies=[DependsJwtAuth],
)
async def get_exam_questions_by_exam_id(
    exam_id: Annotated[int, Path(description='考试 ID')]
) -> ResponseSchemaModel[list[GetExamQuestionDetail]]:
    exam_questions = await exam_question_service.get_by_exam_id(exam_id=exam_id)
    return response_base.success(data=exam_questions)


@router.post(
    '',
    summary='创建考试题目',
    dependencies=[
        Depends(RequestPermission('sys:exam_question:add')),
        DependsRBAC,
    ],
)
async def create_exam_question(obj: CreateExamQuestionParam) -> ResponseModel:
    await exam_question_service.create(obj=obj)
    return response_base.success()


@router.put(
    '/{pk}',
    summary='更新考试题目',
    dependencies=[
        Depends(RequestPermission('sys:exam_question:edit')),
        DependsRBAC,
    ],
)
async def update_exam_question(pk: Annotated[int, Path(description='考试题目 ID')], obj: UpdateExamQuestionParam) -> ResponseModel:
    count = await exam_question_service.update(pk=pk, obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()


@router.delete(
    '',
    summary='批量删除考试题目',
    dependencies=[
        Depends(RequestPermission('sys:exam_question:del')),
        DependsRBAC,
    ],
)
async def delete_exam_questions(obj: DeleteExamQuestionParam) -> ResponseModel:
    count = await exam_question_service.delete(obj=obj)
    if count > 0:
        return response_base.success()
    return response_base.fail()