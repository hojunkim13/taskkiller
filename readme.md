# TaskKiller v1.0

Simple TaskKiller with python.  
파이썬으로 만들어진 간단한 프로세스 킬러입니다.    
  
It is designed to support the mining of PC Bangs that have left computing resources due to COVID-19.   
코로나로 인하여 컴퓨팅 자원이 남는 PC방의 채굴을 지원하기 위한 목적으로 제작되었습니다.

Deploy as an executable file for comfortable.  
사용자의 편의를 위하여 실행파일로 배포합니다.

Executable file is made with pyinstaller 4.2.0  
실행 파일은 pyinstaller 4.2.0 버전을 통하여 제작되었습니다.
```
pyinstllaer -i ico.ico --onefile --noconsole taskkiller.py
```

Please test with test process such as MSPaint('mspaint.exe') before using.  
사용 전 그림판(mspaint.exe) 등의 파일로 테스트하시길 권합니다.
   


## Getting Started

### Prerequisites (Python only)

* Python 3.x
* psutil
* keyboard
```
pip install psutil, keyboard
```
### Install
* Python
    * ```
        git clone https://github.com/hojunkim13/taskkiller
        ```
* Executable (Download these files.)  
    * `taskkill.exe`
    * `config.txt`

## Run
* Python
```
python taskkiller.py
```
* Executable  
`taskkill.exe`
 
After run this, Taskkiller respond to any keyboard inputs to kill target processes in `config.txt`

So, Please check `config.txt` to set target processes.


## Contributing

Please read [CONTRIBUTING.md]() for details on our code of conduct, and the process for submitting pull requests to me.
