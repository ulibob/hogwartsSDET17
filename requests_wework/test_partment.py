import requests


def test_token():
    # 获取token
    res = None
    corpid = "ww0025cb2b86c50838"
    corpsecret = "uWkr1zPQBWBKlRC4l9lcp9rmRZyrFCb0gl5Xkj0Aekk"
    res = requests.get(url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&"
                           f"corpsecret={corpsecret}")
    print(res.json()["access_token"])
    return (res.json()["access_token"])


def test_create():
    #创建部门成员
    data = {
        "name": "广州研发中心",
        "parentid": 1,

    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={test_token()}", json=data)
    print(res.json())


def test_update():
    # 更新成员
    data = {
        "id": 3,
        "name": "广州研发中心654321",
        "parentid": 1,
    }
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={test_token()}", json=data)
    print(res.json())


def test_delete():
    # 删除成员
    partmentid = 3
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={test_token()}&id={partmentid}")
    print(res.json())

