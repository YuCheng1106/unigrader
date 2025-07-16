#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.admin.model import User
from backend.common.security import get_token
from backend.database.db_mysql import async_db_session
from backend.main import app
from .utils.submission_answer_db import create_submission_answer_test_data, delete_submission_answer_test_data


@pytest.fixture(scope='function')
async def submission_answer_test_data():
    """提交答案测试数据fixture"""
    async with async_db_session() as db:
        await create_submission_answer_test_data(db)
        yield
        await delete_submission_answer_test_data(db)


@pytest.fixture(scope='function')
async def submission_answer_client(submission_answer_test_data) -> AsyncClient:
    """提交答案API测试客户端"""
    async with AsyncClient(app=app, base_url='http://test') as client:
        # 创建测试用户并获取token
        async with async_db_session() as db:
            user = await db.get(User, 1)
            if user:
                token = get_token(user.id)
                client.headers.update({'Authorization': f'Bearer {token}'})
        yield client