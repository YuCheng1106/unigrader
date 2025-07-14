#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy import select

from app.admin.model import User
from plugin.exam.model import Exam, Banji, Subject
from database.db import async_db_session


class TestM2MRelationships:
    """测试多对多关系"""

    @pytest.mark.asyncio
    async def test_user_exam_relationship(self):
        """测试用户-考试多对多关系"""
        async with async_db_session() as db:
            # 创建测试数据
            user = User(
                username='test_student',
                nickname='测试学生',
                email='student@test.com',
                phone='13800138001',
                avatar='',
                is_superuser=False,
                is_staff=False,
                status=1
            )
            db.add(user)
            await db.flush()

            exam = Exam(
                name='测试考试',
                subject='数学',
                banji='测试班级',
                creator_id=user.id,
                status=1
            )
            db.add(exam)
            await db.flush()

            # 建立多对多关系
            user.exams.append(exam)
            await db.commit()

            # 验证关系
            stmt = select(User).options(selectinload(User.exams)).where(User.id == user.id)
            result = await db.execute(stmt)
            user_with_exams = result.scalar_one()
            
            assert len(user_with_exams.exams) == 1
            assert user_with_exams.exams[0].name == '测试考试'

            # 清理测试数据
            await db.delete(user)
            await db.delete(exam)
            await db.commit()

    @pytest.mark.asyncio
    async def test_banji_exam_relationship(self):
        """测试班级-考试多对多关系"""
        async with async_db_session() as db:
            # 创建测试数据
            banji = Banji(
                name='测试班级',
                remark='这是一个测试班级'
            )
            db.add(banji)
            await db.flush()

            exam = Exam(
                name='班级考试',
                subject='语文',
                banji='测试班级',
                status=1
            )
            db.add(exam)
            await db.flush()

            # 建立多对多关系
            banji.exams.append(exam)
            await db.commit()

            # 验证关系
            stmt = select(Banji).options(selectinload(Banji.exams)).where(Banji.id == banji.id)
            result = await db.execute(stmt)
            banji_with_exams = result.scalar_one()
            
            assert len(banji_with_exams.exams) == 1
            assert banji_with_exams.exams[0].name == '班级考试'

            # 清理测试数据
            await db.delete(banji)
            await db.delete(exam)
            await db.commit()



    @pytest.mark.asyncio
    async def test_teacher_subject_relationship(self):
        """测试教师-学科多对多关系"""
        async with async_db_session() as db:
            # 创建测试数据
            teacher = User(
                username='test_teacher',
                nickname='测试教师',
                email='teacher@test.com',
                phone='13800138002',
                avatar='',
                is_superuser=False,
                is_staff=True,
                status=1
            )
            db.add(teacher)
            await db.flush()

            subject = Subject(
                name='英语',
                remark='英语学科'
            )
            db.add(subject)
            await db.flush()

            # 建立多对多关系
            teacher.teaching_subjects.append(subject)
            await db.commit()

            # 验证关系
            stmt = select(User).options(selectinload(User.teaching_subjects)).where(User.id == teacher.id)
            result = await db.execute(stmt)
            teacher_with_subjects = result.scalar_one()
            
            assert len(teacher_with_subjects.teaching_subjects) == 1
            assert teacher_with_subjects.teaching_subjects[0].name == '英语'

            # 清理测试数据
            await db.delete(teacher)
            await db.delete(subject)
            await db.commit()

    @pytest.mark.asyncio
    async def test_user_banji_relationship(self):
        """测试用户-班级多对多关系"""
        async with async_db_session() as db:
            # 创建测试数据
            student = User(
                username='test_student2',
                nickname='测试学生2',
                email='student2@test.com',
                phone='13800138003',
                avatar='',
                is_superuser=False,
                is_staff=False,
                status=1
            )
            db.add(student)
            await db.flush()

            banji = Banji(
                name='测试班级2',
                remark='这是另一个测试班级'
            )
            db.add(banji)
            await db.flush()

            # 建立多对多关系
            student.banjis.append(banji)
            await db.commit()

            # 验证关系
            stmt = select(User).options(selectinload(User.banjis)).where(User.id == student.id)
            result = await db.execute(stmt)
            student_with_banjis = result.scalar_one()
            
            assert len(student_with_banjis.banjis) == 1
            assert student_with_banjis.banjis[0].name == '测试班级2'

            # 清理测试数据
            await db.delete(student)
            await db.delete(banji)
            await db.commit()