#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试用户与班级、学科、考试的多对多关系
"""

import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import async_db_session
from app.admin.model import User
from plugin.exam.model import Banji, Subject, Exam


async def test_m2m_relationships():
    """测试多对多关系"""
    async with async_db_session() as db:
        # 查询一个用户
        user = await db.get(User, 1)
        if user:
            print(f"用户: {user.username}")
            
            # 测试用户的班级关系
            print(f"用户的班级数量: {len(user.banjis)}")
            for banji in user.banjis:
                print(f"  - 班级: {banji.name}")
            
            # 测试用户的学科关系
            print(f"用户的学科数量: {len(user.subjects)}")
            for subject in user.subjects:
                print(f"  - 学科: {subject.name}")
            
            # 测试用户的考试关系
            print(f"用户的考试数量: {len(user.exams)}")
            for exam in user.exams:
                print(f"  - 考试: {exam.name}")
        else:
            print("未找到用户")
        
        # 查询一个班级
        banji = await db.get(Banji, 1)
        if banji:
            print(f"\n班级: {banji.name}")
            print(f"班级的用户数量: {len(banji.users)}")
            for user in banji.users:
                print(f"  - 用户: {user.username}")
        
        # 查询一个学科
        subject = await db.get(Subject, 1)
        if subject:
            print(f"\n学科: {subject.name}")
            print(f"学科的用户数量: {len(subject.users)}")
            for user in subject.users:
                print(f"  - 用户: {user.username}")
        
        # 查询一个考试
        exam = await db.get(Exam, 1)
        if exam:
            print(f"\n考试: {exam.name}")
            print(f"考试的用户数量: {len(exam.users)}")
            for user in exam.users:
                print(f"  - 用户: {user.username}")


if __name__ == "__main__":
    asyncio.run(test_m2m_relationships())