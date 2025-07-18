#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Any

from pydantic import Field

from common.schema import SchemaBase


class RunParam(SchemaBase):
    """任务运行参数"""

    name: str = Field(description='任务名称')
    args: list[Any] | None = Field(None, description='任务函数位置参数')
    kwargs: dict[str, Any] | None = Field(None, description='任务函数关键字参数')


class TaskResult(SchemaBase):
    """任务执行结果"""

    result: str = Field(description='任务执行结果')
    traceback: str | None = Field(None, description='错误堆栈信息')
    status: str = Field(description='任务状态')
    name: str | None = Field(None, description='任务名称')
    args: list[Any] | None = Field(None, description='任务函数位置参数')
    kwargs: dict[str, Any] | None = Field(None, description='任务函数关键字参数')
    worker: str | None = Field(None, description='执行任务的 worker')
    retries: int | None = Field(None, description='重试次数')
    queue: str | None = Field(None, description='任务队列')
