#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from plugin.exam.model.submission import Submission
from plugin.exam.schema.submission import CreateSubmissionParam, UpdateSubmissionParam


class CRUDSubmission(CRUDPlus[Submission]):
    """提交数据库操作类"""

    async def get(self, db: AsyncSession, pk: int) -> Submission | None:
        """
        获取提交

        :param db: 数据库会话
        :param pk: 提交 ID
        :return:
        """
        return await self.select_model(db, pk)

    async def get_by_user_exam(self, db: AsyncSession, user_id: int, exam_id: int) -> Submission | None:
        """
        根据用户ID和考试ID获取提交

        :param db: 数据库会话
        :param user_id: 用户 ID
        :param exam_id: 考试 ID
        :return:
        """
        return await self.select_model_by_column(db, user_id=user_id, exam_id=exam_id)

    async def get_list(self, user_id: int | None = None, exam_id: int | None = None, status: str | None = None) -> Select:
        """
        获取提交列表
        
        :param user_id: 用户 ID
        :param exam_id: 考试 ID
        :param status: 提交状态
        :return:
        """
        filters = {}
        if user_id:
            filters.update(user_id=user_id)
        if exam_id:
            filters.update(exam_id=exam_id)
        if status:
            filters.update(status=status)
        return await self.select_models_order(sort_columns='created_time', sort_type='desc', **filters)

    async def get_all(self, db: AsyncSession) -> Sequence[Submission]:
        """
        获取所有提交

        :param db: 数据库会话
        :return:
        """
        return await self.select_models(db)

    async def get_by_user_id(self, db: AsyncSession, user_id: int) -> Sequence[Submission]:
        """
        根据用户ID获取提交列表
        
        :param db: 数据库会话
        :param user_id: 用户 ID
        :return:
        """
        return await self.select_models(db, user_id=user_id)

    async def get_by_exam_id(self, db: AsyncSession, exam_id: int) -> Sequence[Submission]:
        """
        根据考试ID获取提交列表
        
        :param db: 数据库会话
        :param exam_id: 考试 ID
        :return:
        """
        return await self.select_models(db, exam_id=exam_id)

    async def create(self, db: AsyncSession, obj: CreateSubmissionParam) -> Submission:
        """
        创建提交

        :param db: 数据库会话
        :param obj: 创建提交参数
        :return:
        """
        return await self.create_model(db, obj)

    async def update(self, db: AsyncSession, pk: int, obj: UpdateSubmissionParam) -> int:
        """
        更新提交

        :param db: 数据库会话
        :param pk: 提交 ID
        :param obj: 更新提交参数
        :return:
        """
        return await self.update_model(db, pk, obj)

    async def delete(self, db: AsyncSession, pks: list[int]) -> int:
        """
        批量删除提交

        :param db: 数据库会话
        :param pks: 提交 ID 列表
        :return:
        """
        return await self.delete_model_by_column(db, allow_multiple=True, id__in=pks)


submission_dao: CRUDSubmission = CRUDSubmission(Submission)