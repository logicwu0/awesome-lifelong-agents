"""Offline structure checks; not a scientific review or external link checker."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def check():
    errors = []
    papers = []
    for name in ("README.md", "README.zh-CN.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        ids = re.findall(r'https://arxiv.org/abs/(\d{4}\.\d{4,5})', text)
        papers.append(set(ids))
        if len(ids) != len(set(ids)):
            errors.append(f"{name}: duplicate paper")
        if not ids:
            errors.append(f"{name}: no papers")
        anchors = set(re.findall(r'<a id="([^"]+)"></a>', text))
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if target.startswith("#"):
                if target[1:] not in anchors:
                    errors.append(f"{name}: missing anchor {target}")
            elif not target.startswith(("https://", "http://")):
                if not (ROOT / target).is_file():
                    errors.append(f"{name}: missing file {target}")
        for placeholder in ("YOUR_GITHUB_USER", "YOUR_REPO"):
            if placeholder in text:
                errors.append(f"{name}: template placeholder {placeholder}")
        if "logicwu0/awesome-lifelong-agents&type=Date" not in text:
            errors.append(f"{name}: incorrect chart repository")
    if papers[0] != papers[1]:
        errors.append("English and Chinese paper sets differ")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"OK: {len(papers[0])} papers in both languages; local links and anchors valid.")


if __name__ == "__main__":
    check()
