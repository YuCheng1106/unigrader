#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter, Depends, Query

from common.pagination import DependsPagination, paging_data
from common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base
from common.security.jwt import DependsJwtAuth
from database.db import CurrentSession
from plugin.exam.schema.submission_answer import (
    CreateSubmissionAnswerParam,
    UpdateSubmissionAnswerParam,
    DeleteSubmissionAnswerParam,
    GetSubmissionAnswerDetail
)
from plugin.exam.service.submission_answer_service import submission_answer_service

router = APIRouter()


@router.get('/{submission_answer_id}', summary='获取提交答案详情', dependencies=[DependsJwtAuth])
async def get_submission_answer(
    submission_answer_id: int,
    db: CurrentSession
) -> ResponseSchemaModel[GetSubmissionAnswerDetail]:
    submission_answer = await submission_answer_service.get_submission_answer_by_id(db, submission_answer_id)
    return response_base.success(data=submission_answer)


@router.get('/submission/{submission_id}', summary='通过提交ID获取所有答案', dependencies=[DependsJwtAuth])
async def get_submission_answers_by_submission_id(
    submission_id: int,
    db: CurrentSession
) -> ResponseSchemaModel[list[GetSubmissionAnswerDetail]]:
    submission_answers = await submission_answer_service.get_submission_answers_by_submission_id(db, submission_id)
    return response_base.success(data=submission_answers)


@router.get('/user/{user_id}', summary='通过用户ID获取所有答案', dependencies=[DependsJwtAuth])
async def get_submission_answers_by_user_id(
    user_id: int,
    db: CurrentSession
) -> ResponseSchemaModel[list[GetSubmissionAnswerDetail]]:
    submission_answers = await submission_answer_service.get_submission_answers_by_user_id(db, user_id)
    return response_base.success(data=submission_answers)


@router.get('/exam/{exam_id}', summary='通过考试ID获取所有答案', dependencies=[DependsJwtAuth])
async def get_submission_answers_by_exam_id(
    exam_id: int,
    db: CurrentSession
) -> ResponseSchemaModel[list[GetSubmissionAnswerDetail]]:
    submission_answers = await submission_answer_service.get_submission_answers_by_exam_id(db, exam_id)
    return response_base.success(data=submission_answers)


@router.get('/user/{user_id}/question/{exam_question_id}', summary='通过用户ID和题目ID获取答案', dependencies=[DependsJwtAuth])
async def get_submission_answer_by_user_and_question(
    user_id: int,
    exam_question_id: int,
    db: CurrentSession
) -> ResponseSchemaModel[GetSubmissionAnswerDetail | None]:
    submission_answer = await submission_answer_service.get_submission_answer_by_user_and_question(db, user_id, exam_question_id)
    return response_base.success(data=submission_answer)


@router.get('/grader/{graded_by_id}', summary='通过批改者ID获取所有批改的答案', dependencies=[DependsJwtAuth])
async def get_submission_answers_by_grader(
    graded_by_id: int,
    db: CurrentSession
) -> ResponseSchemaModel[list[GetSubmissionAnswerDetail]]:
    submission_answers = await submission_answer_service.get_submission_answers_by_grader(db, graded_by_id)
    return response_base.success(data=submission_answers)


@router.post('', summary='创建提交答案', dependencies=[DependsJwtAuth])
async def create_submission_answer(
    obj: CreateSubmissionAnswerParam,
    db: CurrentSession
) -> ResponseModel:
    await submission_answer_service.create_submission_answer(db, obj)
    return response_base.success()


@router.put('/{submission_answer_id}', summary='更新提交答案', dependencies=[DependsJwtAuth])
async def update_submission_answer(
    submission_answer_id: int,
    obj: UpdateSubmissionAnswerParam,
    db: CurrentSession
) -> ResponseModel:
    await submission_answer_service.update_submission_answer(db, submission_answer_id, obj)
    return response_base.success()


@router.delete('/{submission_answer_id}', summary='删除提交答案', dependencies=[DependsJwtAuth])
async def delete_submission_answer(
    submission_answer_id: int,
    db: CurrentSession
) -> ResponseModel:
    await submission_answer_service.delete_submission_answer(db, submission_answer_id)
    return response_base.success()


@router.delete('', summary='批量删除提交答案', dependencies=[DependsJwtAuth])
async def delete_submission_answers(
    obj: DeleteSubmissionAnswerParam,
    db: CurrentSession
) -> ResponseModel:
    await submission_answer_service.delete_submission_answers(db, obj.pks)
    return response_base.success()