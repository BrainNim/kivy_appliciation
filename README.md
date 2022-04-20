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
아래의 코드를 실행하면 데모프로그램(kivy로 제작할 수 있는 UI의 예)을 실행가능, 정상실행시 가상환경, kivy설치 완료
```
python kivy_venv\share\kivy-examples\demo\showcase\main.py
```


## Kivy Basics
https://kivy.org/doc/stable/guide/basic.html

### Basics: Hello World
```
import kivy
# kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    MyApp().run()
```

### Login Screen
```
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        
        # (1,1)
        self.add_widget(Label(text='User Name'))
        # (1,2)
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        
        # (2,1)
        self.add_widget(Label(text='password'))
        # (2,2)
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
```

- `GridLayout`: 위젯 UI를 그리드(격자)형태로 나타낼 수 있게해주는 클래스
- `add_widget`을 통해 왼쪽부터 차례로 위젯을 추가하는 형태


## 안드로이드 패키지 배포
[공식문서](https://kivy.org/doc/stable/guide/packaging-android.html)

#### WSL 설정
```
sudo apt install python3-pip
sudp apt install unzip
sudo apt install zlib1g-dev  # zlib1g로는 안되더라. 새로 설치해야함
sudo apt install cython
sudo apt -y install openjdk-8-jdk
```

아래와 같은 에러 발생
```
sdkmanager path "/home/olixao/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager" does not exist, sdkmanager is notinstalled
```

해결
```
cd ~/.buildozer/android/platform/android-sdk
curl -L -O -C - https://dl.google.com/android/repository/sdk-tools-linux-4333796.zip
unzip sdk-tools-linux-4333796.zip
```
[에러슈팅 참고링크](https://github.com/kivy/buildozer/issues/927)


그런데 이번엔 또 다른 에러 발생
```
# Search for Git (git)
#  -> found at /usr/bin/git
# Search for Cython (cython)
#  -> found at /usr/bin/cython
# Search for Java compiler (javac)
#  -> found at /usr/lib/jvm/java-11-openjdk-amd64/bin/javac
# Search for Java keytool (keytool)
#  -> found at /usr/lib/jvm/java-11-openjdk-amd64/bin/keytool
# Install platform
# Run 'git config --get remote.origin.url'
# Cwd /mnt/c/Users/user/Documents/Python Scripts/kivy_appliciation/.buildozer/android/platform/python-for-android
https://github.com/kivy/python-for-android.git
# Run 'git branch -vv'
# Cwd /mnt/c/Users/user/Documents/Python Scripts/kivy_appliciation/.buildozer/android/platform/python-for-android
* master 227a7658 [origin/master] Merge pull request #2561 from misl6/release-2022.03.13
# Run '/usr/bin/python3 -m pip install -q --user \'appdirs\' \'colorama>=0.3.3\' \'jinja2\' \'six\' \'enum34; python_version<"3.4"\' \'sh>=1.10; sys_platform!="nt"\' \'pep517<0.7.0\' \'to
ml\''
# Cwd None
# Apache ANT found at /home/lee_ubuntu/.buildozer/android/platform/apache-ant-1.9.4
# Android SDK found at /home/lee_ubuntu/.buildozer/android/platform/android-sdk
# Recommended android's NDK version by p4a is: 19c
# Android NDK found at /home/lee_ubuntu/.buildozer/android/platform/android-ndk-r19c
# Installing/updating SDK platform tools if necessary
# Run '/home/lee_ubuntu/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager --sdk_root=/home/lee_ubuntu/.buildozer/android/platform/android-sdk platform-tools'
# Cwd /home/lee_ubuntu/.buildozer/android/platform/android-sdk
Exception in thread "main" java.lang.NoClassDefFoundError: javax/xml/bind/annotation/XmlSchema
        at com.android.repository.api.SchemaModule$SchemaModuleVersion.<init>(SchemaModule.java:156)
        at com.android.repository.api.SchemaModule.<init>(SchemaModule.java:75)
        at com.android.sdklib.repository.AndroidSdkHandler.<clinit>(AndroidSdkHandler.java:81)
        at com.android.sdklib.tool.sdkmanager.SdkManagerCli.main(SdkManagerCli.java:73)
        at com.android.sdklib.tool.sdkmanager.SdkManagerCli.main(SdkManagerCli.java:48)
Caused by: java.lang.ClassNotFoundException: javax.xml.bind.annotation.XmlSchema
        at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:581)
        at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:178)
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:522)
        ... 5 more
# Command failed: /home/lee_ubuntu/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager --sdk_root=/home/lee_ubuntu/.buildozer/android/platform/android-sdk platform-tools
```

이건 java버전으로 인한 문제
[에러슈팅 참고링크](https://github.com/kivy/buildozer/issues/1425)
난 java 11버전이 돌아가고 있었는데, javac-8, javac-15로 바꿔줘야한다고 한다.
