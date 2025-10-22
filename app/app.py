from collections import defaultdict
from typing import List

def dedupe_header(columns: List[str]) -> List[str]:
    """
    通过向重复项附加数字后缀，使标题列名唯一。

规则：
   - 名称的第一次出现保持原样。
   - 同一名称的第 2、3、... 次出现会附加 ".1"、".2"、...。
   （这模仿了诸如 pandas 之类的工具如何处理重复的列标签。）
   - 顺序完全按给定的保留。
   - 输入是一个字符串列表（列名）；输出是一个相同长度的列表。

示例：
    ["id", "name", "id", "name", "name"] -> ["id", "name", "id.1", "name.1", "name.2"]
    """
    seen_counts = defaultdict(int)
    result: List[str] = []

    for col in columns:
        count = seen_counts[col]
        if count == 0:
            result.append(col)
        else:
            result.append(f"{col}.{count}")
        seen_counts[col] += 1

    return result
# hyq