#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Annotated

from fastapi import APIRouter, Depends, Path

from app.task.schema.task import RunParam, TaskResult
from app.task.service.task_service import task_service
from common.response.response_schema import ResponseModel, ResponseSchemaModel, response_base
from common.security.jwt import DependsJwtAuth
from common.security.permission import RequestPermission
from common.security.rbac import DependsRBAC

router = APIRouter()


@router.get(
    '/{tid}',
    summary='获取任务详情',
    deprecated=True,
    description='此接口被视为作废，建议使用 flower 查看任务详情',
    dependencies=[DependsJwtAuth],
)
async def get_task(tid: Annotated[str, Path(description='任务 UUID')]) -> ResponseSchemaModel[TaskResult]:
    status = task_service.get(tid=tid)
    return response_base.success(data=status)


@router.get('', summary='获取所有任务', dependencies=[DependsJwtAuth])
async def get_all_tasks() -> ResponseSchemaModel[list[str]]:
    tasks = await task_service.get_all()
    return response_base.success(data=tasks)


@router.delete(
    '/{tid}',
    summary='撤销任务',
    dependencies=[
        Depends(RequestPermission('sys:task:revoke')),
        DependsRBAC,
    ],
)
async def revoke_task(tid: Annotated[str, Path(description='任务 UUID')]) -> ResponseModel:
    task_service.revoke(tid=tid)
    return response_base.success()


@router.post(
    '/runs',
    summary='运行任务',
    dependencies=[
        Depends(RequestPermission('sys:task:run')),
        DependsRBAC,
    ],
)
async def run_task(obj: RunParam) -> ResponseSchemaModel[str]:
    task = task_service.run(obj=obj)
    return response_base.success(data=task)
