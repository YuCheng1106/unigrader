#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import async_db_session
from main import app
from plugin.exam.tests.utils.submission_db import create_submission_test_data, delete_submission_test_data


@pytest.fixture
async def submission_test_data(submission_db: AsyncSession):
    """
    提交测试数据fixture
    """
    submission = await create_submission_test_data(submission_db)
    yield {
        'id': submission.id,
        'user_id': submission.user_id,
        'exam_id': submission.exam_id,
        'status': submission.status
    }
    # 清理测试数据
    await delete_submission_test_data(submission_db, submission.id)


# submission_client fixture is now defined in conftest.py