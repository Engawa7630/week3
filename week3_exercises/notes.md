## 练习7：手动编码 vs AI 辅助编程

### 手动编码体验

**任务**：写一个函数，统计字符串中每个字符出现的次数

**耗时**：约 2 分钟

**思考过程**：
1. 需要遍历字符串中的每个字符
2. 需要一个字典来存储字符和次数的映射
3. 如果字符已在字典中，次数 +1；否则初始化为 1

**遇到的困难**：
- 没有遇到明显困难，这是一个很基础的任务

**代码**：
```python
def count_chars_manual(s: str) -> dict:
    result = {}
    for ch in s:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result
AI 辅助编程体验
使用的 AI 工具：GitHub Copilot / ChatGPT

给出的提示：

"写一个 Python 函数，统计字符串中每个字符出现的次数，用字典返回结果"

生成代码：

python
from collections import Counter

def count_chars_ai(s: str) -> dict:
    return dict(Counter(s))
生成代码的质量：很好，使用了标准库的 Counter 类

需要多少修正：不需要修正，代码可以直接使用

对比结论
维度  |  手动编码   |   AI 辅助
时间  | ~2 分钟   |~10 秒
代码质量 |  正确，但可以更优雅    | 使用了最合适的标准库
学习收获 |  复习了 dict 操作  |  知道了 Counter 类的存在
适用场景 |  适合巩固基础知识   |适合快速获取已知问题的解决方案
思考：

AI 辅助能显著提高效率，尤其是对于有标准解法的"已知问题"

手动编码仍然重要，因为它帮助你理解底层原理

最佳实践可能是：新手先手动编码，熟练后善用 AI 辅助
