#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from backend.common.pagination import DependsPagination, paging_data
from backend.common.response import ResponseModel, response_base
from backend.common.security import DependsJwtAuth
from backend.database.db_mysql import get_db
from ...schema.submission_answer import (
    CreateSubmissionAnswerParam,
    UpdateSubmissionAnswerParam,
    DeleteSubmissionAnswerParam,
    GetSubmissionAnswerDetail
)
from ...service.submission_answer_service import submission_answer_service

router = APIRouter()


@router.get('/{int:submission_answer_id}', summary='获取提交答案详情', dependencies=[DependsJwtAuth])
async def get_submission_answer(
    submission_answer_id: int,
    db: AsyncSession = Depends(get_db)
) -> ResponseModel[GetSubmissionAnswerDetail]:
    submission_answer = await submission_answer_service.get_submission_answer_by_id(db, submission_answer_id)
    return await response_base.success(data=submission_answer)


@router.get('/submission/{int:submission_id}', summary='通过提交ID获取所有答案', dependencies=[DependsJwtAuth])
async def get_submission_answers_by_submission_id(
    submission_id: int,
    db: AsyncSession = Depends(get_db)
) -> ResponseModel[list[GetSubmissionAnswerDetail]]:
    submission_answers = await submission_answer_service.get_submission_answers_by_submission_id(db, submission_id)
    return await response_base.success(data=submission_answers)


@router.get('/user/{int:user_id}', summary='通过用户ID获取所有答案', dependencies=[DependsJwtAuth])
async def get_submission_answers_by_user_id(
    user_id: int,
    db: AsyncSession = Depends(get_db)
) -> ResponseModel[list[GetSubmissionAnswerDetail]]:
    submission_answers = await submission_answer_service.get_submission_answers_by_user_id(db, user_id)
    return await response_base.success(data=submission_answers)


@router.get('/exam/{int:exam_id}', summary='通过考试ID获取所有答案', dependencies=[DependsJwtAuth])
async def get_submission_answers_by_exam_id(
    exam_id: int,
    db: AsyncSession = Depends(get_db)
) -> ResponseModel[list[GetSubmissionAnswerDetail]]:
    submission_answers = await submission_answer_service.get_submission_answers_by_exam_id(db, exam_id)
    return await response_base.success(data=submission_answers)


@router.get('/user/{int:user_id}/question/{int:exam_question_id}', summary='通过用户ID和题目ID获取答案', dependencies=[DependsJwtAuth])
async def get_submission_answer_by_user_and_question(
    user_id: int,
    exam_question_id: int,
    db: AsyncSession = Depends(get_db)
) -> ResponseModel[GetSubmissionAnswerDetail | None]:
    submission_answer = await submission_answer_service.get_submission_answer_by_user_and_question(db, user_id, exam_question_id)
    return await response_base.success(data=submission_answer)


@router.get('/grader/{int:graded_by_id}', summary='通过批改者ID获取所有批改的答案', dependencies=[DependsJwtAuth])
async def get_submission_answers_by_grader(
    graded_by_id: int,
    db: AsyncSession = Depends(get_db)
) -> ResponseModel[list[GetSubmissionAnswerDetail]]:
    submission_answers = await submission_answer_service.get_submission_answers_by_grader(db, graded_by_id)
    return await response_base.success(data=submission_answers)


@router.post('', summary='创建提交答案', dependencies=[DependsJwtAuth])
async def create_submission_answer(
    obj: CreateSubmissionAnswerParam,
    db: AsyncSession = Depends(get_db)
) -> ResponseModel:
    await submission_answer_service.create_submission_answer(db, obj)
    return await response_base.success()


@router.put('/{int:submission_answer_id}', summary='更新提交答案', dependencies=[DependsJwtAuth])
async def update_submission_answer(
    submission_answer_id: int,
    obj: UpdateSubmissionAnswerParam,
    db: AsyncSession = Depends(get_db)
) -> ResponseModel:
    await submission_answer_service.update_submission_answer(db, submission_answer_id, obj)
    return await response_base.success()


@router.delete('/{int:submission_answer_id}', summary='删除提交答案', dependencies=[DependsJwtAuth])
async def delete_submission_answer(
    submission_answer_id: int,
    db: AsyncSession = Depends(get_db)
) -> ResponseModel:
    await submission_answer_service.delete_submission_answer(db, submission_answer_id)
    return await response_base.success()


@router.delete('', summary='批量删除提交答案', dependencies=[DependsJwtAuth])
async def delete_submission_answers(
    obj: DeleteSubmissionAnswerParam,
    db: AsyncSession = Depends(get_db)
) -> ResponseModel:
    await submission_answer_service.delete_submission_answers(db, obj.pks)
    return await response_base.success()