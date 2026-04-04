#!/usr/bin/env python3
"""
Master Control — Universe Engine + ARC Spine
Single-command boot for the unified SURE + ARC system.

Usage:
    python launch.py              # start ARC and open Master Control
    python launch.py --arc-only   # ARC backend only
    python launch.py --sure-only  # open universe observer only
    python launch.py --master-only # open Master Control only
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
MASTER_FILE = ROOT / "MasterControl.html"
UNIVERSE_FILE = ROOT / "sure" / "universe_observer_v16_vision.html"

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

    # Front-end files
    if MASTER_FILE.exists():
        print(f"[OK]   Master Control: {MASTER_FILE.name}")
    else:
        print(f"[MISS] Master Control file not found at {MASTER_FILE}")
        ok = False

    if UNIVERSE_FILE.exists():
        print(f"[OK]   Universe engine: {UNIVERSE_FILE.name}")
    else:
        print(f"[MISS] Universe file not found at {UNIVERSE_FILE}")
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

def open_universe():
    url = UNIVERSE_FILE.as_uri()
    print(f"\n[SURE] Opening Universe Engine: {url}")
    webbrowser.open(url)

def open_master():
    url = MASTER_FILE.as_uri()
    print(f"\n[MC]   Opening Master Control: {url}")
    webbrowser.open(url)

def main():
    parser = argparse.ArgumentParser(description="Master Control launcher")
    parser.add_argument("--arc-only",  action="store_true")
    parser.add_argument("--sure-only", action="store_true")
    parser.add_argument("--master-only", action="store_true")
    parser.add_argument("--check",       action="store_true")
    args = parser.parse_args()

    print("=" * 60)
    print("  MASTER CONTROL — Universe Engine + ARC Spine")
    print("=" * 60)

    if args.check or not (args.arc_only or args.sure_only or args.master_only):
        ok = check_env()
        if args.check:
            sys.exit(0 if ok else 1)
        if not ok:
            print("\n[WARN] Environment issues detected — continuing anyway.")

    procs = []

    if not args.sure_only and not args.master_only:
        procs.append(start_arc())
        time.sleep(1.5)   # let ARC boot before browser opens

    if args.sure_only:
        open_universe()
    elif args.master_only:
        open_master()
    elif not args.arc_only:
        open_master()

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
