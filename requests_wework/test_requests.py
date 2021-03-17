import random
import re

from filelock import FileLock
import pytest
import requests
import httprunner
@pytest.fixture(scope="session")
def test_token():
    res = None
    while FileLock("seesion.lock"):
        corpid = "ww0025cb2b86c50838"
        corpsecret = "uWkr1zPQBWBKlRC4l9lcp9rmRZyrFCb0gl5Xkj0Aekk"
        res = requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    return (res.json()["access_token"])



def test_get(userid, test_token):
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_token}&userid={userid}")
    return res.json()


def test_create(userid, name, mobile, test_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
        "department": [1],
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_token}",
                        json=data)
    return res.json()


def test_update(userid, name, mobile, test_token):
    data = {
        "userid": userid,
        "name": name,
        "mobile": mobile,
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_token}", json=data)
    return res.json()

def test_delete(userid, test_token):
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_token}&userid={userid}")
    return res.json()

def test_create_date():
    # data = [(str(random.randint(0, 99999)),
    #              "Zhangsan",
    #              str(random.randint(13811110000, 13811119999))
    #              ) for x in range(10)]
    data = [("test1123g" + str(x), f"zhangsan{x}", "138%08d" % x) for x in range(20)]
    print(data)
    return data

@pytest.mark.parametrize("userid, name, mobile", test_create_date())
def test_all(userid, name, mobile, test_token):
    # 可能创建失败
    try:
        assert "created" == test_create(userid, name, mobile, test_token)["errmsg"]
    except AssertionError as e:
        if "mobile exited" in e.__str__():
            # 如果手机号被使用了，找出使用手机号的userid，进行删除
            re_userid = re.findall(":(.*)", e.__str__())[0]
            assert "deleted" == test_delete(re_userid, test_token)["errmsg"]
            assert 60111 == test_get(userid,test_token)["errcode"]
            assert "created" == test_create(userid, name, mobile,test_token)["errmsg"]

    # 可能发生userid不存在异常
    assert name == test_get(userid, test_token)["name"]
    # 可能发生userid不存在异常
    assert "updated" == test_update(userid, "小黑", mobile, test_token)["errmsg"]
    # 可能发生userid不存在异常
    assert "小黑" == test_get(userid, test_token)["name"]

    assert "deleted" == test_delete(userid, test_token)["errmsg"]
    assert 60111 == test_get(userid, test_token)["errcode"]