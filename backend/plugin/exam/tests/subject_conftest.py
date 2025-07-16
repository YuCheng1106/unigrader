#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.exam.tests.conftest import subject_client, subject_db


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'