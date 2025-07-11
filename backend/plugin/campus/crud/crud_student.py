#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.sql import Select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from app.admin.model import User
from plugin.campus.model import Student
from plugin.campus.schema.student import CreateStudentParam, UpdateStudentParam


class CRUDStudent(CRUDPlus[Student]):
    """学生信息数据库操作类"""

    async def get(self, db: AsyncSession, pk: int) -> Student | None:
        """
        获取学生信息

        :param db: 数据库会话
        :param pk: 学生信息 ID
        :return:
        """
        return await self.select_model(db, pk)

    async def get_by_student_number(self, db: AsyncSession, school_id: int, student_number: str) -> Student | None:
        """
        通过学号获取学生信息

        :param db: 数据库会话
        :param school_id: 学校 ID
        :param student_number: 学号
        :return:
        """
        return await self.select_model_by_column(db, student_number=student_number, school_id=school_id )

    async def get_list(self) -> Select:
        """获取学生信息列表"""
        return await self.select_order('created_time', 'desc')

    async def get_all(self, db: AsyncSession) -> Sequence[Student]:
        """
        获取所有学生信息

        :param db: 数据库会话
        :return:
        """
        return await self.select_models(db)

    async def add(self, db: AsyncSession, obj: CreateStudentParam) -> None:
        """
        添加学生

        :param db: 数据库会话
        :param obj: 添加用户参数
        :return:
        """
        dict_obj = obj.model_dump(exclude={'user'})
        new_student = self.model(**dict_obj)

        stmt = select(User).where(User.id == obj.user_id)
        user = await db.execute(stmt)
        new_student.user = user.scalars().first()

        db.add(new_student)

    async def create(self, db: AsyncSession, obj: CreateStudentParam) -> None:
        """
        创建学生信息

        :param db: 数据库会话
        :param obj: 创建学生信息参数
        :return:
        """

        await self.create_model(db, obj)

    async def update(self, db: AsyncSession, pk: int, obj: UpdateStudentParam) -> int:
        """
        更新学生信息

        :param db: 数据库会话
        :param pk: 学生信息 ID
        :param obj: 更新学生信息参数
        :return:
        """
        return await self.update_model(db, pk, obj)

    async def delete(self, db: AsyncSession, pks: list[int]) -> int:
        """
        批量删除学生信息

        :param db: 数据库会话
        :param pks: 学生信息 ID 列表
        :return:
        """
        return await self.delete_model_by_column(db, allow_multiple=True, id__in=pks)


student_dao: CRUDStudent = CRUDStudent(Student)
