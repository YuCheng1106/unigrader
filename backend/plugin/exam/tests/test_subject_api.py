#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.exam.tests.utils.subject_db import create_subject_test_data, delete_subject_test_data
from plugin.exam.tests.utils.login_auth import get_token


class TestSubjectAPI:
    """学科 API 测试"""

    async def test_create_subject(self, exam_client: AsyncClient):
        """测试创建学科"""
        response = await exam_client.post(
            '/api/v1/subjects',
            json={
                'name': '数学',
                'remark': '数学学科'
            }
        )
        assert response.status_code == 200
        assert response.json()['code'] == 200

    async def test_get_subject_detail(self, exam_client: AsyncClient, subject_db: AsyncSession):
        """测试获取学科详情"""
        # 创建测试数据
        subject_id = await create_subject_test_data(subject_db)
        assert subject_id is not None, f"subject_id should not be None, got {subject_id}"
        assert isinstance(subject_id, int), f"subject_id should be int, got {type(subject_id)}: {subject_id}"
        
        response = await exam_client.get(
            f'/api/v1/subjects/{subject_id}'
        )
        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text}")
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        assert data['data']['id'] == subject_id
        assert data['data']['name'] == '测试学科'
        
        # 清理测试数据
        await delete_subject_test_data(subject_db, subject_id)

    async def test_get_subjects_paged(self, exam_client: AsyncClient, subject_db: AsyncSession):
        """测试分页获取学科列表"""
        # 创建测试数据
        subject_id = await create_subject_test_data(subject_db)
        
        response = await exam_client.get(
            '/api/v1/subjects?page=1&size=10'
        )
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        assert 'data' in data
        assert 'items' in data['data']
        
        # 清理测试数据
        await delete_subject_test_data(subject_db, subject_id)

    async def test_update_subject(self, exam_client: AsyncClient, subject_db: AsyncSession):
        """测试更新学科"""
        # 创建测试数据
        subject_id = await create_subject_test_data(subject_db)
        
        response = await exam_client.put(
            f'/api/v1/subjects/{subject_id}',
            json={
                'name': '更新后的学科',
                'remark': '更新后的备注'
            }
        )
        assert response.status_code == 200
        assert response.json()['code'] == 200
        
        # 清理测试数据
        await delete_subject_test_data(subject_db, subject_id)

    async def test_delete_subjects(self, exam_client: AsyncClient, subject_db: AsyncSession):
        """测试批量删除学科"""
        # 创建测试数据
        subject_id = await create_subject_test_data(subject_db)
        print(f"Created subject_id: {subject_id}")
        print(f"Type of subject_id: {type(subject_id)}")
        
        request_data = {'ids': [subject_id]}
        print(f"Request data: {request_data}")
        
        response = await exam_client.request(
            'DELETE',
            '/api/v1/subjects',
            json=request_data
        )
        print(f"Response status: {response.status_code}")
        print(f"Response text: {response.text}")
        if response.status_code != 200:
            print(f"Error details: {response.json()}")
        assert response.status_code == 200, f"Expected 200, got {response.status_code}. Response: {response.text}"
        assert response.json()['code'] == 200