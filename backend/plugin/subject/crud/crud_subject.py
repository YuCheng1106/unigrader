#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy_crud_plus import CRUDPlus
from plugin.subject.model.subject import Subject
from plugin.subject.schema.subject import CreateSubjectParam, UpdateSubjectParam


class CRUDSubject(CRUDPlus[Subject]):
    """学科 CRUD 类"""

    async def get(self, db: AsyncSession, pk: int) -> Subject | None:
        """
        获取学科

        :param db: 数据库会话
        :param pk: 学科 ID
        :return:
        """
        return await self.select_model(db, pk)

    async def get_list(self, name: str | None = None) -> Select:
        """
        获取学科列表

        :param name: 学科名称
        :return:
        """
        filters = {}
        if name:
            filters.update(name__icontains=name)
        return await self.select_models_order(sort_columns='id', **filters)

    async def get_all(self, db: AsyncSession) -> Sequence[Subject]:
        """
        获取所有学科

        :param db: 数据库会话
        :return:
        """
        return await self.select_models(db)

    async def create(self, db: AsyncSession, obj: CreateSubjectParam) -> None:
        """
        创建学科

        :param db: 数据库会话
        :param obj: 创建学科参数
        :return:
        """
        await self.create_model(db, obj)

    async def update(self, db: AsyncSession, pk: int, obj: UpdateSubjectParam) -> int:
        """
        更新学科

        :param db: 数据库会话
        :param pk: 学科 ID
        :param obj: 更新学科参数
        :return:
        """
        return await self.update_model(db, pk, obj)

    async def delete(self, db: AsyncSession, pk: list[int]) -> int:
        """
        删除学科

        :param db: 数据库会话
        :param pk: 学科 ID 列表
        :return:
        """
        return await self.delete_model_by_column(db, allow_multiple=True, id__in=pk)


subject_dao: CRUDSubject = CRUDSubject(Subject)