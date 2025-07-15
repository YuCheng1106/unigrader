#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_crud_plus import CRUDPlus

from ..model.submission_answer import SubmissionAnswer
from ..schema.submission_answer import CreateSubmissionAnswerParam, UpdateSubmissionAnswerParam


class SubmissionAnswerDal(CRUDPlus[SubmissionAnswer]):
    """提交答案数据库操作类"""

    async def get(self, db: AsyncSession, pk: int) -> SubmissionAnswer | None:
        """
        通过 id 获取提交答案
        """
        return await self.select_model(db, pk)

    async def get_submission_answers_by_submission_id(self, db: AsyncSession, submission_id: int) -> list[SubmissionAnswer]:
        """
        通过提交ID获取所有答案
        """
        sql = select(SubmissionAnswer).where(SubmissionAnswer.submission_id == submission_id)
        queryset = await db.execute(sql)
        return queryset.scalars().all()

    async def get_submission_answers_by_user_id(self, db: AsyncSession, user_id: int) -> list[SubmissionAnswer]:
        """
        通过用户ID获取所有答案
        """
        sql = select(SubmissionAnswer).where(SubmissionAnswer.user_id == user_id)
        queryset = await db.execute(sql)
        return queryset.scalars().all()

    async def get_submission_answers_by_exam_id(self, db: AsyncSession, exam_id: int) -> list[SubmissionAnswer]:
        """
        通过考试ID获取所有答案
        """
        sql = select(SubmissionAnswer).where(SubmissionAnswer.exam_id == exam_id)
        queryset = await db.execute(sql)
        return queryset.scalars().all()

    async def get_submission_answer_by_user_and_question(self, db: AsyncSession, user_id: int, exam_question_id: int) -> SubmissionAnswer | None:
        """
        通过用户ID和题目ID获取答案
        """
        sql = select(SubmissionAnswer).where(
            SubmissionAnswer.user_id == user_id,
            SubmissionAnswer.exam_question_id == exam_question_id
        )
        queryset = await db.execute(sql)
        return queryset.scalars().first()

    async def get_submission_answers_by_grader(self, db: AsyncSession, graded_by_id: int) -> list[SubmissionAnswer]:
        """
        通过批改者ID获取所有批改的答案
        """
        sql = select(SubmissionAnswer).where(SubmissionAnswer.graded_by_id == graded_by_id)
        queryset = await db.execute(sql)
        return queryset.scalars().all()

    async def create(self, db: AsyncSession, obj: CreateSubmissionAnswerParam) -> SubmissionAnswer:
        """
        创建提交答案
        """
        return await self.create_model(db, obj)

    async def update(self, db: AsyncSession, pk: int, obj: UpdateSubmissionAnswerParam) -> int:
        """
        更新提交答案
        """
        return await self.update_model(db, pk, obj)

    async def delete(self, db: AsyncSession, pk: int) -> int:
        """
        删除提交答案
        """
        return await self.delete_model(db, pk)

    async def delete_submission_answers(self, db: AsyncSession, submission_answer_ids: list[int]) -> int:
        """
        批量删除提交答案
        """
        return await self.delete_model_by_column(db, allow_multiple=True, id__in=submission_answer_ids)


submission_answer_dao = SubmissionAnswerDal(SubmissionAnswer)