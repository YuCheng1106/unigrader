#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select

from common.exception import errors
from database.db import async_db_session
from plugin.exam.crud.crud_exam import exam_dao
from plugin.exam.model import Exam
from plugin.exam.schema.exam import CreateExamParam, DeleteExamParam, UpdateExamParam


class ExamService:
    """测验服务类"""

    @staticmethod
    async def get(*, pk: int) -> Exam:
        """
        获取测验

        :param pk: 测验 ID
        :return:
        """
        async with async_db_session() as db:
            exam = await exam_dao.get(db, pk)
            if not exam:
                raise errors.NotFoundError(msg='测验不存在')
            return exam

    @staticmethod
    async def get_select() -> Select:
        """获取测验查询对象"""
        return await exam_dao.get_list()

    @staticmethod
    async def get_all() -> Sequence[Exam]:
        """获取所有测验"""
        async with async_db_session() as db:
            exams = await exam_dao.get_all(db)
            return exams

    @staticmethod
    async def create(*, obj: CreateExamParam) -> None:
        """
        创建测验

        :param obj: 创建测验参数
        :return:
        """
        async with async_db_session.begin() as db:
            await exam_dao.create(db, obj)

    @staticmethod
    async def update(*, pk: int, obj: UpdateExamParam) -> int:
        """
        更新测验

        :param pk: 测验 ID
        :param obj: 更新测验参数
        :return:
        """
        async with async_db_session.begin() as db:
            exam = await exam_dao.get(db, pk)
            if not exam:
                raise errors.NotFoundError(msg='测验不存在')
            count = await exam_dao.update(db, pk, obj)
            return count

    @staticmethod
    async def delete(*, obj: DeleteExamParam) -> int:
        """
        批量删除测验

        :param obj: 测验 ID 列表
        :return:
        """
        async with async_db_session.begin() as db:
            count = await exam_dao.delete(db, obj.pks)
            return count


exam_service: ExamService = ExamService()
