#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.admin.model import User
from plugin.exam.model import Exam, ExamQuestion, Submission, SubmissionAnswer


async def create_submission_answer_test_data(db: AsyncSession) -> None:
    """创建提交答案测试数据"""
    # 创建测试用户
    user = User(
        username='test_user',
        nickname='测试用户',
        email='test@example.com',
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
        exam_name='测试考试',
        exam_desc='这是一个测试考试',
        exam_time=120,
        total_score=100.0,
        pass_score=60.0,
        exam_type='online',
        status='published'
    )
    db.add(exam)
    await db.flush()
    
    # 创建测试题目
    exam_question = ExamQuestion(
        exam_id=exam.id,
        question_text='这是一道测试题目',
        question_type='single_choice',
        options='A.选项A\nB.选项B\nC.选项C\nD.选项D',
        correct_answer='A',
        score=10.0,
        difficulty='medium'
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
    
    # 创建测试提交答案
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
    
    await db.commit()


async def delete_submission_answer_test_data(db: AsyncSession) -> None:
    """删除提交答案测试数据"""
    # 删除提交答案
    await db.execute('DELETE FROM submission_answer WHERE id > 0')
    # 删除提交
    await db.execute('DELETE FROM submission WHERE id > 0')
    # 删除题目
    await db.execute('DELETE FROM exam_question WHERE id > 0')
    # 删除考试
    await db.execute('DELETE FROM exam WHERE id > 0')
    # 删除用户
    await db.execute('DELETE FROM sys_user WHERE username = "test_user"')
    await db.commit()