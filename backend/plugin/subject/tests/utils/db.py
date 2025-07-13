#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.subject.crud.crud_subject import subject_dao
from plugin.subject.schema.subject import CreateSubjectParam


async def create_subject_test_data(db: AsyncSession) -> int:
    """
    创建学科测试数据

    :param db: 数据库会话
    :return: 学科 ID
    """
    param = CreateSubjectParam(
        name='测试学科',
        remark='这是一个测试学科'
    )
    subject = await subject_dao.create(db, param)
    return subject.id


async def delete_subject_test_data(db: AsyncSession, subject_id: int) -> None:
    """
    删除学科测试数据

    :param db: 数据库会话
    :param subject_id: 学科 ID
    :return:
    """
    await subject_dao.delete(db, [subject_id])