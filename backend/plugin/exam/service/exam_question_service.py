#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from common.exception import errors
from database.db import async_db_session
from plugin.exam.crud.crud_exam_question import exam_question_dao
from plugin.exam.model.exam_question import ExamQuestion
from plugin.exam.schema.exam_question import CreateExamQuestionParam, DeleteExamQuestionParam, UpdateExamQuestionParam


class ExamQuestionService:
    """考试题目服务类"""

    @staticmethod
    async def get(*, pk: int) -> ExamQuestion:
        """
        获取考试题目

        :param pk: 考试题目 ID
        :return:
        """
        async with async_db_session() as db:
            exam_question = await exam_question_dao.get(db, pk)
            if not exam_question:
                raise errors.NotFoundError(msg='考试题目不存在')
            return exam_question

    @staticmethod
    async def get_select(*, exam_id: int | None = None) -> Select:
        """
        获取考试题目列表查询条件

        :param exam_id: 考试 ID
        :return:
        """
        return await exam_question_dao.get_list(exam_id=exam_id)

    @staticmethod
    async def get_all(*, db: AsyncSession) -> Sequence[ExamQuestion]:
        """
        获取所有考试题目

        :param db: 数据库会话
        :return:
        """
        return await exam_question_dao.get_all(db)

    @staticmethod
    async def get_by_exam_id(*, exam_id: int) -> Sequence[ExamQuestion]:
        """
        根据考试ID获取题目列表
        
        :param exam_id: 考试 ID
        :return:
        """
        async with async_db_session() as db:
            return await exam_question_dao.get_by_exam_id(db, exam_id)

    @staticmethod
    async def create(*, obj: CreateExamQuestionParam) -> None:
        """
        创建考试题目

        :param obj: 创建考试题目参数
        :return:
        """
        async with async_db_session.begin() as db:
            await exam_question_dao.create(db, obj)

    @staticmethod
    async def update(*, pk: int, obj: UpdateExamQuestionParam) -> int:
        """
        更新考试题目

        :param pk: 考试题目 ID
        :param obj: 更新考试题目参数
        :return:
        """
        async with async_db_session.begin() as db:
            count = await exam_question_dao.update(db, pk, obj)
            if count == 0:
                raise errors.NotFoundError(msg='考试题目不存在')
            return count

    @staticmethod
    async def delete(*, obj: DeleteExamQuestionParam) -> int:
        """
        删除考试题目

        :param obj: 删除考试题目参数
        :return:
        """
        async with async_db_session.begin() as db:
            count = await exam_question_dao.delete(db, obj.pks)
            if count == 0:
                raise errors.NotFoundError(msg='考试题目不存在')
            return count


exam_question_service: ExamQuestionService = ExamQuestionService()