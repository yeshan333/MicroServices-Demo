# MicroServices-Demo

**Usage:**

```bash
1、pip install -r requirements.txt

2、run services，python app.py

3、.\mongod.exe --config .\mongod.conf # shift+mouse right powershell, mount mongo server

4、api unittest, pip install nose

5、nosetests  # unittest
```

```bash
# api test tool: httpie,Json Object Default
# https://httpie.org/
# GET
http http://127.0.0.1:5000/api/v1/users/1 -v

# POST
http POST http://127.0.0.1:5000/api/v1/users username="foo" email="1329441308@qq.cw" password="123kk" full_name="bar"

# DELETE
http delete http://127.0.0.1:5000/api/v1/users username="foo"

# PUT
http PUT http://127.0.0.1:5000/api/v1/users/1 password="123456"

# v2 api
http http://127.0.0.1:5000/api/v1/info -v

http http://127.0.0.1:5000/api/v2/tweets -v

http POST http://127.0.0.1:5000/api/v2/tweets username="yeshan333" body="Hello 2020!" -v

http http://127.0.0.1:5000/api/v2/tweets/2 -v
```