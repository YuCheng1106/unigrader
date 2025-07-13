#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.subject.tests.utils.db import create_subject_test_data, delete_subject_test_data
from tests.utils.login_auth import get_token


class TestSubjectAPI:
    """学科 API 测试"""

    async def test_create_subject(self, subject_client: AsyncClient):
        """测试创建学科"""
        token = await get_token(subject_client)
        headers = {'Authorization': f'Bearer {token}'}
        
        response = await subject_client.post(
            '/api/v1/subjects',
            json={
                'name': '数学',
                'remark': '数学学科'
            },
            headers=headers
        )
        assert response.status_code == 200
        assert response.json()['code'] == 200

    async def test_get_subject_detail(self, subject_client: AsyncClient, subject_db: AsyncSession):
        """测试获取学科详情"""
        # 创建测试数据
        subject_id = await create_subject_test_data(subject_db)
        
        token = await get_token(subject_client)
        headers = {'Authorization': f'Bearer {token}'}
        
        response = await subject_client.get(
            f'/api/v1/subjects/{subject_id}',
            headers=headers
        )
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        assert data['data']['id'] == subject_id
        assert data['data']['name'] == '测试学科'
        
        # 清理测试数据
        await delete_subject_test_data(subject_db, subject_id)

    async def test_get_subjects_paged(self, subject_client: AsyncClient, subject_db: AsyncSession):
        """测试分页获取学科列表"""
        # 创建测试数据
        subject_id = await create_subject_test_data(subject_db)
        
        token = await get_token(subject_client)
        headers = {'Authorization': f'Bearer {token}'}
        
        response = await subject_client.get(
            '/api/v1/subjects?page=1&size=10',
            headers=headers
        )
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        assert 'data' in data
        assert 'items' in data['data']
        
        # 清理测试数据
        await delete_subject_test_data(subject_db, subject_id)

    async def test_update_subject(self, subject_client: AsyncClient, subject_db: AsyncSession):
        """测试更新学科"""
        # 创建测试数据
        subject_id = await create_subject_test_data(subject_db)
        
        token = await get_token(subject_client)
        headers = {'Authorization': f'Bearer {token}'}
        
        response = await subject_client.put(
            f'/api/v1/subjects/{subject_id}',
            json={
                'name': '更新后的学科',
                'remark': '更新后的备注'
            },
            headers=headers
        )
        assert response.status_code == 200
        assert response.json()['code'] == 200
        
        # 清理测试数据
        await delete_subject_test_data(subject_db, subject_id)

    async def test_delete_subjects(self, subject_client: AsyncClient, subject_db: AsyncSession):
        """测试批量删除学科"""
        # 创建测试数据
        subject_id = await create_subject_test_data(subject_db)
        
        token = await get_token(subject_client)
        headers = {'Authorization': f'Bearer {token}'}
        
        response = await subject_client.delete(
            '/api/v1/subjects',
            json={'ids': [subject_id]},
            headers=headers
        )
        assert response.status_code == 200
        assert response.json()['code'] == 200