#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Sequence

from sqlalchemy import Select

from app.admin.crud.crud_user import user_dao
from common.exception import errors
from database.db import async_db_session
from plugin.campus.crud.crud_student import student_dao
from plugin.campus.model import Student
from plugin.campus.schema.student import CreateStudentParam, DeleteStudentParam, UpdateStudentParam


class StudentService:
    """学生信息服务类"""

    @staticmethod
    async def get(*, pk: int) -> Student:
        """
        获取学生信息

        :param pk: 学生信息 ID
        :return:
        """
        async with async_db_session() as db:
            student = await student_dao.get(db, pk)
            if not student:
                raise errors.NotFoundError(msg='学生信息不存在')
            return student

    @staticmethod
    async def get_by_number(*, student_number: str) -> Student:
        """
        通过学号获取学生信息

        :param student_number: 学生信息 ID
        :return:
        """
        async with async_db_session() as db:
            student = await student_dao.get_by_student_number(db, student_number)
            if not student:
                raise errors.NotFoundError(msg='学生信息不存在')
            return student

    @staticmethod
    async def get_select() -> Select:
        """获取学生信息查询对象"""
        return await student_dao.get_list()

    @staticmethod
    async def get_all() -> Sequence[Student]:
        """获取所有学生信息"""
        async with async_db_session() as db:
            students = await student_dao.get_all(db)
            return students

    @staticmethod
    async def create(*, obj: CreateStudentParam) -> None:
        """
        创建学生信息

        :param obj: 创建学生信息参数
        :return:
        """
        async with async_db_session.begin() as db:
            await student_dao.create(db, obj)

    @staticmethod
    async def update(*, pk: int, obj: UpdateStudentParam) -> int:
        """
        更新学生信息

        :param pk: 学生信息 ID
        :param obj: 更新学生信息参数
        :return:
        """
        async with async_db_session.begin() as db:
            student = await student_dao.get(db, pk)
            if not student:
                raise errors.NotFoundError(msg='学生信息不存在')
            count = await student_dao.update(db, pk, obj)
            return count

    @staticmethod
    async def delete(*, obj: DeleteStudentParam) -> int:
        """
        批量删除学生信息

        :param obj: 学生信息 ID 列表
        :return:
        """
        async with async_db_session.begin() as db:
            count = await student_dao.delete(db, obj.pks)
            return count

    @staticmethod
    async def check_student_number(*, school_id: int, student_number: str) -> bool:
        """
        批量删除学生信息

        :param school_id: 学校 ID
        :param student_number: 学号
        :return:
        """
        async with async_db_session.begin() as db:
            student = await student_dao.get_by_student_number(db, school_id, student_number)
            if student is not None:
                return True
            else:
                return False

student_service: StudentService = StudentService()
