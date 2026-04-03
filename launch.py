#!/usr/bin/env python3
"""
Master Control — Universe Engine + ARC Spine
Single-command boot for the unified SURE + ARC system.

Usage:
    python launch.py              # start both services
    python launch.py --arc-only   # ARC backend only
    python launch.py --sure-only  # open SURE universe engine only
    python launch.py --check      # verify environment only
"""
import argparse
import subprocess
import sys
import os
import webbrowser
import time
from pathlib import Path

ROOT    = Path(__file__).resolve().parent
ARC_DIR = ROOT / "ARC_Console"
SURE_FILE = ROOT / "sure" / "universe_observer_v10_master_control.html"

ARC_HOST  = "127.0.0.1"
ARC_PORT  = 8000

def check_env():
    ok = True
    # Python version
    if sys.version_info < (3, 10):
        print(f"[FAIL] Python ≥ 3.10 required (got {sys.version})")
        ok = False
    else:
        print(f"[OK]   Python {sys.version.split()[0]}")

    # uvicorn + fastapi
    for pkg in ["uvicorn", "fastapi", "pydantic"]:
        try:
            __import__(pkg)
            print(f"[OK]   {pkg}")
        except ImportError:
            print(f"[MISS] {pkg} — run: pip install {pkg}")
            ok = False

    # SURE file
    if SURE_FILE.exists():
        print(f"[OK]   SURE engine: {SURE_FILE.name}")
    else:
        print(f"[MISS] SURE file not found at {SURE_FILE}")
        ok = False

    # ARC package
    if (ARC_DIR / "arc" / "api" / "main.py").exists():
        print(f"[OK]   ARC-Core at {ARC_DIR}")
    else:
        print(f"[MISS] ARC main.py not found at {ARC_DIR}")
        ok = False

    return ok

def start_arc():
    print(f"\n[ARC]  Starting ARC-Core on http://{ARC_HOST}:{ARC_PORT}")
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ARC_DIR)
    return subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "arc.api.main:app",
         "--host", ARC_HOST, "--port", str(ARC_PORT), "--reload"],
        cwd=str(ARC_DIR),
        env=env,
    )

def open_sure():
    url = SURE_FILE.as_uri()
    print(f"\n[SURE] Opening Universe Engine: {url}")
    webbrowser.open(url)

def main():
    parser = argparse.ArgumentParser(description="Master Control launcher")
    parser.add_argument("--arc-only",  action="store_true")
    parser.add_argument("--sure-only", action="store_true")
    parser.add_argument("--check",     action="store_true")
    args = parser.parse_args()

    print("=" * 60)
    print("  MASTER CONTROL — Universe Engine + ARC Spine")
    print("=" * 60)

    if args.check or not (args.arc_only or args.sure_only):
        ok = check_env()
        if args.check:
            sys.exit(0 if ok else 1)
        if not ok:
            print("\n[WARN] Environment issues detected — continuing anyway.")

    procs = []

    if not args.sure_only:
        procs.append(start_arc())
        time.sleep(1.5)   # let ARC boot before browser opens

    if not args.arc_only:
        open_sure()

    if procs:
        print(f"\n[INFO] ARC dashboard: http://{ARC_HOST}:{ARC_PORT}/")
        print("[INFO] Press Ctrl+C to stop.\n")
        try:
            for p in procs:
                p.wait()
        except KeyboardInterrupt:
            print("\n[STOP] Shutting down...")
            for p in procs:
                p.terminate()

if __name__ == "__main__":
    main()
