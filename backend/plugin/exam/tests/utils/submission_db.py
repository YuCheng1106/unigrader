#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.exam.crud.crud_submission import submission_dao
from plugin.exam.model.submission import Submission
from plugin.exam.schema.submission import CreateSubmissionParam


async def create_submission_test_data(db: AsyncSession, user_id: int = 1, exam_id: int = 1) -> Submission:
    """
    创建提交测试数据

    :param db: 数据库会话
    :param user_id: 用户ID
    :param exam_id: 考试ID
    :return: 创建的提交对象
    """
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
    return await submission_dao.delete(db, [submission_id])