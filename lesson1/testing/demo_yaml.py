import yaml

y = """
add:
  datas:
    [1,2,3]
  ids: ["pos_int","pos_bignum","pos_float","zero"]

"""
with open('./datas/calc.yml') as f:
    datas = yaml.safe_load(f)
    print(datas)

