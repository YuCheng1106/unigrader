#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Generator

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.testclient import TestClient

# from app.admin.tests.utils.db import override_get_db
from core.conf import settings
from database.db import get_db
from main import app
from plugin.exam.tests.utils.db import override_get_db as exam_override_get_db

# 重载数据库 - 使用exam插件的数据库覆盖
app.dependency_overrides[get_db] = exam_override_get_db


# Test data
PYTEST_USERNAME = 'admin'
PYTEST_PASSWORD = '123456'
PYTEST_BASE_URL = 'http://testserver'


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'


@pytest.fixture(scope='module')
def client() -> Generator:
    with TestClient(app, base_url=PYTEST_BASE_URL) as c:
        yield c


@pytest.fixture(scope='module')
def token_headers(client: TestClient) -> dict[str, str]:
    params = {
        'username': PYTEST_USERNAME,
        'password': PYTEST_PASSWORD,
    }
    response = client.post('/api/v1/auth/login/swagger', params=params)
    response.raise_for_status()
    token_type = response.json()['token_type']
    access_token = response.json()['access_token']
    headers = {'Authorization': f'{token_type} {access_token}'}
    return headers


# Exam plugin specific fixtures
@pytest.fixture(scope='function')
async def exam_client() -> AsyncClient:
    from plugin.exam.tests.utils.login_auth import get_token
    async with AsyncClient(app=app, base_url=PYTEST_BASE_URL) as ac:
        # 获取认证token
        token = await get_token(ac)
        # 设置认证头
        ac.headers.update({'Authorization': f'Bearer {token}'})
        yield ac


@pytest.fixture(scope='function')
async def exam_db() -> AsyncSession:
    async for session in exam_override_get_db():
        yield session


@pytest.fixture(scope='function')
async def subject_client() -> AsyncClient:
    async with AsyncClient(app=app, base_url=PYTEST_BASE_URL) as ac:
        yield ac


@pytest.fixture(scope='function')
async def subject_db() -> AsyncSession:
    async for session in exam_override_get_db():
        yield session


@pytest.fixture(scope='function')
async def banji_client() -> AsyncClient:
    async with AsyncClient(app=app, base_url=PYTEST_BASE_URL) as ac:
        yield ac


@pytest.fixture(scope='function')
async def banji_db() -> AsyncSession:
    async for session in exam_override_get_db():
        yield session


@pytest.fixture(scope='function')
async def exam_question_client() -> AsyncClient:
    async with AsyncClient(app=app, base_url=PYTEST_BASE_URL) as ac:
        yield ac


@pytest.fixture(scope='function')
async def exam_question_db() -> AsyncSession:
    async for session in exam_override_get_db():
        yield session


@pytest.fixture(scope='function')
async def submission_client() -> AsyncClient:
    from plugin.exam.tests.utils.login_auth import get_token
    async with AsyncClient(app=app, base_url=PYTEST_BASE_URL) as ac:
        # 获取认证token
        token = await get_token(ac)
        # 设置认证头
        ac.headers.update({'Authorization': f'Bearer {token}'})
        yield ac


@pytest.fixture(scope='function')
async def submission_db() -> AsyncSession:
    async for session in exam_override_get_db():
        yield session


@pytest.fixture(scope='function')
async def submission_answer_client() -> AsyncClient:
    from plugin.exam.tests.utils.login_auth import get_token
    async with AsyncClient(app=app, base_url=PYTEST_BASE_URL) as ac:
        # 获取认证token
        token = await get_token(ac)
        # 设置认证头
        ac.headers.update({'Authorization': f'Bearer {token}'})
        yield ac


@pytest.fixture(scope='function')
async def submission_answer_db() -> AsyncSession:
    async for session in exam_override_get_db():
        yield session



