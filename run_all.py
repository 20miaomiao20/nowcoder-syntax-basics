#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
本地自动判题脚本（不依赖牛客，离线验证每份题解能否跑过样例）。

用法:
    python run_all.py              # 跑全部题目
    python run_all.py 16570        # 只跑某道题（按题号前缀匹配）
    python run_all.py -v           # 失败时打印完整期望/实际输出

约定:
    题解文件:  <分类目录>/<题号>_<中文题名>.py
    样例文件:  tests/<题号>_<序号>.in  与  tests/<题号>_<序号>.out
"""

from __future__ import annotations

import difflib
import re
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
TESTS = BASE / "tests"
PYTHON = sys.executable
ID_RE = re.compile(r"(\d{5,6})")   # 牛客题号有 5 位（NC16570）也有 6 位（NC213204）


def collect_solutions() -> list[Path]:
    """收集所有题解文件（排除本脚本自身）。"""
    return sorted(
        p for p in BASE.rglob("*.py")
        if p.name != Path(__file__).name and not p.name.startswith("_")
    )


def problem_id(path: Path) -> str | None:
    m = ID_RE.search(path.name)
    return m.group(1) if m else None


def normalize(text: str) -> str:
    """判题式宽松比较：忽略行尾空格与文件末尾空行。"""
    lines = [ln.rstrip() for ln in text.replace("\r\n", "\n").split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def run_case(solution: Path, case_in: Path) -> tuple[bool, str, str, str]:
    stdin_data = case_in.read_bytes()
    try:
        proc = subprocess.run(
            [PYTHON, str(solution)],
            input=stdin_data,
            capture_output=True,
            timeout=10,
            cwd=solution.parent,
        )
    except subprocess.TimeoutExpired:
        return False, "<timeout>", "", "运行超时（>10s）"

    out = proc.stdout.decode("utf-8", errors="replace")
    err = proc.stderr.decode("utf-8", errors="replace")
    if proc.returncode != 0:
        return False, out, err, f"退出码 {proc.returncode}"

    expected_path = case_in.with_suffix(".out")
    if not expected_path.exists():
        return True, out, err, "无期望输出，仅检查能否运行"

    expected = expected_path.read_text(encoding="utf-8")
    if normalize(out) == normalize(expected):
        return True, out, err, "OK"
    return False, out, err, "输出与样例不一致"


def diff_hint(expected: str, actual: str) -> str:
    exp = normalize(expected).split("\n")
    act = normalize(actual).split("\n")
    lines = list(difflib.unified_diff(exp, act, "期望", "实际", lineterm="", n=1))
    return "\n".join(lines[:40])


def main(argv: list[str]) -> int:
    verbose = "-v" in argv
    filters = [a for a in argv[1:] if not a.startswith("-")]

    solutions = collect_solutions()
    if filters:
        solutions = [s for s in solutions if any(f in s.name for f in filters)]

    if not solutions:
        print("没有找到题解文件。")
        return 1

    total = passed = 0
    failures: list[str] = []
    current_group = None

    for sol in solutions:
        group = sol.parent.name
        if group != current_group:
            current_group = group
            print(f"\n== {group} ==")
        pid = problem_id(sol)
        cases = sorted(TESTS.glob(f"{pid}_*.in")) if pid else []
        if not cases:
            print(f"  [SKIP] {sol.name}   （tests/ 下没有 {pid}_*.in）")
            continue
        for case_in in cases:
            total += 1
            ok, out, err, reason = run_case(sol, case_in)
            tag = "PASS" if ok else "FAIL"
            print(f"  [{tag}] {sol.name}  ({case_in.name}: {reason})")
            if ok:
                passed += 1
                continue
            failures.append(f"{sol.name} / {case_in.name}")
            if err.strip():
                print("         stderr:", err.strip().splitlines()[-1][:300])
            exp = case_in.with_suffix(".out")
            if exp.exists():
                hint = diff_hint(exp.read_text(encoding="utf-8"), out)
                if verbose:
                    print(hint)
                else:
                    print("         " + (hint.splitlines()[0] if hint else ""))

    print(f"\n{'=' * 46}\n通过 {passed}/{total}")
    if failures:
        print("未通过用 -v 查看完整差异：")
        for f in failures:
            print("  -", f)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
