FROM python:3.13-slim

# 安装 uv
RUN pip install --no-cache-dir uv -i https://pypi.tuna.tsinghua.edu.cn/simple

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY pyproject.toml uv.lock ./
COPY app.py ./
COPY templates/ ./templates/

# 安装依赖
RUN uv sync

# 暴露端口
EXPOSE 5000

# 启动应用
CMD ["uv", "run", "python", "app.py"]