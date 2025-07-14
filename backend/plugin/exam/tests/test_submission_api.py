#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.exam.schema.submission import CreateSubmissionParam, UpdateSubmissionParam
from plugin.exam.tests.utils.submission_db import create_submission_test_data, delete_submission_test_data


class TestSubmissionAPI:
    """提交API测试"""

    async def test_create_submission(self, submission_client: AsyncClient):
        """测试创建提交"""
        json_data = {
            'user_id': 1,
            'exam_id': 1,
            'status': 'not_started'
        }
        response = await submission_client.post('/api/v1/sys/submission', json=json_data)
        assert response.status_code == 200
        assert response.json()['code'] == 200
        data = response.json()['data']
        assert data['user_id'] == 1
        assert data['exam_id'] == 1
        assert data['status'] == 'not_started'

    async def test_get_submission(self, submission_client: AsyncClient, submission_test_data):
        """测试获取提交详情"""
        submission_id = submission_test_data['id']
        response = await submission_client.get(f'/api/v1/sys/submission/{submission_id}')
        assert response.status_code == 200
        assert response.json()['code'] == 200
        data = response.json()['data']
        assert data['id'] == submission_id
        assert data['user_id'] == submission_test_data['user_id']
        assert data['exam_id'] == submission_test_data['exam_id']

    async def test_get_submission_not_found(self, submission_client: AsyncClient):
        """测试获取不存在的提交"""
        response = await submission_client.get('/api/v1/sys/submission/99999')
        assert response.status_code == 404

    async def test_get_submissions_pagination(self, submission_client: AsyncClient, submission_test_data):
        """测试获取提交分页列表"""
        response = await submission_client.get('/api/v1/sys/submission?page=1&size=10')
        assert response.status_code == 200
        assert response.json()['code'] == 200
        data = response.json()['data']
        assert 'items' in data
        assert 'total' in data
        assert len(data['items']) >= 1

    async def test_get_submissions_by_user(self, submission_client: AsyncClient, submission_test_data):
        """测试根据用户ID获取提交列表"""
        user_id = submission_test_data['user_id']
        response = await submission_client.get(f'/api/v1/sys/submission/user/{user_id}')
        assert response.status_code == 200
        assert response.json()['code'] == 200
        data = response.json()['data']
        assert isinstance(data, list)
        if data:
            assert all(item['user_id'] == user_id for item in data)

    async def test_get_submissions_by_exam(self, submission_client: AsyncClient, submission_test_data):
        """测试根据考试ID获取提交列表"""
        exam_id = submission_test_data['exam_id']
        response = await submission_client.get(f'/api/v1/sys/submission/exam/{exam_id}')
        assert response.status_code == 200
        assert response.json()['code'] == 200
        data = response.json()['data']
        assert isinstance(data, list)
        if data:
            assert all(item['exam_id'] == exam_id for item in data)

    async def test_get_submission_by_user_exam(self, submission_client: AsyncClient, submission_test_data):
        """测试根据用户ID和考试ID获取提交"""
        user_id = submission_test_data['user_id']
        exam_id = submission_test_data['exam_id']
        response = await submission_client.get(f'/api/v1/sys/submission/user/{user_id}/exam/{exam_id}')
        assert response.status_code == 200
        assert response.json()['code'] == 200
        data = response.json()['data']
        if data:
            assert data['user_id'] == user_id
            assert data['exam_id'] == exam_id

    async def test_update_submission(self, submission_client: AsyncClient, submission_test_data):
        """测试更新提交"""
        submission_id = submission_test_data['id']
        json_data = {
            'status': 'in_progress',
            'total_score': 85.5
        }
        response = await submission_client.put(f'/api/v1/sys/submission/{submission_id}', json=json_data)
        assert response.status_code == 200
        assert response.json()['code'] == 200
        assert response.json()['data'] == 1

        # 验证更新结果
        response = await submission_client.get(f'/api/v1/sys/submission/{submission_id}')
        data = response.json()['data']
        assert data['status'] == 'in_progress'
        assert data['total_score'] == 85.5

    async def test_update_submission_not_found(self, submission_client: AsyncClient):
        """测试更新不存在的提交"""
        json_data = {
            'status': 'submitted'
        }
        response = await submission_client.put('/api/v1/sys/submission/99999', json=json_data)
        assert response.status_code == 404

    async def test_delete_submission(self, submission_client: AsyncClient):
        """测试删除提交"""
        # 先创建一个提交用于删除
        json_data = {
            'user_id': 2,
            'exam_id': 2,
            'status': 'not_started'
        }
        response = await submission_client.post('/api/v1/sys/submission', json=json_data)
        submission_id = response.json()['data']['id']

        # 删除提交
        delete_data = {'pks': [submission_id]}
        response = await submission_client.delete('/api/v1/sys/submission', json=delete_data)
        assert response.status_code == 200
        assert response.json()['code'] == 200
        assert response.json()['data'] == 1

        # 验证删除结果
        response = await submission_client.get(f'/api/v1/sys/submission/{submission_id}')
        assert response.status_code == 404

    async def test_delete_submission_not_found(self, submission_client: AsyncClient):
        """测试删除不存在的提交"""
        delete_data = {'pks': [99999]}
        response = await submission_client.delete('/api/v1/sys/submission', json=delete_data)
        assert response.status_code == 404