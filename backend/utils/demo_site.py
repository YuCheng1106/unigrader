#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import Request

from common.exception import errors
from core.conf import settings


async def demo_site(request: Request) -> None:
    """
    演示站点

    :param request: FastAPI 请求对象
    :return:
    """
    method = request.method
    path = request.url.path
    if (
        settings.DEMO_MODE
        and method != 'GET'
        and method != 'OPTIONS'
        and (method, path) not in settings.DEMO_MODE_EXCLUDE
    ):
        raise errors.ForbiddenError(msg='演示环境下禁止执行此操作')
