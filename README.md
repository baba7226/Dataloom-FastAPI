# Data Loom Cleaning Microservice

这是一个基于 **FastAPI** 的后端微服务，专门设计为供 **Spring Boot** 或其他系统调用，提供 **CSV 文件的自动分析与数据清洗推荐能力**。

---

## 🎯 功能特点

- 支持上传 CSV 文件
- 自动分析字段特征：
  - 缺失率
  - 唯一值数量
  - 数据类型
  - 是否为日期字段
- 返回字段级的清洗建议：
  - 缺失值填充/删除
  - 编码建议
  - 日期格式转换建议
- 易集成微服务接口，方便前后端或跨系统调用

---

## 🗂️ 项目结构

```
app/
  api/           # 路由接口
  models/        # Pydantic 数据模型
  services/      # 业务逻辑（分析与推荐）
  utils/         # 工具函数
  main.py        # 应用入口
requirements.txt # 依赖文件
README.md        # 项目说明
```



---

## ⚙️ 技术栈

- Python 3.10+
- FastAPI
- Pandas
- Pydantic

---

## 📦 安装依赖

请先确认已安装 Python 3.10 或更高版本。

```bash
pip install -r requirements.txt
```
## 🚀 本地运行
使用 Uvicorn 启动开发服务器：

```bash
uvicorn app.main:app --reload
```

默认访问地址：

```cpp
http://127.0.0.1:8000
```

## 📑 访问API文档
FastAPI 自动生成的交互式文档：

- Swagger UI:
http://127.0.0.1:8000/docs

- ReDoc 文档:
http://127.0.0.1:8000/redoc
=======
# Dataloom-FastAPI
为dataloom数据处理所准备的FastAPI后端微服务（现仅处于初级阶段）

