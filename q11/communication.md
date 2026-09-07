## Issue

**环境**：Windows 10 22H2，Python 3.8，sdt-greet 0.1.0（待确认其他版本）

**复现命令**：

sdt-greet --name " "


**期望结果**：
- 输出错误信息 `Error: name cannot be blank`
- 退出码为 2

**实际结果**：
- 输出 `Hello,  !`（包含空格）
- 退出码为 0

---

## 提交信息

**标题**：fix: handle blank name input with non-zero exit code

**正文**：
当 `--name` 参数为空白字符串或仅含空格时，程序当前忽略此情况，打印带空名字的问候语并以状态码 0 退出。

此补丁修改如下：
- 增加输入验证：若 name 为空或只含空白字符，则输出错误到 stderr
- 以状态码 2 退出，符合 CLI 工具约定

---

## 评审意见

**Blocking**：
- 当前检查 `not a.name or a.name.isspace()` 可以覆盖空字符串和纯空格，建议统一使用 `if not a.name.strip():` 来处理所有空白情况。
- 需要补充单元测试覆盖该边缘情况。

**Suggestion**：
- 可在参数解析阶段添加 `type` 自定义检查，但当前实现足够。

**Nit**：
- 错误信息可更具体，如 `Error: --name argument cannot be blank`。
