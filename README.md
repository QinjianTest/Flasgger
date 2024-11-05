# 项目简介

用于公司内部测试快速查询以及构建数据的平台
使用的是Flasgger框架

## 特性

- 从 JSON 响应中提取特定类型的内容。
- 支持通过 API 端点访问和测试。
- 易于配置和扩展。

## 安装

### 克隆存储库：

```bash
   git clone https://github.com/QinjianTest/Flasgger.git
```
### 创建并激活虚拟环境
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
```

### 安装依赖
```bash
pip install -r requirements.txt
```
## 使用方法
启动 Flask 应用：
```bash
python app.py
```
使用浏览器或 API 客户端（如 Postman）访问 API 端点。


#### 扩展：配置
可创建配置文件位于 config.py，你可以在其中设置 API 主机、用户凭据和其他配置。
base_cookies 和 headers 的静态部分在 config.py 中定义

