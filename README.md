# 🔒 SimplePassGenerator - 手机密码生成器
**开发者**：zxc10089 (xcwm95@163.com) | [项目链接](https://github.com/zxc10089/SimplePassGenerator)

## 功能特点
- 生成8-50位安全密码
- 自定义包含大写字母/数字/特殊符号
- 自动复制到剪贴板（使用Termux API）

## 📱 手机使用指南
```bash
# 1. 安装Python
pkg install python

# 2. 安装Termux:API（必须）
pkg install termux-api

# 3. 从Google Play安装"Termux:API"应用
#    链接：https://play.google.com/store/apps/details?id=com.termux.api

# 4. 授予剪贴板权限（首次运行需操作）
termux-clipboard-set "测试"
#    手机将弹出权限请求 → 点击"允许"

# 5. 运行程序
python pass_generator.py