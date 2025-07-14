#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from plugin.exam.model.exam_question import ExamQuestion
from plugin.exam.schema.exam_question import CreateExamQuestionParam, UpdateExamQuestionParam


class CRUDExamQuestion(CRUDPlus[ExamQuestion]):
    """考试题目数据库操作类"""

    async def get(self, db: AsyncSession, pk: int) -> ExamQuestion | None:
        """
        获取考试题目

        :param db: 数据库会话
        :param pk: 考试题目 ID
        :return:
        """
        return await self.select_model(db, pk)

    async def get_list(self, exam_id: int | None = None) -> Select:
        """
        获取考试题目列表
        
        :param exam_id: 考试 ID
        :return:
        """
        filters = {}
        if exam_id:
            filters.update(exam_id=exam_id)
        return await self.select_models_order(sort_columns='sequence', **filters)

    async def get_all(self, db: AsyncSession) -> Sequence[ExamQuestion]:
        """
        获取所有考试题目

        :param db: 数据库会话
        :return:
        """
        return await self.select_models(db)

    async def get_by_exam_id(self, db: AsyncSession, exam_id: int) -> Sequence[ExamQuestion]:
        """
        根据考试ID获取题目列表
        
        :param db: 数据库会话
        :param exam_id: 考试 ID
        :return:
        """
        return await self.select_models(db, exam_id=exam_id)

    async def create(self, db: AsyncSession, obj: CreateExamQuestionParam) -> None:
        """
        创建考试题目

        :param db: 数据库会话
        :param obj: 创建考试题目参数
        :return:
        """
        await self.create_model(db, obj)

    async def update(self, db: AsyncSession, pk: int, obj: UpdateExamQuestionParam) -> int:
        """
        更新考试题目

        :param db: 数据库会话
        :param pk: 考试题目 ID
        :param obj: 更新考试题目参数
        :return:
        """
        return await self.update_model(db, pk, obj)

    async def delete(self, db: AsyncSession, pks: list[int]) -> int:
        """
        批量删除考试题目

        :param db: 数据库会话
        :param pks: 考试题目 ID 列表
        :return:
        """
        return await self.delete_model_by_column(db, allow_multiple=True, id__in=pks)


exam_question_dao: CRUDExamQuestion = CRUDExamQuestion(ExamQuestion)