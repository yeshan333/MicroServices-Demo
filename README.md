# MicroServices-Demo

Usage:

1、pip install -r requirement.txt
2、


```
# api test tool: httpie,Json Object Default:tada:
# https://httpie.org/
# GET
http http://127.0.0.1:5000/api/v1/users/1 -v

# POST
http POST http://127.0.0.1:5000/api/v1/users username="foo" email="1329441308@qq.cw" id=2 password="123kk" full_name="bar"

# DELETE
http delete http://127.0.0.1:5000/api/v1/users username="foo"
```