#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from starlette.testclient import TestClient


def test_create_exam(client: TestClient, token_headers: dict[str, str]) -> None:
    data = {
        'name': '第一次测验',
        'status': 1,
        'remark': 'nihao1',
        'creator_id': 1
    }
    response = client.post('/sys/exams', headers=token_headers, json=data)
    assert response.status_code == 200
    assert response.json()['code'] == 200

def test_update_exam(client: TestClient, token_headers: dict[str, str]) -> None:
    data = {
        'name': '第一次测验',
        'status': 1,
        'remark': 'nihao1',
        'creator_id': 1
    }
    response = client.post('/sys/exams', headers=token_headers, json=data)
    assert response.status_code == 200
    assert response.json()['code'] == 200

