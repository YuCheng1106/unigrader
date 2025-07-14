#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select

from common.exception import errors
from database.db import async_db_session
from plugin.exam.crud.crud_banji import banji_dao
from plugin.exam.model import Banji
from plugin.exam.schema.banji import CreateBanjiParam, DeleteBanjiParam, UpdateBanjiParam


class BanjiService:
    """班级服务类"""

    @staticmethod
    async def get(*, pk: int) -> Banji:
        """
        获取班级

        :param pk: 班级 ID
        :return:
        """
        async with async_db_session() as db:
            banji = await banji_dao.get(db, pk)
            if not banji:
                raise errors.NotFoundError(msg='班级不存在')
            return banji

    @staticmethod
    async def get_select() -> Select:
        """获取班级查询对象"""
        return await banji_dao.get_list()

    @staticmethod
    async def get_all() -> Sequence[Banji]:
        """获取所有班级"""
        async with async_db_session() as db:
            banjis = await banji_dao.get_all(db)
            return banjis

    @staticmethod
    async def create(*, obj: CreateBanjiParam) -> None:
        """
        创建班级

        :param obj: 创建班级参数
        :return:
        """
        async with async_db_session.begin() as db:
            await banji_dao.create(db, obj)

    @staticmethod
    async def update(*, pk: int, obj: UpdateBanjiParam) -> int:
        """
        更新班级

        :param pk: 班级 ID
        :param obj: 更新班级参数
        :return:
        """
        async with async_db_session.begin() as db:
            banji = await banji_dao.get(db, pk)
            if not banji:
                raise errors.NotFoundError(msg='班级不存在')
            count = await banji_dao.update(db, pk, obj)
            return count

    @staticmethod
    async def delete(*, obj: DeleteBanjiParam) -> int:
        """
        批量删除班级

        :param obj: 班级 ID 列表
        :return:
        """
        async with async_db_session.begin() as db:
            count = await banji_dao.delete(db, obj.pks)
            return count


banji_service: BanjiService = BanjiService()