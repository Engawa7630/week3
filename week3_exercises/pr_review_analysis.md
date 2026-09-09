## 练习3：PR 评审意见分析

## 选择的 PR

**项目**：requests（Python HTTP 库）  
**PR 链接**：https://github.com/psf/requests/pull/6685  
**主题**：修复 SSL 验证问题

---

## 评审意见分类

### 高效的评论

**评论1**（来自维护者 @sigmavirus24）：
> "This fix looks correct, but please add a test case that reproduces the original issue. Without a test, we risk regressing this in the future."

**为什么高效**：
- 明确指出了当前修改的不足（缺少测试）
- 给出了具体的行动要求（添加测试用例）
- 解释了为什么这是必要的（防止回归）

**评论2**（来自贡献者 @nateprewitt）：
> "Good catch! However, have you considered using `verify=False` instead of patching the session? It's a smaller change with less surface area."

**为什么高效**：
- 先肯定了贡献者的工作（"Good catch"）
- 提出了一个替代方案，并解释了其优点（改动更小、风险更低）
- 语气友好，没有贬低对方的方案

---

### 低效的评论

**评论3**（假设示例）：
> "This is wrong. Fix it."

**为什么低效**：
- 没有说明哪里"wrong"
- 没有提供如何"fix it"的指导
- 语气生硬，可能打击贡献者的积极性

---

## 如果你是 PR 作者，收到这些评论的体验如何？

收到评论1和评论2时，我会有以下感受：
1. **感受到尊重**：评论者先肯定了我的工作，再提出改进建议。
2. **有明确的行动方向**：我知道下一步该做什么（添加测试、考虑替代方案）。
3. **学到了东西**：我了解到项目对测试覆盖的重视，以及某些改动有更优雅的实现方式。

相反，如果只收到评论3，我可能会感到挫败，并且不知道该从哪里修改。
