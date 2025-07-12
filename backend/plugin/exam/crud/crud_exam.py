#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from plugin.exam.model import Exam
from plugin.exam.schema.exam import CreateExamParam, UpdateExamParam


class CRUDExam(CRUDPlus[Exam]):
    """测验数据库操作类"""

    async def get(self, db: AsyncSession, pk: int) -> Exam | None:
        """
        获取测验

        :param db: 数据库会话
        :param pk: 测验 ID
        :return:
        """
        return await self.select_model(db, pk)

    async def get_list(self) -> Select:
        """获取测验列表"""
        return await self.select_order('created_time', 'desc')

    async def get_all(self, db: AsyncSession) -> Sequence[Exam]:
        """
        获取所有测验

        :param db: 数据库会话
        :return:
        """
        return await self.select_models(db)

    async def create(self, db: AsyncSession, obj: CreateExamParam) -> None:
        """
        创建测验

        :param db: 数据库会话
        :param obj: 创建测验参数
        :return:
        """
        await self.create_model(db, obj)

    async def update(self, db: AsyncSession, pk: int, obj: UpdateExamParam) -> int:
        """
        更新测验

        :param db: 数据库会话
        :param pk: 测验 ID
        :param obj: 更新测验参数
        :return:
        """
        return await self.update_model(db, pk, obj)

    async def delete(self, db: AsyncSession, pks: list[int]) -> int:
        """
        批量删除测验

        :param db: 数据库会话
        :param pks: 测验 ID 列表
        :return:
        """
        return await self.delete_model_by_column(db, allow_multiple=True, id__in=pks)


exam_dao: CRUDExam = CRUDExam(Exam)
