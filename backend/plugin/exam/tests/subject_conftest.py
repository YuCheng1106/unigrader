#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from tests.conftest import async_client, async_db_session


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'


@pytest.fixture
async def subject_client(async_client: AsyncClient) -> AsyncClient:
    return async_client


@pytest.fixture
async def subject_db(async_db_session: AsyncSession) -> AsyncSession:
    return async_db_session