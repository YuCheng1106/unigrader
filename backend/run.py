#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

import uvicorn
# uvicorn main:app --host 0.0.0.0 --port 8000 --reload
if __name__ == '__main__':
    # 为什么独立此启动文件：https://stackoverflow.com/questions/64003384
    # 如果你喜欢在 IDE 中进行 DEBUG，可在 IDE 中直接右键启动此文件
    # 如果你喜欢通过 print 方式进行调试，建议使用 fastapi cli 方式启动服务
    try:
        uvicorn.run(
            app='main:app',
            host='127.0.0.1',
            port=8000,
            reload=True,
        )
    except Exception as e:
        raise e
