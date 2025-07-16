#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.exam.crud.crud_exam_question import exam_question_dao
from plugin.exam.schema.exam_question import CreateExamQuestionParam


async def create_exam_question_test_data(db: AsyncSession) -> tuple[int, int]:
    """创建考试题目测试数据"""
    # 先创建一个考试记录
    from plugin.exam.model import Exam
    
    exam = Exam(
        name='测试考试',
        status=1,
        remark='这是一个测试考试',
        creator_id=1,
        subject='数学',
        banji='一年级一班'
    )
    db.add(exam)
    await db.commit()
    await db.refresh(exam)
    
    # 创建考试题目
    from plugin.exam.model.exam_question import ExamQuestion
    
    exam_question = ExamQuestion(
        exam_id=exam.id,
        question_type='single_choice',
        question_content='测试题目内容',
        options={'A': '选项A', 'B': '选项B', 'C': '选项C', 'D': '选项D'},
        correct_answer='A',
        points=10.0,
        sequence=1
    )
    db.add(exam_question)
    await db.commit()
    await db.refresh(exam_question)
    return exam_question.id, exam.id


async def delete_exam_question_test_data(db: AsyncSession, question_id: int):
    """删除考试题目测试数据"""
    await exam_question_dao.delete(db, [question_id])
    await db.commit()