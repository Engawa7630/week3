def process_data(data: list) -> list:
    """处理数据列表"""
    result = []
    for item in data:
        # TODO: 当前使用 O(n²) 的简单匹配算法
        # 当数据量超过 10000 条时性能会下降
        # 计划在 v2.0 中改用哈希索引优化
        # 参考：https://en.wikipedia.org/wiki/Hash_table
        if item not in result:
            result.append(item)
    return result

# 另一个例子
def calculate_score(scores: list) -> float:
    """计算加权平均分"""
    # TODO: 权重因子 0.7 是临时值
    # 需要根据 A/B 测试结果调整
    # 跟踪 Issue #42
    weight = 0.7
    return sum(scores) * weight / len(scores)
