"""Fail closed on obvious private-source inclusions, source links and PII.

A technical scanner does NOT itself authorise publishing restricted survey information.
"""
from pathlib import Path
from urllib.parse import unquote
import re
ROOT=Path(__file__).resolve().parents[1]
BANNED={".sav",".spv",".sps",".xls",".xlsx",".doc",".docx",".pdf",".zip",".sqlite",".db"}
EMAIL=re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
LINK=re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SKIP={".git",".venv","__pycache__",".pytest_cache","local_results"}
def scan():
    errors=[]
    count=0
    for p in ROOT.rglob("*"):
        if not p.is_file() or set(p.relative_to(ROOT).parts)&SKIP:
            continue
        count+=1
        if p.suffix.lower() in BANNED:
            errors.append(f"restricted extension: {p.relative_to(ROOT)}")
            continue
        if p.suffix.lower() not in {".py",".md",".csv",".yml",".yaml",".cff",".svg",".ipynb",".txt",""}:
            errors.append(f"unknown extension: {p.relative_to(ROOT)}")
            continue
        try:
            s=p.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"binary/unreadable: {p.relative_to(ROOT)}")
            continue
        for email in EMAIL.findall(s):
            if not email.endswith((".example.org",".example.net",".example.com")):
                errors.append(f"possible email/identity: {p.relative_to(ROOT)}")
        if p.suffix.lower()==".md":
            for m in LINK.finditer(s):
                url=m.group(1).split("#")[0].strip("<>").split(" ")[0]
                if not url or url.startswith(("https:","http:","mailto:","data:","/")):continue
                path=(p.parent/unquote(url)).resolve()
                if not path.is_relative_to(ROOT.resolve()) or not path.exists():
                    errors.append(f"broken local link: {p.relative_to(ROOT)} -> {url}")
    return errors,count
if __name__=="__main__":
    errors,count=scan()
    if errors:raise SystemExit("\n".join(errors))
    print(f"PASS: {count} files scanned; no obvious respondent files, contact emails or broken local links.")
