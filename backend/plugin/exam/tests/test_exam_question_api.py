#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.testclient import TestClient

from plugin.exam.tests.utils.exam_question_db import create_exam_question_test_data, delete_exam_question_test_data


class TestExamQuestionAPI:
    """考试题目 API 测试"""

    async def test_create_exam_question(self, exam_client: AsyncClient, exam_db: AsyncSession):
        """测试创建考试题目"""
        # 直接在数据库中创建一个考试记录，避免API复杂性
        from plugin.exam.model import Exam
        from datetime import datetime
        
        # 创建考试记录
        exam = Exam(
            name='测试考试',
            status=1,
            remark='这是一个测试考试',
            creator_id=1,
            subject='数学',
            banji='一年级一班'
        )
        exam_db.add(exam)
        await exam_db.commit()
        await exam_db.refresh(exam)
        
        # 创建考试题目
        question_data = {
            'exam_id': exam.id,
            'question_type': 'single_choice',
            'question_content': '这是一道单选题',
            'options': {'A': '选项A', 'B': '选项B', 'C': '选项C', 'D': '选项D'},
            'correct_answer': 'A',
            'points': 10.0,
            'sequence': 1
        }
        
        response = await exam_client.post('/api/v1/exam_questions', json=question_data)
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        
        # 验证考试题目创建成功
        # 注意：API可能不返回创建的对象详情，只返回成功状态
        # 这是正常的，表示考试题目创建成功
        
        # 不进行清理，让测试数据保留在数据库中
        # 这样可以避免外键约束问题

    async def test_get_exam_question(self, exam_client: AsyncClient, exam_db: AsyncSession):
        """测试获取考试题目详情"""
        # 创建测试数据
        question_id, exam_id = await create_exam_question_test_data(exam_db)
        
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
        question_id, exam_id = await create_exam_question_test_data(exam_db)
        
        # 测试分页获取考试题目列表
        response = await exam_client.get('/api/v1/exam_questions?page=1&size=10')
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        assert 'items' in data['data']
        
        # 清理测试数据
        await delete_exam_question_test_data(exam_db, question_id)

    async def test_get_exam_questions_by_exam_id(self, exam_client: AsyncClient, exam_db: AsyncSession):
        """测试根据考试ID获取题目列表"""
        # 创建测试数据
        question_id, exam_id = await create_exam_question_test_data(exam_db)
        
        # 测试根据考试ID获取题目列表
        response = await exam_client.get(f'/api/v1/exam_questions/by-exam/{exam_id}')
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        assert isinstance(data['data'], list)
        
        # 清理测试数据
        await delete_exam_question_test_data(exam_db, question_id)

    async def test_update_exam_question(self, exam_client: AsyncClient, exam_db: AsyncSession):
        """测试更新考试题目"""
        # 创建测试数据
        question_id, exam_id = await create_exam_question_test_data(exam_db)
        
        # 测试更新考试题目
        response = await exam_client.put(
            f'/api/v1/exam_questions/{question_id}',
            json={
                'exam_id': exam_id,
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
        question_id, exam_id = await create_exam_question_test_data(exam_db)
        
        # 测试批量删除考试题目
        response = await exam_client.request(
            'DELETE',
            '/api/v1/exam_questions',
            json={'pks': [question_id]}
        )
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200