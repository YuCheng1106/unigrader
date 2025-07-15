#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy.ext.asyncio import AsyncSession

from app.admin.model import User
from plugin.exam.model import Exam
from plugin.exam.crud.crud_submission import submission_dao
from plugin.exam.model.submission import Submission
from plugin.exam.schema.submission import CreateSubmissionParam


async def create_submission_test_data(db: AsyncSession, user_id: int = None, exam_id: int = None) -> Submission:
    """
    创建提交测试数据

    :param db: 数据库会话
    :param user_id: 用户ID（可选，如果不提供则创建新用户）
    :param exam_id: 考试ID（可选，如果不提供则创建新考试）
    :return: 创建的提交对象
    """
    # 创建或获取测试用户
    if user_id is not None:
        user = await db.get(User, user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
    else:
        # 创建新的测试用户
        import uuid
        unique_suffix = str(uuid.uuid4())[:8]
        user = User(
            username=f'test_user_{unique_suffix}',
            nickname='测试用户',
            password='test_password',
            salt=b'test_salt',
            email=f'test_{unique_suffix}@example.com',
            phone='13800138000',
            avatar='',
            is_superuser=False,
            is_staff=False,
            status=1
        )
        db.add(user)
        await db.flush()
        await db.refresh(user)
        user_id = user.id
    
    # 创建或获取测试考试
    if exam_id is not None:
        exam = await db.get(Exam, exam_id)
        if not exam:
            raise ValueError(f"Exam with id {exam_id} not found")
    else:
        # 创建新的测试考试
        import uuid
        unique_suffix = str(uuid.uuid4())[:8]
        exam = Exam(
            name=f'测试考试_{unique_suffix}',
            status=1,
            remark='这是一个测试考试',
            creator_id=user_id,
            subject='数学',
            banji='一年级一班'
        )
        db.add(exam)
        await db.flush()
        await db.refresh(exam)
        exam_id = exam.id
    
    # 创建提交数据
    submission_data = CreateSubmissionParam(
        user_id=user_id,
        exam_id=exam_id,
        status='not_started'
    )
    return await submission_dao.create(db, submission_data)


async def delete_submission_test_data(db: AsyncSession, submission_id: int) -> int:
    """
    删除提交测试数据

    :param db: 数据库会话
    :param submission_id: 提交ID
    :return: 删除的记录数
    """
    from sqlalchemy import text, select
    
    # 首先获取提交记录以获取相关的用户ID和考试ID
    submission_result = await db.execute(
        text('SELECT user_id, exam_id FROM submission WHERE id = :submission_id'),
        {'submission_id': submission_id}
    )
    submission_row = submission_result.fetchone()
    
    if submission_row:
        user_id, exam_id = submission_row
        
        # 删除提交数据
        result = await submission_dao.delete(db, [submission_id])
        
        # 清理测试数据（删除测试用户和考试）
        # 只删除以 test_ 开头的用户和考试，避免删除其他数据
        await db.execute(
            text('DELETE FROM sys_exam WHERE id = :exam_id AND name LIKE "测试考试_%"'),
            {'exam_id': exam_id}
        )
        await db.execute(
            text('DELETE FROM sys_user WHERE id = :user_id AND username LIKE "test_user_%"'),
            {'user_id': user_id}
        )
        await db.commit()
        
        return result
    else:
        # 如果提交记录不存在，直接返回0
        return 0