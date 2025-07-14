#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.exam.tests.utils.exam_question_db import create_exam_question_test_data, delete_exam_question_test_data


class TestExamQuestionAPI:
    """考试题目 API 测试"""

    async def test_create_exam_question(self, exam_client: AsyncClient):
        """测试创建考试题目"""
        response = await exam_client.post(
            '/api/v1/exam_questions',
            json={
                'exam_id': 1,
                'question_type': 'single_choice',
                'question_content': '这是一道单选题',
                'options': {'A': '选项A', 'B': '选项B', 'C': '选项C', 'D': '选项D'},
                'correct_answer': 'A',
                'points': 10.0,
                'sequence': 1
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200

    async def test_get_exam_question(self, exam_client: AsyncClient, exam_db: AsyncSession):
        """测试获取考试题目详情"""
        # 创建测试数据
        question_id = await create_exam_question_test_data(exam_db)
        
        # 测试获取考试题目详情
        response = await exam_client.get(f'/api/v1/exam_questions/{question_id}')
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        assert data['data']['question_content'] == '测试题目内容'
        
        # 清理测试数据
        await delete_exam_question_test_data(exam_db, question_id)

    async def test_get_exam_questions_paged(self, exam_client: AsyncClient, exam_db: AsyncSession):
        """测试分页获取考试题目列表"""
        # 创建测试数据
        question_id = await create_exam_question_test_data(exam_db)
        
        # 测试分页获取考试题目列表
        response = await exam_client.get('/api/v1/exam_questions?page=1&size=10')
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        assert 'records' in data['data']
        
        # 清理测试数据
        await delete_exam_question_test_data(exam_db, question_id)

    async def test_get_exam_questions_by_exam_id(self, exam_client: AsyncClient, exam_db: AsyncSession):
        """测试根据考试ID获取题目列表"""
        # 创建测试数据
        question_id = await create_exam_question_test_data(exam_db)
        
        # 测试根据考试ID获取题目列表
        response = await exam_client.get('/api/v1/exam_questions/by-exam/1')
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        assert isinstance(data['data'], list)
        
        # 清理测试数据
        await delete_exam_question_test_data(exam_db, question_id)

    async def test_update_exam_question(self, exam_client: AsyncClient, exam_db: AsyncSession):
        """测试更新考试题目"""
        # 创建测试数据
        question_id = await create_exam_question_test_data(exam_db)
        
        # 测试更新考试题目
        response = await exam_client.put(
            f'/api/v1/exam_questions/{question_id}',
            json={
                'exam_id': 1,
                'question_type': 'multiple_choice',
                'question_content': '更新后的题目内容',
                'options': {'A': '选项A', 'B': '选项B', 'C': '选项C', 'D': '选项D'},
                'correct_answer': 'A,B',
                'points': 15.0,
                'sequence': 1
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        
        # 清理测试数据
        await delete_exam_question_test_data(exam_db, question_id)

    async def test_delete_exam_questions(self, exam_client: AsyncClient, exam_db: AsyncSession):
        """测试批量删除考试题目"""
        # 创建测试数据
        question_id = await create_exam_question_test_data(exam_db)
        
        # 测试批量删除考试题目
        response = await exam_client.delete(
            '/api/v1/exam_questions',
            json={
                'pks': [question_id]
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200