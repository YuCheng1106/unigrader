#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from core.conf import settings
from plugin.exam.api.v1.sys.exam import router as exam_router
from plugin.exam.api.v1.sys.banji import router as banji_router
from plugin.exam.api.v1.sys.subject import router as subject_router
from plugin.exam.api.v1.sys.exam_question import router as exam_question_router
from plugin.exam.api.v1.sys.submission import router as submission_router
from plugin.exam.api.v1.sys.submission_answer import router as submission_answer_router

v1 = APIRouter(prefix=settings.FASTAPI_API_V1_PATH, tags=['考试管理'])

v1.include_router(exam_router, prefix='/exams', tags=['考试管理'])
v1.include_router(banji_router, prefix='/banjis', tags=['班级管理'])
v1.include_router(subject_router, prefix='/subjects', tags=['学科管理'])
v1.include_router(exam_question_router, prefix='/exam_questions', tags=['考试题目管理'])
v1.include_router(submission_router, prefix='/submissions', tags=['提交管理'])
v1.include_router(submission_answer_router, prefix='/submission_answers', tags=['提交答案管理'])