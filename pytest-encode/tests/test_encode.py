#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

@pytest.fixture(params=["harry", "hemin"])
def login(request):
    print("login")
    return request.param


def test_search(login):
    print(login)
    print("搜索")

@pytest.mark.parametrize('name', ['哈利', '赫敏'])
def test_encode(name):
    print(name)


@pytest.mark.parametrize('name', ['利1', '敏1'])
def test_fixture1(name):
    print("fixture1")
