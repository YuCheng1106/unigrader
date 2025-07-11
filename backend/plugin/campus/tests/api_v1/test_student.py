#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from starlette.testclient import TestClient


def test_create_student(client: TestClient, token_headers: dict[str, str]) -> None:
    data = {
        'school_id': 1,
        'username': 'chengyu',
        'password': 'cy123456',
    }
    response = client.post('/sys/students', headers=token_headers, json=data)
    assert response.status_code == 200
    assert response.json()['code'] == 200


def test_create_student_with_number(client: TestClient, token_headers: dict[str, str]) -> None:
    data = {
        'username': 'chengyu1',
        'password': 'cy123456',
        'nickname': 'chengyu',
        'school_id': 1,
        'student_number': '202126202182'
    }
    response = client.post('/sys/students', headers=token_headers, json=data)
    assert response.status_code == 200
    assert response.json()['code'] == 200
    response = client.post('/sys/students', headers=token_headers, json=data)
    print(response.json())