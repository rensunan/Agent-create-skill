import re, yaml
from pathlib import Path

path = Path(r"C:\Users\ADMIN\Desktop\系统\个人skill\智能体创建skill\agent-creator\SKILL.md")
content = path.read_text(encoding="utf-8")

ok = True

# 1. Basic structure
print("1. Starts with ---:", content.startswith("---"))
match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
if match:
    fm = yaml.safe_load(match.group(1))
    print(f"2. name: {fm.get('name')}, desc: {len(fm.get('description',''))} chars")
else:
    print("2. Frontmatter: MISSING"); ok = False

# 3. Check numbered option pattern
checks = [
    ("选项式交互", "选项式交互" in content),
    ("0 = 都不满意", content.count("都不满意，我们详细讨论")),
    ("编号选项格式 1.", content.count("1. ")),
    ("编号选项格式 0.", content.count("0. ")),
    ("问题标题格式【】", "【" in content),
]
for name, val in checks:
    status = "✓" if val else "✗"
    print(f"3. {status} {name}: {val}")
    if not val: ok = False

# 4. All phases still present
phases = ["阶段一", "阶段二", "阶段三", "阶段四", "阶段五", "阶段六"]
for p in phases:
    present = p in content
    print(f"4. {p}: {'✓' if present else '✗'}")
    if not present: ok = False

print(f"\n{'ALL OK' if ok else 'ISSUES FOUND'}")
