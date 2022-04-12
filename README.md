# kivy_appliciation
kivy를 활용한 python기반의 app 개발

## 가상환경 설정
[공식문서](https://kivy.org/doc/stable/gettingstarted/installation.html)에 따르면 kivy는 가상환경을 생성하는 것이 거의 필수적(strongly recommended)이기 때문에,  
가상환경을 설정해 준 뒤 해당 환경에서 개발을 진행한다.


#### 0. Setup terminal and pip
```
python -m pip install --upgrade pip setuptools virtualenv
```

#### 1. Create the virtual environment named `kivy_venv` in your current directory
```
python -m virtualenv kivy_venv
```

#### 2. Activate the `kivy_venv`
- WINDOWS
```
kivy_venv\Scripts\activate
```
- linux, MacOS
```
source kivy_venv/bin/activate
```
