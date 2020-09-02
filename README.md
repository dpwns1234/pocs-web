# pocs-web

한성대학교 동아리 POCS의 웹페이지입니다.

## Prerequisites

이하 소프트웨어가 사전 설치되어있는지 확인합니다.

- Python 3.8
- pip
- virtualenv

## Installation

가상환경이 없는 경우 아래와 같이 생성하면 됩니다.

```text
$ python -m virtualenv venv
$ .\venv\Scripts\activate.bat   (Command Prompt인 경우)
$ .\venv\Scripts\activate.ps1   (PowerShell인 경우)

$ pip install -r requirements.txt
```

## Launch

가상환경에 진입하지 않은 경우, 먼저 아래와 같이 진입해 줍니다.

```text
$ .\venv\Scripts\activate.bat   (Command Prompt인 경우)
$ .\venv\Scripts\activate.ps1   (PowerShell인 경우)
```

이후 `manage.py`가 있는 디렉터리로 이동해 서버를 실행합니다.

```text
$ cd web  (필요한 경우)

$ python manage.py runserver
```

기본적으로 `8000`번 포트를 사용하나, 아래와 같이 변경할 수 있습니다.

```text
$ python manage.py runserver 8080
```

# 추가한 것
카페 메인 html, 글쓰기 기능

# 진행중인 것
게시물 리스트, 글쓰기 기능
