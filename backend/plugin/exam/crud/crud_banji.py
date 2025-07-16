#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from plugin.exam.model import Banji
from plugin.exam.schema.banji import CreateBanjiParam, UpdateBanjiParam


class CRUDBanji(CRUDPlus[Banji]):
    """班级数据库操作类"""

    async def get(self, db: AsyncSession, pk: int) -> Banji | None:
        """
        获取班级

        :param db: 数据库会话
        :param pk: 班级 ID
        :return:
        """
        return await self.select_model(db, pk)

    async def get_list(self) -> Select:
        """获取班级列表"""
        return await self.select_order('created_time', 'desc')

    async def get_all(self, db: AsyncSession) -> Sequence[Banji]:
        """
        获取所有班级

        :param db: 数据库会话
        :return:
        """
        return await self.select_models(db)

    async def create(self, db: AsyncSession, obj: CreateBanjiParam) -> None:
        """
        创建班级

        :param db: 数据库会话
        :param obj: 创建班级参数
        :return:
        """
        await self.create_model(db, obj)

    async def update(self, db: AsyncSession, pk: int, obj: UpdateBanjiParam) -> int:
        """
        更新班级

        :param db: 数据库会话
        :param pk: 班级 ID
        :param obj: 更新班级参数
        :return:
        """
        return await self.update_model(db, pk, obj)

    async def delete(self, db: AsyncSession, pks: list[int]) -> int:
        """
        批量删除班级

        :param db: 数据库会话
        :param pks: 班级 ID 列表
        :return:
        """
        return await self.delete_model_by_column(db, allow_multiple=True, id__in=pks)


banji_dao: CRUDBanji = CRUDBanji(Banji)