import argparse
import os
import sys
import time
import json
import threading
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen
from urllib.parse import urlencode


API_LIST = "https://cie.fraft.cn/obj/Common/Fetch/renum"
API_REDIR = "https://cie.fraft.cn/obj/Common/Fetch/redir/"


def fetch_file_list(subject, year, season, include_ms=False):
    data = urlencode({"subject": subject, "year": year, "season": season}).encode()
    req = Request(API_LIST, data=data)
    with urlopen(req) as resp:
        payload = json.loads(resp.read())
    files = []
    for row in payload.get("rows", []):
        name = row["file"]
        if "_qp_" in name:
            files.append(name)
        elif include_ms and "_ms_" in name:
            files.append(name)
    return files


def download_file(url, dest, max_retries=3):
    for attempt in range(max_retries):
        try:
            req = Request(url)
            with urlopen(req) as resp:
                with open(dest, "wb") as f:
                    while True:
                        chunk = resp.read(8192)
                        if not chunk:
                            break
                        f.write(chunk)
            return True
        except Exception as e:
            if attempt < max_retries - 1 and "429" in str(e):
                wait = 2 ** attempt
                time.sleep(wait)
                continue
            raise


def main():
    parser = argparse.ArgumentParser(description="Fetch CIE question papers from Frank's CIE workshop")
    parser.add_argument("--subject", default="9231", help="Subject code (default: 9231)")
    parser.add_argument("--years", default="2020-2025", help="Year range (default: 2020-2025)")
    parser.add_argument("--season", default="Jun,Nov", help="Seasons (default: Jun,Nov)")
    parser.add_argument("--out", default="papers", help="Output directory (default: papers)")
    parser.add_argument("--paper", type=int, help="Paper number to download (e.g. 2 for Paper 2)")
    parser.add_argument("--ms", action="store_true", help="Also download mark scheme files")
    parser.add_argument("--workers", type=int, default=4, help="Download threads (default: 4)")
    parser.add_argument("--delay", type=float, default=0.5, help="Min seconds between requests (default: 0.5)")
    args = parser.parse_args(args=None if sys.argv[1:] else ["--help"])

    def matches_paper(name):
        if args.paper is None:
            return True
        marker = "_qp_" if "_qp_" in name else "_ms_"
        idx = name.index(marker) + len(marker)
        return idx < len(name) and name[idx].isdigit() and int(name[idx]) == args.paper

    if "-" in args.years:
        parts = args.years.split("-")
        years = list(range(int(parts[0]), int(parts[1]) + 1))
    else:
        years = [int(y) for y in args.years.split(",")]

    seasons = args.season.split(",")
    lock = threading.Lock()
    tasks = []

    for year in years:
        for season in seasons:
            print(f"[{year} {season}] Fetching file list...")
            try:
                files = fetch_file_list(args.subject, year, season, args.ms)
            except Exception as e:
                print(f"  ERROR: {e}")
                continue

            if not files:
                print("  No files found.")
                continue

            files = [f for f in files if matches_paper(f)]
            paper_dir = os.path.join(args.out, str(args.subject), f"{year}_{season}")
            os.makedirs(paper_dir, exist_ok=True)

            for fname in files:
                dest = os.path.join(paper_dir, fname)
                tasks.append((API_REDIR + fname, dest, fname))

    if not tasks:
        print("No files to download.")
        return

    print(f"\nDownloading {len(tasks)} file(s) with {args.workers} thread(s)...\n")

    results = {"ok": 0, "skip": 0, "fail": 0}
    rate_limiter = threading.Semaphore(args.workers)

    def work(item):
        url, dest, fname = item
        if os.path.exists(dest):
            with lock:
                print(f"  SKIP  {fname}")
                results["skip"] += 1
            return
        with rate_limiter:
            try:
                download_file(url, dest)
                with lock:
                    print(f"  OK    {fname}")
                    results["ok"] += 1
            except Exception as e:
                with lock:
                    print(f"  FAIL  {fname}: {e}")
                    results["fail"] += 1
            finally:
                time.sleep(args.delay)

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        pool.map(work, tasks)

    print(f"\n{'='*40}")
    print(f"Downloaded: {results['ok']} | Skipped: {results['skip']} | Failed: {results['fail']}")
    print(f"Saved to: {os.path.abspath(args.out)}\\{args.subject}")


if __name__ == "__main__":
    main()
