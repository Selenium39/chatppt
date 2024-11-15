# ChatPPT

ChatPPT 是一个基于 AI 的演示文稿生成工具，能够根据用户输入的内容自动生成专业的 PowerPoint 演示文稿。

## 功能特点

- 🚀 快速生成：只需输入标题和内容，即可自动生成完整的演示文稿
- 🎨 多样模板：提供简约、明亮和深色三种专业模板供选择
- 📝 智能排版：自动进行内容分析和页面布局
- 🖼️ 自动配图：可选择是否自动为幻灯片添加相关图片
- 🔒 用户系统：支持用户注册和登录功能

## 使用界面

### 首页和生成界面
![生成界面](https://github.com/Selenium39/chatppt/raw/master/examples/1.jpg)
![输入界面](https://github.com/Selenium39/chatppt/raw/master/examples/2.jpg)

### 生成效果展示
![演示文稿示例1](https://github.com/Selenium39/chatppt/raw/master/examples/3.jpg)
![演示文稿示例2](https://github.com/Selenium39/chatppt/raw/master/examples/4.jpg)
![演示文稿示例3](https://github.com/Selenium39/chatppt/raw/master/examples/5.jpg)
![演示文稿示例4](https://github.com/Selenium39/chatppt/raw/master/examples/6.jpg)
![演示文稿示例5](https://github.com/Selenium39/chatppt/raw/master/examples/7.jpg)

## 使用演示

查看完整使用演示视频：[示例视频](https://github.com/Selenium39/chatppt/raw/master/examples/video.mp4)

## 技术栈

- 后端：Flask
- 前端：HTML, CSS, JavaScript, jQuery
- 数据库：SQLite
- AI 接口：Dify.ai API
- 用户认证：Flask-Login
- 密码加密：Flask-Bcrypt

## 快速开始

1. 克隆项目
```bash
git clone https://github.com/YourUsername/chatppt.git
cd chatppt
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
创建 `.env` 文件并添加以下配置：
```
SECRET_KEY=your_secret_key
OPENAI_API_KEY=your_dify_api_key
PEXELS_API_KEY=your_pexels_api_key
```

4. 运行项目
```bash
cd myapp
python flaskapp.py
```

访问 `http://localhost:5001` 即可使用

## 主要功能

1. **用户管理**
   - 用户注册
   - 用户登录
   - 用户注销

2. **演示文稿生成**
   - 自定义标题和作者
   - 设置幻灯片数量
   - 输入演示文稿内容
   - 选择模板样式
   - 可选自动配图功能

3. **文件处理**
   - 生成 PowerPoint 文件
   - 文件下载功能

## 注意事项

- 自动配图功能可能会插入不太相关的图片，请根据实际需求选择是否使用
- 建议输入详细的内容描述以获得更好的生成效果
- 生成时间可能因内容长度和服务器负载而异

## 许可证

MIT License

## 联系方式

如有问题或建议，欢迎提出 Issue 或 Pull Request。
