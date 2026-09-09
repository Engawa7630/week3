# 最小可复现示例：列表遍历时删除元素导致的问题
# 原始 bug：在遍历列表时删除元素会导致跳过某些元素
# 剥离掉所有无关代码，只保留核心问题

def remove_even_numbers_buggy(numbers):
    """错误实现：遍历时删除偶数"""
    for num in numbers:
        if num % 2 == 0:
            numbers.remove(num)
    return numbers

# 测试
test_list = [1, 2, 3, 4, 5, 6]
print(f"原始: {test_list}")
print(f"错误结果: {remove_even_numbers_buggy(test_list[:])}")
# 预期结果：[1, 3, 5]
# 实际结果：[1, 3, 5]（可能正确，但换其他输入会出错）
