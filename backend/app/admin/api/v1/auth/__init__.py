#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from app.admin.api.v1.auth.auth import router as auth_router
from app.admin.api.v1.auth.captcha import router as captcha_router

router = APIRouter(prefix='/auth')

router.include_router(auth_router, tags=['授权'])
router.include_router(captcha_router, tags=['验证码'])
