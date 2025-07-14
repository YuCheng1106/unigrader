#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from common.crud import DalBase
from ..model.submission_answer import SubmissionAnswer
from ..schema.submission_answer import CreateSubmissionAnswerParam, UpdateSubmissionAnswerParam


class SubmissionAnswerDal(DalBase):

    def __init__(self, db: AsyncSession):
        super(SubmissionAnswerDal, self).__init__()
        self.db = db
        self.model = SubmissionAnswer

    async def get_submission_answer_by_id(self, submission_answer_id: int) -> SubmissionAnswer | None:
        """
        通过 id 获取提交答案
        """
        return await self.get_model_by_id(self.db, self.model, submission_answer_id)

    async def get_submission_answers_by_submission_id(self, submission_id: int) -> list[SubmissionAnswer]:
        """
        通过提交ID获取所有答案
        """
        sql = select(self.model).where(self.model.submission_id == submission_id)
        queryset = await self.db.execute(sql)
        return queryset.scalars().all()

    async def get_submission_answers_by_user_id(self, user_id: int) -> list[SubmissionAnswer]:
        """
        通过用户ID获取所有答案
        """
        sql = select(self.model).where(self.model.user_id == user_id)
        queryset = await self.db.execute(sql)
        return queryset.scalars().all()

    async def get_submission_answers_by_exam_id(self, exam_id: int) -> list[SubmissionAnswer]:
        """
        通过考试ID获取所有答案
        """
        sql = select(self.model).where(self.model.exam_id == exam_id)
        queryset = await self.db.execute(sql)
        return queryset.scalars().all()

    async def get_submission_answer_by_user_and_question(self, user_id: int, exam_question_id: int) -> SubmissionAnswer | None:
        """
        通过用户ID和题目ID获取答案
        """
        sql = select(self.model).where(
            self.model.user_id == user_id,
            self.model.exam_question_id == exam_question_id
        )
        queryset = await self.db.execute(sql)
        return queryset.scalars().first()

    async def get_submission_answers_by_grader(self, graded_by_id: int) -> list[SubmissionAnswer]:
        """
        通过批改者ID获取所有批改的答案
        """
        sql = select(self.model).where(self.model.graded_by_id == graded_by_id)
        queryset = await self.db.execute(sql)
        return queryset.scalars().all()

    async def create_submission_answer(self, obj: CreateSubmissionAnswerParam) -> None:
        """
        创建提交答案
        """
        await self.create_model(self.db, self.model, obj)

    async def update_submission_answer(self, submission_answer_id: int, obj: UpdateSubmissionAnswerParam) -> int:
        """
        更新提交答案
        """
        return await self.update_model_by_id(self.db, self.model, submission_answer_id, obj)

    async def delete_submission_answer(self, submission_answer_id: int) -> int:
        """
        删除提交答案
        """
        return await self.delete_model_by_id(self.db, self.model, submission_answer_id)

    async def delete_submission_answers(self, submission_answer_ids: list[int]) -> int:
        """
        批量删除提交答案
        """
        return await self.delete_model_by_ids(self.db, self.model, submission_answer_ids)


submission_answer_dao: SubmissionAnswerDal = SubmissionAnswerDal