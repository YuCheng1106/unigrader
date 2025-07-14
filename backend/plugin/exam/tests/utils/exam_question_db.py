#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.exam.crud.crud_exam_question import exam_question_dao
from plugin.exam.schema.exam_question import CreateExamQuestionParam


async def create_exam_question_test_data(db: AsyncSession) -> int:
    """创建考试题目测试数据"""
    exam_question_data = CreateExamQuestionParam(
        exam_id=1,
        question_type='single_choice',
        question_content='测试题目内容',
        options={'A': '选项A', 'B': '选项B', 'C': '选项C', 'D': '选项D'},
        correct_answer='A',
        points=10.0,
        sequence=1
    )
    exam_question = await exam_question_dao.create(db, exam_question_data)
    await db.commit()
    return exam_question.id


async def delete_exam_question_test_data(db: AsyncSession, question_id: int):
    """删除考试题目测试数据"""
    await exam_question_dao.delete(db, question_id)
    await db.commit()