#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.exam.crud.crud_banji import banji_dao
from plugin.exam.schema.banji import CreateBanjiParam


async def create_banji_test_data(db: AsyncSession) -> int:
    """
    创建班级测试数据

    :param db: 数据库会话
    :return: 班级 ID
    """
    banji_data = CreateBanjiParam(
        name='测试班级',
        remark='这是一个测试班级'
    )
    await banji_dao.create(db, banji_data)
    banji = await banji_dao.get_by_column(db, name='测试班级')
    return banji.id


async def delete_banji_test_data(db: AsyncSession, banji_id: int) -> None:
    """
    删除班级测试数据

    :param db: 数据库会话
    :param banji_id: 班级 ID
    :return:
    """
    await banji_dao.delete(db, [banji_id])