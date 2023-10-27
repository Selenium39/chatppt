# 使用官方的 Python 3.8 基础镜像
FROM python:3.8-slim-buster

# 设置工作目录
WORKDIR /usr/src/app

# 复制项目文件到工作目录
COPY . .

# 安装项目所需的依赖项
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /usr/src/app/myapp

# 设置容器的启动命令，以运行项目
CMD ["python", "./flaskapp.py"]
