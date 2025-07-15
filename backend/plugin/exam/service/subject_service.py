#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from common.exception import errors
from database.db import async_db_session
from plugin.exam.crud.crud_subject import subject_dao
from plugin.exam.model.subject import Subject
from plugin.exam.schema.subject import CreateSubjectParam, DeleteSubjectParam, UpdateSubjectParam


class SubjectService:
    """学科服务类"""

    @staticmethod
    async def get(*, pk: int) -> Subject:
        """
        获取学科

        :param pk: 学科 ID
        :return:
        """
        async with async_db_session() as db:
            subject = await subject_dao.get(db, pk)
            if not subject:
                raise errors.NotFoundError(msg='学科不存在')
            return subject

    @staticmethod
    async def get_select(*, name: str | None = None) -> Select:
        """
        获取学科列表查询条件

        :param name: 学科名称
        :return:
        """
        return await subject_dao.get_list(name=name)

    @staticmethod
    async def get_all(*, db: AsyncSession) -> Sequence[Subject]:
        """
        获取所有学科

        :param db: 数据库会话
        :return:
        """
        return await subject_dao.get_all(db)

    @staticmethod
    async def create(*, obj: CreateSubjectParam) -> None:
        """
        创建学科

        :param obj: 创建学科参数
        :return:
        """
        async with async_db_session.begin() as db:
            await subject_dao.create(db, obj)

    @staticmethod
    async def update(*, pk: int, obj: UpdateSubjectParam) -> int:
        """
        更新学科

        :param pk: 学科 ID
        :param obj: 更新学科参数
        :return:
        """
        async with async_db_session.begin() as db:
            count = await subject_dao.update(db, pk, obj)
            if count == 0:
                raise errors.NotFoundError(msg='学科不存在')
            return count

    @staticmethod
    async def delete(*, db: AsyncSession, obj: DeleteSubjectParam) -> int:
        """
        删除学科

        :param db: 数据库会话
        :param obj: 删除学科参数
        :return:
        """
        count = await subject_dao.delete(db, obj.ids)
        if count == 0:
            raise errors.NotFoundError(msg='学科不存在')
        return count


subject_service: SubjectService = SubjectService()