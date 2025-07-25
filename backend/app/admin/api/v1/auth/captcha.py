#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fast_captcha import img_captcha
from fastapi import APIRouter, Depends, Request
from fastapi_limiter.depends import RateLimiter
from starlette.concurrency import run_in_threadpool

from app.admin.schema.captcha import GetCaptchaDetail
from common.response.response_schema import ResponseSchemaModel, response_base
from core.conf import settings
from database.redis import redis_client

router = APIRouter()


@router.get(
    '/captcha',
    summary='获取登录验证码',
    dependencies=[Depends(RateLimiter(times=5, seconds=10))],
)
async def get_captcha(request: Request) -> ResponseSchemaModel[GetCaptchaDetail]:
    """
    此接口可能存在性能损耗，尽管是异步接口，但是验证码生成是IO密集型任务，使用线程池尽量减少性能损耗
    """
    img_type: str = 'base64'
    img, code = await run_in_threadpool(img_captcha, img_byte=img_type)
    ip = request.state.ip
    await redis_client.set(
        f'{settings.CAPTCHA_LOGIN_REDIS_PREFIX}:{ip}',
        code,
        ex=settings.CAPTCHA_LOGIN_EXPIRE_SECONDS,
    )
    data = GetCaptchaDetail(image_type=img_type, image=img)
    return response_base.success(data=data)
