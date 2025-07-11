#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from app.admin.api.v1.monitor.online import router as token_router
from app.admin.api.v1.monitor.redis import router as redis_router
from app.admin.api.v1.monitor.server import router as server_router

router = APIRouter(prefix='/monitors')

router.include_router(redis_router, prefix='/redis', tags=['redis监控'])
router.include_router(server_router, prefix='/server', tags=['服务器监控'])
router.include_router(token_router, prefix='/sessions', tags=['会话监控'])
