#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
from database.db import create_database_url, create_async_engine_and_session
from common.model import MappedBase

# 导入所有模型以确保它们被注册到MappedBase.metadata中
from app.admin.model import *  # noqa: F403, F401
from plugin.exam.model import *  # noqa: F403, F401
from plugin.code_generator.model import *  # noqa: F403, F401
from plugin.dict.model import *  # noqa: F403, F401
from plugin.notice.model import *  # noqa: F403, F401
from plugin.oauth2.model import *  # noqa: F403, F401

async def init_test_database():
    """初始化测试数据库表结构"""
    # 创建测试数据库连接
    test_url = create_database_url(unittest=True)
    test_engine, _ = create_async_engine_and_session(test_url)
    
    # 创建所有表
    async with test_engine.begin() as conn:
        await conn.run_sync(MappedBase.metadata.create_all)
    
    print("测试数据库表结构创建完成")
    await test_engine.dispose()

if __name__ == "__main__":
    asyncio.run(init_test_database())