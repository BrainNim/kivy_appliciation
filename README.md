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

#### 3. pip install
```
python -m pip install "kivy[base]" kivy_examples
```
위의 pip install에서 에러가 나타날 경우 ([참조1](https://kivy.org/doc/stable/gettingstarted/installation.html), [참조2](https://stackoverflow.com/questions/59125232/how-to-deal-with-kivy-installing-error-in-python-3-8))
```
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2==0.1.* kivy_deps.glew==0.1.*
python -m pip install kivy_deps.gstreamer==0.1.*
python -m pip install kivy_deps.angle==0.1.*
python -m pip install "kivy[base] @ https://github.com/kivy/kivy/archive/master.zip"
```

#### 4. Optional(example demo)
```
python -m pip install kivy_examples==1.11.1
```
아래의 코드를 실행하면 데모프로그램(kivy로 제작할 수 있는 UI의 예)을 실행가능
```
python kivy_venv\share\kivy-examples\demo\showcase\main.py
```
