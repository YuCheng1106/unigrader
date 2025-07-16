#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from httpx import AsyncClient

# 测试用户凭据
PYTEST_USERNAME = 'admin'
PYTEST_PASSWORD = '123456'


async def get_token(client: AsyncClient) -> str:
    """获取测试用的认证token"""
    params = {
        'username': PYTEST_USERNAME,
        'password': PYTEST_PASSWORD,
    }
    response = await client.post('/api/v1/auth/login/swagger', params=params)
    if response.status_code != 200:
        raise Exception(f"Login failed: {response.status_code} - {response.text}")
    
    token_data = response.json()
    return token_data['access_token']