#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy.ext.asyncio import AsyncSession

from common.exception import errors
from common.pagination import PageData
from ..crud.crud_submission_answer import submission_answer_dao
from ..model.submission_answer import SubmissionAnswer
from ..schema.submission_answer import (
    CreateSubmissionAnswerParam,
    UpdateSubmissionAnswerParam,
    GetSubmissionAnswerDetail
)


class SubmissionAnswerService:
    """
    提交答案服务类
    """

    @staticmethod
    async def get_submission_answer_by_id(db: AsyncSession, submission_answer_id: int) -> GetSubmissionAnswerDetail:
        """
        通过ID获取提交答案详情
        """
        submission_answer_obj: SubmissionAnswer = await submission_answer_dao.get(db, submission_answer_id)
        if not submission_answer_obj:
            raise errors.NotFoundError(msg='提交答案不存在')
        return GetSubmissionAnswerDetail.model_validate(submission_answer_obj)

    @staticmethod
    async def get_submission_answers_by_submission_id(db: AsyncSession, submission_id: int) -> list[GetSubmissionAnswerDetail]:
        """
        通过提交ID获取所有答案
        """
        submission_answers = await submission_answer_dao.get_submission_answers_by_submission_id(db, submission_id)
        return [GetSubmissionAnswerDetail.model_validate(answer) for answer in submission_answers]

    @staticmethod
    async def get_submission_answers_by_user_id(db: AsyncSession, user_id: int) -> list[GetSubmissionAnswerDetail]:
        """
        通过用户ID获取所有答案
        """
        submission_answers = await submission_answer_dao.get_submission_answers_by_user_id(db, user_id)
        return [GetSubmissionAnswerDetail.model_validate(answer) for answer in submission_answers]

    @staticmethod
    async def get_submission_answers_by_exam_id(db: AsyncSession, exam_id: int) -> list[GetSubmissionAnswerDetail]:
        """
        通过考试ID获取所有答案
        """
        submission_answers = await submission_answer_dao.get_submission_answers_by_exam_id(db, exam_id)
        return [GetSubmissionAnswerDetail.model_validate(answer) for answer in submission_answers]

    @staticmethod
    async def get_submission_answer_by_user_and_question(db: AsyncSession, user_id: int, exam_question_id: int) -> GetSubmissionAnswerDetail | None:
        """
        通过用户ID和题目ID获取答案
        """
        submission_answer = await submission_answer_dao.get_submission_answer_by_user_and_question(db, user_id, exam_question_id)
        if not submission_answer:
            return None
        return GetSubmissionAnswerDetail.model_validate(submission_answer)

    @staticmethod
    async def get_submission_answers_by_grader(db: AsyncSession, graded_by_id: int) -> list[GetSubmissionAnswerDetail]:
        """
        通过批改者ID获取所有批改的答案
        """
        submission_answers = await submission_answer_dao.get_submission_answers_by_grader(db, graded_by_id)
        return [GetSubmissionAnswerDetail.model_validate(answer) for answer in submission_answers]

    @staticmethod
    async def create_submission_answer(db: AsyncSession, obj: CreateSubmissionAnswerParam) -> None:
        """
        创建提交答案
        """
        # 检查是否已存在相同用户和题目的答案
        existing_answer = await submission_answer_dao.get_submission_answer_by_user_and_question(
            db, obj.user_id, obj.exam_question_id
        )
        if existing_answer:
            raise errors.ForbiddenError(msg='该用户已提交过此题目的答案')
        
        await submission_answer_dao.create(db, obj)

    @staticmethod
    async def update_submission_answer(db: AsyncSession, submission_answer_id: int, obj: UpdateSubmissionAnswerParam) -> int:
        """
        更新提交答案
        """
        count = await submission_answer_dao.update(db, submission_answer_id, obj)
        if count == 0:
            raise errors.NotFoundError(msg='提交答案不存在')
        return count

    @staticmethod
    async def delete_submission_answer(db: AsyncSession, submission_answer_id: int) -> int:
        """
        删除提交答案
        """
        count = await submission_answer_dao.delete(db, submission_answer_id)
        if count == 0:
            raise errors.NotFoundError(msg='提交答案不存在')
        return count

    @staticmethod
    async def delete_submission_answers(db: AsyncSession, submission_answer_ids: list[int]) -> int:
        """
        批量删除提交答案
        """
        count = await submission_answer_dao.delete_submission_answers(db, submission_answer_ids)
        return count


submission_answer_service = SubmissionAnswerService()