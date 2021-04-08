import json

jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

text = json.loads(jsonData)
print(f"https://api.weixin.qq.com/sns/jscode2session"
        f"?appid=&secret=&js_code=&grant_type=authorization_code")