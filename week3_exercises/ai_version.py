# AI 辅助生成的代码
# 提示：写一个 Python 函数统计字符串中每个字符的出现次数

from collections import Counter

def count_chars_ai(s: str) -> dict:
    """使用 Counter 统计字符出现次数"""
    return dict(Counter(s))

# 测试
print(count_chars_ai("hello world"))
