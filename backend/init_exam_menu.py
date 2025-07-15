#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
from database.db import async_db_session
from sqlalchemy import text

async def init_exam_menu():
    """初始化考试插件菜单和权限"""
    async with async_db_session() as db:
        with open('plugin/exam/sql/mysql/init_exam_menu.sql', 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        # 分割SQL语句
        statements = []
        for line in sql_content.split('\n'):
            line = line.strip()
            if line and not line.startswith('--'):
                statements.append(line)
        
        sql_text = ' '.join(statements)
        sql_statements = [s.strip() for s in sql_text.split(';') if s.strip()]
        
        try:
            for stmt in sql_statements:
                if stmt:
                    await db.execute(text(stmt))
            await db.commit()
            print('考试插件菜单权限初始化完成')
        except Exception as e:
            await db.rollback()
            print(f'初始化失败: {e}')
            raise

if __name__ == '__main__':
    asyncio.run(init_exam_menu())