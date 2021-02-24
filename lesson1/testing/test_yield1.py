


def test_search():
    print("搜索")

def test_cart(login):
    print(login)
    print("购物")

# @pytest.mark.usefixture("login")
def test_order(login):
    print(login)
    print("下单")