# FRPC 配置管理器

一个基于 Flask 的 Web 应用程序，用于管理和编辑 FRP 客户端的 TOML 配置文件。

GitHub: https://github.com/nomi982/frpc-panel

## Docker 启动方式

```bash
#先克隆源码
git clone https://github.com/nomi982/frpc-panel.git

# 使用 Docker Compose 一键启动
docker-compose up -d

# 访问管理界面
http://localhost:5000
```

## 源码启动方式

```bash
# 克隆项目
git clone https://github.com/nomi982/frpc-panel.git
cd frpc-panel

# 安装依赖
uv sync

# 启动应用
uv run python app.py

# 访问管理界面
http://localhost:5000
```

⚠️ **注意**: 修改完配置文件，需要将 FRPC 客户端进行重启才能使配置生效。

## 功能特性

### 配置文件管理
- 固定使用 `frpc.toml` 文件
- 页面加载时自动读取配置
- 实时保存修改到文件

### 配置结构支持
- `[common]` 全局配置部分
- 项目配置部分（如 `[ssh]`）
- 支持项目名称修改

### 网页端功能
- 分为全局设置和项目设置两部分
- 支持批量新增/删除项目
- 交互式输入验证：
  - IP地址格式验证
  - 端口号范围验证（1-65535）
  - 远程端口自动递增（从10000开始）
- 实时保存修改

## 安装和运行

### 前置要求
- Python 3.13+
- UV 包管理器

### 安装依赖
```bash
uv sync
```

### 运行应用
```bash
uv run python app.py
```

应用将在 http://127.0.0.1:5000 运行

## 项目结构

```
frpc/
├── app.py              # Flask 主应用
├── frpc.toml           # FRP 客户端配置文件
├── templates/
│   └── index.html      # 前端界面
├── pyproject.toml      # 项目配置和依赖
├── uv.lock             # 依赖锁定文件
└── README.md           # 项目说明
```

## API 接口

### 读取配置
```
GET /api/read_toml?file_path=frpc.toml
```

### 写入配置
```
POST /api/write_toml
Content-Type: application/json

{
  "content": {
    "common": {
      "server_addr": "1.1.1.1",
      "server_port": 7000,
      "token": "admin"
    }
  },
  "file_path": "frpc.toml"
}
```

## 配置格式

### 全局配置 (common)
```toml
[common]
server_addr = "1.1.1.1"    # 服务器地址
server_port = 7000         # 服务器端口
token = "admin123"         # 身份验证令牌
```

### 项目配置
```toml
[ssh]
type = "tcp"               # 类型 (tcp/udp/http/https)
local_ip = "127.0.0.1"     # 本地IP
local_port = 22            # 本地端口
remote_port = 10022        # 远程端口
```

## 使用说明

1. **启动应用**: 运行 `uv run python app.py`
2. **访问界面**: 在浏览器中打开 http://127.0.0.1:5000
3. **配置全局设置**: 填写服务器地址、端口和令牌
4. **管理项目**: 
   - 点击"新增项目"添加新服务
   - 使用复选框选择多个项目进行批量删除
   - 点击单个项目的"删除"按钮移除项目
5. **实时保存**: 所有修改会自动保存到 `frpc.toml` 文件

## 技术栈

- **后端**: Flask
- **前端**: 原生 JavaScript + HTML5 + CSS3
- **配置文件**: TOML (使用 tomli/tomli-w 库)
- **包管理**: UV
- **开发语言**: Python 3.13+

## 开发

### 添加新依赖
```bash
uv add package-name
```

### 同步依赖
```bash
uv sync
```

### 运行测试
应用启动后访问 http://127.0.0.1:5000 测试功能

## 注意事项

- 确保有写入 `frpc.toml` 文件的权限
- IP 地址格式会自动验证
- 端口号必须在 1-65535 范围内
- 远程端口默认从 10000 开始自动递增

## 许可证

MIT License
