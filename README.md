# ImageServer

파이썬으로 만든

간단한 이미지 서버



## 특징

+ URI Generation
+ File type validation
+ SQLITE3



## 기본 사용법

`GET /`

파일 전송 폼

결과로 key 전송



`POST /`

Multipart 수신부분



`GET /<id>`

id 값에 해당하는 이미지 출력



## 구조

```
├── file.db	(자동생성)
├── README.md
├── index.py
├── util/
|   ├── base62.py
|   └── db.py
├── upload/
|   └── YYYY/
|	   └── mm/
|	      └── dd/
└── templates/
    └── home.html
```

| 파일                 | 설명                            |
| :------------------- | ------------------------------- |
| file.db              | SQLITE3 데이터베이스 (자동생성) |
| Index.py             | flask entry point               |
| util / base62.py     | base62 키 생성                  |
| util / db.py         | SQLITE3 Helper                  |
| upload /             | 파일 저장위치 (자동생성)        |
| templates /home.html | `GET /` 접속시의 홈 템플릿      |



## TODO

+ Image resizing
+ Cache ([groupcache](https://github.com/golang/groupcache), [Redis](https://github.com/garyburd/redigo), [Memcache](https://github.com/bradfitz/gomemcache), in memory)
+ HTTPS Support
+ Crop
+ Convert (JPEG, GIF (animated), PNG , BMP, TIFF, ...)
+ Docker image

