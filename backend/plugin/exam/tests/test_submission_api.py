#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.exam.schema.submission import CreateSubmissionParam, UpdateSubmissionParam
from plugin.exam.tests.utils.submission_db import create_submission_test_data, delete_submission_test_data


class TestSubmissionAPI:
    """提交API测试"""

    async def test_create_submission(self, submission_client: AsyncClient, submission_db: AsyncSession):
        """测试创建提交"""
        # 先创建必要的测试数据
        from app.admin.model import User
        from plugin.exam.model import Exam
        import uuid
        
        # 生成唯一的用户名
        unique_suffix = str(uuid.uuid4())[:6]
        username = f'test_user_{unique_suffix}'
        email = f'test_{unique_suffix}@example.com'
        
        # 创建测试用户
        user = User(
            username=username,
            nickname='测试创建用户',
            password='test_password',
            salt=b'test_salt',
            email=email,
            phone='13800138001',
            avatar='',
            is_superuser=False,
            is_staff=False,
            status=1
        )
        submission_db.add(user)
        await submission_db.flush()
        await submission_db.refresh(user)
        
        # 创建测试考试
        exam = Exam(
            name='测试创建考试',
            status=1,
            remark='这是一个测试创建考试',
            creator_id=user.id,
            subject='数学',
            banji='一年级一班'
        )
        submission_db.add(exam)
        await submission_db.flush()
        await submission_db.refresh(exam)
        await submission_db.commit()
        
        json_data = {
            'user_id': user.id,
            'exam_id': exam.id,
            'status': 'not_started'
        }
        response = await submission_client.post('/api/v1/submissions', json=json_data)
        assert response.status_code == 200
        assert response.json()['code'] == 200
        data = response.json()['data']
        assert data['user_id'] == user.id
        assert data['exam_id'] == exam.id
        assert data['status'] == 'not_started'
        
        # 清理测试数据
        from sqlalchemy import text
        await submission_db.execute(text('DELETE FROM submission WHERE user_id = :user_id'), {'user_id': user.id})
        await submission_db.execute(text('DELETE FROM sys_exam WHERE id = :exam_id'), {'exam_id': exam.id})
        await submission_db.execute(text('DELETE FROM sys_user WHERE id = :user_id'), {'user_id': user.id})
        await submission_db.commit()

    async def test_get_submission(self, submission_client: AsyncClient, submission_db: AsyncSession):
        """测试获取提交详情"""
        # 先创建必要的测试数据
        from app.admin.model import User
        from plugin.exam.model import Exam
        import uuid
        
        # 生成唯一的用户名
        unique_suffix = str(uuid.uuid4())[:6]
        username = f'test_user_{unique_suffix}'
        email = f'test_{unique_suffix}@example.com'
        
        # 创建测试用户
        user = User(
            username=username,
            nickname='测试获取用户',
            password='test_password',
            salt=b'test_salt',
            email=email,
            phone='13800138002',
            avatar='',
            is_superuser=False,
            is_staff=False,
            status=1
        )
        submission_db.add(user)
        await submission_db.flush()
        await submission_db.refresh(user)
        
        # 创建测试考试
        exam = Exam(
            name=f'测试获取考试_{unique_suffix}',
            status=1,
            remark='这是一个测试获取考试',
            creator_id=user.id,
            subject='数学',
            banji='一年级一班'
        )
        submission_db.add(exam)
        await submission_db.flush()
        await submission_db.refresh(exam)
        
        # 创建提交
        json_data = {
            'user_id': user.id,
            'exam_id': exam.id,
            'status': 'not_started'
        }
        response = await submission_client.post('/api/v1/submissions', json=json_data)
        assert response.status_code == 200
        submission_id = response.json()['data']['id']
        
        # 测试获取提交详情
        response = await submission_client.get(f'/api/v1/submissions/{submission_id}')
        assert response.status_code == 200
        assert response.json()['code'] == 200
        data = response.json()['data']
        assert data['id'] == submission_id
        assert data['user_id'] == user.id
        assert data['exam_id'] == exam.id
        
        # 清理测试数据
        from sqlalchemy import text
        await submission_db.execute(text('DELETE FROM submission WHERE id = :submission_id'), {'submission_id': submission_id})
        await submission_db.execute(text('DELETE FROM sys_exam WHERE id = :exam_id'), {'exam_id': exam.id})
        await submission_db.execute(text('DELETE FROM sys_user WHERE id = :user_id'), {'user_id': user.id})
        await submission_db.commit()

    async def test_get_submission_not_found(self, submission_client: AsyncClient):
        """测试获取不存在的提交"""
        response = await submission_client.get('/api/v1/submissions/99999')
        assert response.status_code == 404

    async def test_get_submissions_pagination(self, submission_client: AsyncClient):
        """测试获取提交分页列表"""
        response = await submission_client.get('/api/v1/submissions?page=1&size=10')
        assert response.status_code == 200
        assert response.json()['code'] == 200
        data = response.json()['data']
        assert 'items' in data
        assert 'total' in data
        # 不要求必须有数据，因为可能数据库是空的
        assert isinstance(data['items'], list)
        assert isinstance(data['total'], int)

    async def test_get_submissions_by_user(self, submission_client: AsyncClient):
        """测试根据用户ID获取提交列表"""
        # 使用一个不存在的用户ID进行测试
        user_id = 99999
        response = await submission_client.get(f'/api/v1/submissions/user/{user_id}')
        assert response.status_code == 200
        assert response.json()['code'] == 200
        data = response.json()['data']
        assert isinstance(data, list)
        # 对于不存在的用户，应该返回空列表
        assert len(data) == 0

    async def test_get_submissions_by_exam(self, submission_client: AsyncClient):
        """测试根据考试ID获取提交列表"""
        # 使用一个不存在的考试ID进行测试
        exam_id = 99999
        response = await submission_client.get(f'/api/v1/submissions/exam/{exam_id}')
        assert response.status_code == 200
        assert response.json()['code'] == 200
        data = response.json()['data']
        assert isinstance(data, list)
        # 对于不存在的考试，应该返回空列表
        assert len(data) == 0

    async def test_get_submission_by_user_exam(self, submission_client: AsyncClient):
        """测试根据用户ID和考试ID获取提交"""
        # 使用不存在的用户ID和考试ID进行测试
        user_id = 99999
        exam_id = 99999
        response = await submission_client.get(f'/api/v1/submissions/user/{user_id}/exam/{exam_id}')
        assert response.status_code == 200
        assert response.json()['code'] == 200
        data = response.json()['data']
        # 对于不存在的用户和考试组合，应该返回 None 或空数据
        assert data is None or data == {}

    async def test_update_submission(self, submission_client: AsyncClient, submission_db: AsyncSession):
        """测试更新提交"""
        # 先创建必要的测试数据
        from app.admin.model import User
        from plugin.exam.model import Exam
        import uuid
        
        # 生成唯一的用户名
        unique_suffix = str(uuid.uuid4())[:6]
        username = f'test_user_{unique_suffix}'
        email = f'test_{unique_suffix}@example.com'
        
        # 创建测试用户
        user = User(
            username=username,
            nickname='测试更新用户',
            password='test_password',
            salt=b'test_salt',
            email=email,
            phone='13800138003',
            avatar='',
            is_superuser=False,
            is_staff=False,
            status=1
        )
        submission_db.add(user)
        await submission_db.flush()
        await submission_db.refresh(user)
        
        # 创建测试考试
        exam = Exam(
            name=f'测试更新考试_{unique_suffix}',
            status=1,
            remark='这是一个测试更新考试',
            creator_id=user.id,
            subject='数学',
            banji='一年级一班'
        )
        submission_db.add(exam)
        await submission_db.flush()
        await submission_db.refresh(exam)
        
        # 创建提交
        json_data = {
            'user_id': user.id,
            'exam_id': exam.id,
            'status': 'not_started'
        }
        response = await submission_client.post('/api/v1/submissions', json=json_data)
        assert response.status_code == 200
        submission_id = response.json()['data']['id']
        
        # 测试更新提交
        update_data = {
            'status': 'in_progress',
            'total_score': 85.5
        }
        response = await submission_client.put(f'/api/v1/submissions/{submission_id}', json=update_data)
        assert response.status_code == 200
        assert response.json()['code'] == 200
        assert response.json()['data'] == 1

        # 验证更新结果
        response = await submission_client.get(f'/api/v1/submissions/{submission_id}')
        data = response.json()['data']
        assert data['status'] == 'in_progress'
        assert data['total_score'] == 85.5
        
        # 清理测试数据
        from sqlalchemy import text
        await submission_db.execute(text('DELETE FROM submission WHERE id = :submission_id'), {'submission_id': submission_id})
        await submission_db.execute(text('DELETE FROM sys_exam WHERE id = :exam_id'), {'exam_id': exam.id})
        await submission_db.execute(text('DELETE FROM sys_user WHERE id = :user_id'), {'user_id': user.id})
        await submission_db.commit()

    async def test_update_submission_not_found(self, submission_client: AsyncClient):
        """测试更新不存在的提交"""
        json_data = {
            'status': 'submitted'
        }
        response = await submission_client.put('/api/v1/submissions/99999', json=json_data)
        assert response.status_code == 404

    async def test_delete_submission(self, submission_client: AsyncClient, submission_db: AsyncSession):
        """测试删除提交"""
        # 先创建必要的测试数据
        from app.admin.model import User
        from plugin.exam.model import Exam
        import uuid
        
        # 生成唯一的用户名
        unique_suffix = str(uuid.uuid4())[:6]
        username = f'test_user_{unique_suffix}'
        email = f'test_{unique_suffix}@example.com'
        
        # 创建测试用户
        user = User(
            username=username,
            nickname='测试删除用户',
            password='test_password',
            salt=b'test_salt',
            email=email,
            phone='13800138004',
            avatar='',
            is_superuser=False,
            is_staff=False,
            status=1
        )
        submission_db.add(user)
        await submission_db.flush()
        await submission_db.refresh(user)
        
        # 创建测试考试
        exam = Exam(
            name=f'测试删除考试_{unique_suffix}',
            status=1,
            remark='这是一个测试删除考试',
            creator_id=user.id,
            subject='数学',
            banji='一年级一班'
        )
        submission_db.add(exam)
        await submission_db.flush()
        await submission_db.refresh(exam)
        await submission_db.commit()
        
        # 创建提交
        json_data = {
            'user_id': user.id,
            'exam_id': exam.id,
            'status': 'not_started'
        }
        response = await submission_client.post('/api/v1/submissions', json=json_data)
        assert response.status_code == 200
        submission_id = response.json()['data']['id']

        # 删除提交
        delete_data = {'pks': [submission_id]}
        response = await submission_client.request('DELETE', '/api/v1/submissions', json=delete_data)
        assert response.status_code == 200
        assert response.json()['code'] == 200
        assert response.json()['data'] == 1

        # 验证删除结果
        response = await submission_client.get(f'/api/v1/submissions/{submission_id}')
        assert response.status_code == 404
        
        # 清理测试数据
        from sqlalchemy import text
        await submission_db.execute(text('DELETE FROM sys_exam WHERE id = :exam_id'), {'exam_id': exam.id})
        await submission_db.execute(text('DELETE FROM sys_user WHERE id = :user_id'), {'user_id': user.id})
        await submission_db.commit()

    async def test_delete_submission_not_found(self, submission_client: AsyncClient):
        """测试删除不存在的提交"""
        delete_data = {'pks': [99999]}
        response = await submission_client.request('DELETE', '/api/v1/submissions', json=delete_data)
        assert response.status_code == 404