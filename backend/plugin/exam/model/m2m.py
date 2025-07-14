#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import BigInteger, Column, ForeignKey, Table, DateTime
from datetime import datetime

from common.model import MappedBase
from utils.timezone import timezone

# 用户考试关系表（用户参与的考试）
exam_user = Table(
    'exam_user',
    MappedBase.metadata,
    Column('id', BigInteger, primary_key=True, unique=True, index=True, autoincrement=True, comment='主键ID'),
    Column('user_id', BigInteger, ForeignKey('sys_user.id', ondelete='CASCADE'), primary_key=True, comment='用户ID'),
    Column('exam_id', BigInteger, ForeignKey('sys_exam.id', ondelete='CASCADE'), primary_key=True, comment='考试ID'),

)

# 考试班级关系表（考试对应的班级）
exam_banji = Table(
    'exam_banji',
    MappedBase.metadata,
    Column('id', BigInteger, primary_key=True, unique=True, index=True, autoincrement=True, comment='主键ID'),
    Column('exam_id', BigInteger, ForeignKey('sys_exam.id', ondelete='CASCADE'), primary_key=True, comment='考试ID'),
    Column('banji_id', BigInteger, ForeignKey('sys_banji.id', ondelete='CASCADE'), primary_key=True, comment='班级ID'),
)



# 用户班级关系表（用户所属的班级）
user_banji = Table(
    'user_banji',
    MappedBase.metadata,
    Column('id', BigInteger, primary_key=True, unique=True, index=True, autoincrement=True, comment='主键ID'),
    Column('user_id', BigInteger, ForeignKey('sys_user.id', ondelete='CASCADE'), primary_key=True, comment='用户ID'),
    Column('banji_id', BigInteger, ForeignKey('sys_banji.id', ondelete='CASCADE'), primary_key=True, comment='班级ID'),

)

# 教师学科关系表（教师教授的学科）
teacher_subject = Table(
    'teacher_subject',
    MappedBase.metadata,
    Column('id', BigInteger, primary_key=True, unique=True, index=True, autoincrement=True, comment='主键ID'),
    Column('teacher_id', BigInteger, ForeignKey('sys_user.id', ondelete='CASCADE'), primary_key=True, comment='教师ID'),
    Column('subject_id', BigInteger, ForeignKey('sys_subject.id', ondelete='CASCADE'), primary_key=True, comment='学科ID'),

)

# 教师班级关系表（教师负责的班级）
teacher_banji = Table(
    'teacher_banji',
    MappedBase.metadata,
    Column('id', BigInteger, primary_key=True, unique=True, index=True, autoincrement=True, comment='主键ID'),
    Column('teacher_id', BigInteger, ForeignKey('sys_user.id', ondelete='CASCADE'), primary_key=True, comment='教师ID'),
    Column('banji_id', BigInteger, ForeignKey('sys_banji.id', ondelete='CASCADE'), primary_key=True, comment='班级ID'),

)