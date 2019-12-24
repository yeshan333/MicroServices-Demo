# MicroServices-Demo

**Usage:**

1、pip install -r requirements.txt

2、run services，python app.py

3、sqlite3 app.db < app.sql

4、api test

```
# api test tool: httpie,Json Object Default:tada:
# https://httpie.org/
# GET
http http://127.0.0.1:5000/api/v1/users/1 -v

# POST
http POST http://127.0.0.1:5000/api/v1/users username="foo" email="1329441308@qq.cw" id=2 password="123kk" full_name="bar"

# DELETE
http delete http://127.0.0.1:5000/api/v1/users username="foo"

# PUT
http PUT http://127.0.0.1:5000/api/v1/users/1 password="123456"
```