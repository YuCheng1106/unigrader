#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
from database.db import async_db_session
from sqlalchemy import text

async def cleanup():
    async with async_db_session() as db:
        await db.execute(text('DELETE FROM submission_answer WHERE user_id IN (SELECT id FROM sys_user WHERE username = "test_user")'))
        await db.execute(text('DELETE FROM submission WHERE user_id IN (SELECT id FROM sys_user WHERE username = "test_user")'))
        await db.execute(text('DELETE FROM exam_question WHERE exam_id IN (SELECT id FROM sys_exam WHERE name = "测试考试")'))
        await db.execute(text('DELETE FROM sys_exam WHERE name = "测试考试"'))
        await db.execute(text('DELETE FROM sys_user WHERE username = "test_user"'))
        await db.commit()
        print('清理完成')

if __name__ == '__main__':
    asyncio.run(cleanup())