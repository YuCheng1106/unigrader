#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.admin.model import User
from plugin.exam.model import Exam, ExamQuestion, Submission, SubmissionAnswer
from plugin.exam.schema.submission_answer import CreateSubmissionAnswerParam, UpdateSubmissionAnswerParam
from .utils.submission_answer_db import create_submission_answer_test_data, delete_submission_answer_test_data


class TestSubmissionAnswerApi:
    """提交答案API测试"""

    async def test_create_submission_answer(self, submission_answer_client: AsyncClient):
        """测试创建提交答案"""
        json_data = {
            'user_id': 1,
            'exam_id': 1,
            'submission_id': 1,
            'exam_question_id': 1,
            'answer_content': '这是我的答案',
            'submitted_at': '2024-01-01T10:00:00'
        }
        response = await submission_answer_client.post('/api/v1/submission_answers', json=json_data)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['code'] == 200

    async def test_get_submission_answer_detail(self, submission_answer_client: AsyncClient):
        """测试获取提交答案详情"""
        response = await submission_answer_client.get('/api/v1/submission_answers/1')
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['code'] == 200
        assert response_data['data']['id'] == 1

    async def test_get_submission_answers_by_submission_id(self, submission_answer_client: AsyncClient):
        """测试通过提交ID获取所有答案"""
        response = await submission_answer_client.get('/api/v1/submission_answers/submission/1')
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['code'] == 200
        assert isinstance(response_data['data'], list)

    async def test_get_submission_answers_by_user_id(self, submission_answer_client: AsyncClient):
        """测试通过用户ID获取所有答案"""
        response = await submission_answer_client.get('/api/v1/submission_answers/user/1')
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['code'] == 200
        assert isinstance(response_data['data'], list)

    async def test_get_submission_answers_by_exam_id(self, submission_answer_client: AsyncClient):
        """测试通过考试ID获取所有答案"""
        response = await submission_answer_client.get('/api/v1/submission_answers/exam/1')
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['code'] == 200
        assert isinstance(response_data['data'], list)

    async def test_get_submission_answer_by_user_and_question(self, submission_answer_client: AsyncClient):
        """测试通过用户ID和题目ID获取答案"""
        response = await submission_answer_client.get('/api/v1/submission_answers/user/1/question/1')
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['code'] == 200

    async def test_get_submission_answers_by_grader(self, submission_answer_client: AsyncClient):
        """测试通过批改者ID获取所有批改的答案"""
        response = await submission_answer_client.get('/api/v1/submission_answers/grader/1')
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['code'] == 200
        assert isinstance(response_data['data'], list)

    async def test_update_submission_answer(self, submission_answer_client: AsyncClient):
        """测试更新提交答案"""
        json_data = {
            'answer_content': '更新后的答案',
            'is_correct': True,
            'score': 85.5,
            'feedback': '答案正确，表述清晰'
        }
        response = await submission_answer_client.put('/api/v1/submission_answers/1', json=json_data)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['code'] == 200

    async def test_delete_submission_answer(self, submission_answer_client: AsyncClient):
        """测试删除提交答案"""
        response = await submission_answer_client.delete('/api/v1/submission_answers/1')
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['code'] == 200

    async def test_delete_submission_answers_batch(self, submission_answer_client: AsyncClient):
        """测试批量删除提交答案"""
        json_data = {'pks': [2, 3]}
        response = await submission_answer_client.request('DELETE', '/api/v1/submission_answers', json=json_data)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['code'] == 200

    async def test_get_submission_answer_not_found(self, submission_answer_client: AsyncClient):
        """测试获取不存在的提交答案"""
        response = await submission_answer_client.get('/api/v1/submission_answers/999')
        assert response.status_code == 404
        response_data = response.json()
        assert response_data['code'] == 404
        assert '提交答案不存在' in response_data['msg']

    async def test_update_submission_answer_not_found(self, submission_answer_client: AsyncClient):
        """测试更新不存在的提交答案"""
        json_data = {'answer_content': '更新答案'}
        response = await submission_answer_client.put('/api/v1/submission_answers/999', json=json_data)
        assert response.status_code == 404
        response_data = response.json()
        assert response_data['code'] == 404
        assert '提交答案不存在' in response_data['msg']

    async def test_delete_submission_answer_not_found(self, submission_answer_client: AsyncClient):
        """测试删除不存在的提交答案"""
        response = await submission_answer_client.delete('/api/v1/submission_answers/999')
        assert response.status_code == 404
        response_data = response.json()
        assert response_data['code'] == 404
        assert '提交答案不存在' in response_data['msg']