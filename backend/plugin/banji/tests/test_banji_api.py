#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from plugin.banji.tests.utils.db import create_banji_test_data, delete_banji_test_data


class TestBanjiAPI:
    """班级 API 测试"""

    async def test_create_banji(self, banji_client: AsyncClient):
        """测试创建班级"""
        response = await banji_client.post(
            '/api/v1/banjis',
            json={
                'name': '新建班级',
                'remark': '这是一个新建的班级'
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200

    async def test_get_banji(self, banji_client: AsyncClient, banji_db: AsyncSession):
        """测试获取班级详情"""
        # 创建测试数据
        banji_id = await create_banji_test_data(banji_db)
        
        # 测试获取班级详情
        response = await banji_client.get(f'/api/v1/banjis/{banji_id}')
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        assert data['data']['name'] == '测试班级'
        
        # 清理测试数据
        await delete_banji_test_data(banji_db, banji_id)

    async def test_get_banjis_paged(self, banji_client: AsyncClient, banji_db: AsyncSession):
        """测试分页获取班级列表"""
        # 创建测试数据
        banji_id = await create_banji_test_data(banji_db)
        
        # 测试分页获取班级列表
        response = await banji_client.get('/api/v1/banjis?page=1&size=10')
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        assert 'records' in data['data']
        
        # 清理测试数据
        await delete_banji_test_data(banji_db, banji_id)

    async def test_update_banji(self, banji_client: AsyncClient, banji_db: AsyncSession):
        """测试更新班级"""
        # 创建测试数据
        banji_id = await create_banji_test_data(banji_db)
        
        # 测试更新班级
        response = await banji_client.put(
            f'/api/v1/banjis/{banji_id}',
            json={
                'name': '更新后的班级',
                'remark': '这是更新后的班级备注'
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200
        
        # 清理测试数据
        await delete_banji_test_data(banji_db, banji_id)

    async def test_delete_banjis(self, banji_client: AsyncClient, banji_db: AsyncSession):
        """测试批量删除班级"""
        # 创建测试数据
        banji_id = await create_banji_test_data(banji_db)
        
        # 测试批量删除班级
        response = await banji_client.delete(
            '/api/v1/banjis',
            json={
                'ids': [banji_id]
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data['code'] == 200