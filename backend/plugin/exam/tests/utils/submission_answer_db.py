#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from app.admin.model import User
from plugin.exam.model import Exam, ExamQuestion, Submission, SubmissionAnswer


async def create_submission_answer_test_data(db: AsyncSession, include_answers: bool = True) -> dict:
    """创建提交答案测试数据"""
    import uuid
    # 创建测试用户
    unique_id = str(uuid.uuid4())[:8]
    user = User(
        username=f'test_user_{unique_id}',
        nickname='测试用户',
        password='hashed_password',
        salt=b'test_salt',
        email=f'test_{unique_id}@example.com',
        phone='13800138000',
        avatar='',
        is_superuser=False,
        is_staff=False,
        status=1
    )
    db.add(user)
    await db.flush()
    
    # 创建测试考试
    exam = Exam(
        name='测试考试',
        subject='数学',
        banji='一年级一班',
        creator_id=user.id,
        status=1,
        remark='测试考试备注'
    )
    db.add(exam)
    await db.flush()
    
    # 创建测试题目
    exam_question = ExamQuestion(
        exam_id=exam.id,
        question_content='这是一道测试题目',
        question_type='single_choice',
        options={'A': '选项A', 'B': '选项B', 'C': '选项C', 'D': '选项D'},
        correct_answer='A',
        points=10.0,
        sequence=1
    )
    db.add(exam_question)
    await db.flush()
    
    # 创建测试提交
    submission = Submission(
        user_id=user.id,
        exam_id=exam.id,
        start_time=datetime.now(),
        status='in_progress'
    )
    db.add(submission)
    await db.flush()
    
    submission_answer_ids = []
    # 只有在include_answers为True时才创建提交答案
    if include_answers:
        submission_answers = [
            SubmissionAnswer(
                user_id=user.id,
                exam_id=exam.id,
                submission_id=submission.id,
                exam_question_id=exam_question.id,
                answer_content='A',
                is_correct=True,
                score=10.0,
                submitted_at=datetime.now()
            ),
            SubmissionAnswer(
                user_id=user.id,
                exam_id=exam.id,
                submission_id=submission.id,
                exam_question_id=exam_question.id,
                answer_content='B',
                is_correct=False,
                score=0.0,
                submitted_at=datetime.now()
            ),
            SubmissionAnswer(
                user_id=user.id,
                exam_id=exam.id,
                submission_id=submission.id,
                exam_question_id=exam_question.id,
                answer_content='C',
                submitted_at=datetime.now()
            )
        ]
        
        for submission_answer in submission_answers:
            db.add(submission_answer)
        
        await db.flush()
        submission_answer_ids = [sa.id for sa in submission_answers]
    
    await db.commit()
    
    return {
        'user_id': user.id,
        'exam_id': exam.id,
        'submission_id': submission.id,
        'exam_question_id': exam_question.id,
        'submission_answer_ids': submission_answer_ids
    }


async def delete_submission_answer_test_data(db: AsyncSession) -> None:
    """删除提交答案测试数据"""
    from sqlalchemy import text
    
    # 删除提交答案
    await db.execute(text('DELETE FROM submission_answer WHERE user_id IN (SELECT id FROM sys_user WHERE username LIKE "test_user_%")'))
    # 删除提交
    await db.execute(text('DELETE FROM submission WHERE user_id IN (SELECT id FROM sys_user WHERE username LIKE "test_user_%")'))
    # 删除题目
    await db.execute(text('DELETE FROM exam_question WHERE exam_id IN (SELECT id FROM sys_exam WHERE name = "测试考试")'))
    # 删除考试
    await db.execute(text('DELETE FROM sys_exam WHERE name = "测试考试"'))
    # 删除用户
    await db.execute(text('DELETE FROM sys_user WHERE username LIKE "test_user_%"'))
    await db.commit()