#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.exam.tests.utils.exam_question_db import create_exam_question_test_data, delete_exam_question_test_data


@pytest.fixture
async def exam_question_test_data(exam_db: AsyncSession):
    """考试题目测试数据夹具"""
    question_id = await create_exam_question_test_data(exam_db)
    yield question_id
    await delete_exam_question_test_data(exam_db, question_id)


@pytest.fixture
async def exam_question_client(exam_client: AsyncClient):
    """考试题目API客户端夹具"""
    yield exam_client