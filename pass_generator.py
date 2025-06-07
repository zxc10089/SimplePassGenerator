import random
import subprocess

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """生成随机密码 - 开发者：zxc10089"""
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if use_upper else ''
    digits = '0123456789' if use_digits else ''
    symbols = '!@#$%^&*()' if use_symbols else ''
    
    all_chars = lowercase + uppercase + digits + symbols
    if not all_chars:
        return "请至少启用一种字符类型"
    
    length = max(4, min(length, 50))
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔒 密码生成器 by zxc10089 🔒")
    print("-" * 30)
    try:
        length = int(input("密码长度 (默认12): ") or 12)
        upper = input("包含大写字母? (y/n): ").lower() == 'y'
        digits = input("包含数字? (y/n): ").lower() == 'y'
        symbols = input("包含符号? (y/n): ").lower() == 'y'
        
        password = generate_password(length, upper, digits, symbols)
        print("\n✅ 生成的密码:", password)
        
        # 使用Termux剪贴板API
        try:
            subprocess.run(["termux-clipboard-set", password], check=True)
            print("📋 已复制到剪贴板!")
        except Exception as clip_error:
            print(f"⚠️ 复制失败: {str(clip_error)}")
            print("请确保已安装Termux:API应用并授予权限")
            
    except Exception as e:
        print(f"⚠️ 程序出错: {str(e)}")
        print("请检查输入是否正确")