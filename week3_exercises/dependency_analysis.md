## 练习9：Python 依赖关系分析

### 直接依赖
- requests==2.32.3
- flask==3.0.0

### 间接依赖（requests 的依赖）
根据 pip 安装输出，requests 依赖：
- charset-normalizer<4,>=2
- idna<4,>=2.5
- urllib3<3,>=1.21.1
- certifi>=2017.4.17

### 间接依赖（flask 的依赖）
flask 依赖：
- Werkzeug>=3.0.0
- Jinja2>=3.1.2
- itsdangerous>=2.1.2
- click>=8.1.3
- blinker>=1.6.2

### 为什么需要区分直接和间接依赖？
1. 直接依赖是开发者明确选择的
2. 间接依赖是自动引入的，可能引入安全漏洞
3. 升级直接依赖时可能影响间接依赖的版本
4. 使用 pip freeze > requirements.txt 会列出所有依赖（包括间接的）
