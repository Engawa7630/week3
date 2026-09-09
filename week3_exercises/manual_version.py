def count_chars_manual(s: str) -> dict:
    """手动编码：统计字符串中每个字符出现的次数"""
    result = {}
    for ch in s:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result

# 测试
print(count_chars_manual("hello world"))
