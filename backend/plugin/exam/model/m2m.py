#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import BigInteger, Column, ForeignKey, Table

from common.model import MappedBase

# 用户班级多对多关系表
sys_user_banji = Table(
    'sys_user_banji',
    MappedBase.metadata,
    Column('id', BigInteger, primary_key=True, unique=True, index=True, autoincrement=True, comment='主键ID'),
    Column('user_id', BigInteger, ForeignKey('sys_user.id', ondelete='CASCADE'), primary_key=True, comment='用户ID'),
    Column('banji_id', BigInteger, ForeignKey('sys_banji.id', ondelete='CASCADE'), primary_key=True, comment='班级ID'),
)

# 用户学科多对多关系表
sys_user_subject = Table(
    'sys_user_subject',
    MappedBase.metadata,
    Column('id', BigInteger, primary_key=True, unique=True, index=True, autoincrement=True, comment='主键ID'),
    Column('user_id', BigInteger, ForeignKey('sys_user.id', ondelete='CASCADE'), primary_key=True, comment='用户ID'),
    Column('subject_id', BigInteger, ForeignKey('sys_subject.id', ondelete='CASCADE'), primary_key=True, comment='学科ID'),
)