import random
import pyperclip

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """生成随机密码 - 开发者：zxc10089"""
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if use_upper else ''
    digits = '0123456789' if use_digits else ''
    symbols = '!@#$%^&*()' if use_symbols else ''
    
    all_chars = lowercase + uppercase + digits + symbols
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
        
        pyperclip.copy(password)
        print("📋 已复制到剪贴板!")
    except Exception as e:
        print(f"⚠️ 出错: {e}")