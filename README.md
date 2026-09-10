##🐶 Cute Animal Show (可爱动物展示平台)

这是一个基于 **Django** 框架开发的 Web 应用程序，旨在展示各种可爱的动物照片和详细信息。用户可以通过该平台浏览动物档案，并进行注册和登录以[...]

✨ 主要功能

  动物展示：浏览高清动物图片和详细品种介绍。
  用户系统：支持用户注册、登录和安全退出。
  响应式设计：界面简洁美观，适配不同设备。
  后台管理：基于 Django Admin 的强大数据管理功能。

📸 效果展示

![Cute Animals Showcase](images/animals/showcase.png)

🛠️ 技术栈

后端：Python, Django
数据库：SQLite (默认)
前端：HTML5, CSS3, Bootstrap

🚀 如何启动项目

在本地运行此项目非常简单，请按照以下步骤操作：

1. 克隆仓库
```bash
git clone https://github.com/HLIU5F/cute-animal.git
cd cute-animal
```

2. 创建虚拟环境并安装依赖
```bash
# Windows 系统
python -m venv venv
venv\Scripts\activate

# Mac/Linux 系统
# python3 -m venv venv
# source venv/bin/activate

# 安装依赖包
pip install -r requirements.txt
```

3. 数据库迁移
```bash
python manage.py migrate
```

4. 启动开发服务器
```bash
python manage.py runserver
```

现在，打开浏览器访问 http://127.0.0.1:8000 即可看到可爱的动物们！

📝 许可证

本项目仅供学习和交流使用。
