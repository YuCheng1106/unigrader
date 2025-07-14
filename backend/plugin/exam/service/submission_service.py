#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from common.exception import errors
from database.db import async_db_session
from plugin.exam.crud.crud_submission import submission_dao
from plugin.exam.model.submission import Submission
from plugin.exam.schema.submission import CreateSubmissionParam, DeleteSubmissionParam, UpdateSubmissionParam


class SubmissionService:
    """提交服务类"""

    @staticmethod
    async def get(*, pk: int) -> Submission:
        """
        获取提交

        :param pk: 提交 ID
        :return:
        """
        async with async_db_session() as db:
            submission = await submission_dao.get(db, pk)
            if not submission:
                raise errors.NotFoundError(msg='提交不存在')
            return submission

    @staticmethod
    async def get_by_user_exam(*, user_id: int, exam_id: int) -> Submission | None:
        """
        根据用户ID和考试ID获取提交

        :param user_id: 用户 ID
        :param exam_id: 考试 ID
        :return:
        """
        async with async_db_session() as db:
            return await submission_dao.get_by_user_exam(db, user_id, exam_id)

    @staticmethod
    async def get_select(*, user_id: int | None = None, exam_id: int | None = None, status: str | None = None) -> Select:
        """
        获取提交列表查询条件

        :param user_id: 用户 ID
        :param exam_id: 考试 ID
        :param status: 提交状态
        :return:
        """
        return await submission_dao.get_list(user_id=user_id, exam_id=exam_id, status=status)

    @staticmethod
    async def get_all(*, db: AsyncSession) -> Sequence[Submission]:
        """
        获取所有提交

        :param db: 数据库会话
        :return:
        """
        return await submission_dao.get_all(db)

    @staticmethod
    async def get_by_user_id(*, user_id: int) -> Sequence[Submission]:
        """
        根据用户ID获取提交列表
        
        :param user_id: 用户 ID
        :return:
        """
        async with async_db_session() as db:
            return await submission_dao.get_by_user_id(db, user_id)

    @staticmethod
    async def get_by_exam_id(*, exam_id: int) -> Sequence[Submission]:
        """
        根据考试ID获取提交列表
        
        :param exam_id: 考试 ID
        :return:
        """
        async with async_db_session() as db:
            return await submission_dao.get_by_exam_id(db, exam_id)

    @staticmethod
    async def create(*, obj: CreateSubmissionParam) -> Submission:
        """
        创建提交

        :param obj: 创建提交参数
        :return:
        """
        async with async_db_session.begin() as db:
            # 检查是否已存在相同用户和考试的提交
            existing = await submission_dao.get_by_user_exam(db, obj.user_id, obj.exam_id)
            if existing:
                raise errors.ConflictError(msg='该用户已有此考试的提交记录')
            return await submission_dao.create(db, obj)

    @staticmethod
    async def update(*, pk: int, obj: UpdateSubmissionParam) -> int:
        """
        更新提交

        :param pk: 提交 ID
        :param obj: 更新提交参数
        :return:
        """
        async with async_db_session.begin() as db:
            count = await submission_dao.update(db, pk, obj)
            if count == 0:
                raise errors.NotFoundError(msg='提交不存在')
            return count

    @staticmethod
    async def delete(*, obj: DeleteSubmissionParam) -> int:
        """
        删除提交

        :param obj: 删除提交参数
        :return:
        """
        async with async_db_session.begin() as db:
            count = await submission_dao.delete(db, obj.pks)
            if count == 0:
                raise errors.NotFoundError(msg='提交不存在')
            return count


submission_service: SubmissionService = SubmissionService()