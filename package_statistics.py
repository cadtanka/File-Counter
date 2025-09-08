import argparse
import gzip
import requests
from collections import defaultdict, Counter

# Constants
BASE_URL = "http://ftp.uk.debian.org/debian/dists/stable/main/"
CONTENTS_TEMPLATE = "Contents-{}.gz"

def download_contents_file(arch):
    # Download the compressed Contents file for given architecture
    url = f"{BASE_URL}/{CONTENTS_TEMPLATE.format(arch)}"
    response = requests.get(url, stream=True)

    if response.status_code != 200:
        raise Exception(f"Failed to download file: {url}")
    return gzip.decompress(response.content).decode("utf-8", errors="replace")

def parse_contents(contents_text):
    # Parses the Contents file and count files per package
    package_file_count = defaultdict(int)

    for line in contents_text.splitlines():
        if not line.strip() or line.startswith("FILE"):
            continue # Skip headers or empty lines
        try:
            filepath, packages = line.rsplit(maxsplit=1)
            for pkg in packages.split(','):
                pkg_name = pkg.strip().split('/')[-1] # Extract the package
                package_file_count[pkg_name] += 1
        except ValueError:
            continue # Skip ill-formatted lines

    return package_file_count

def print_top_packages(package_file_count, top_n=10):
    # Print the top N packages by file count
    top_packages = Counter(package_file_count).most_common(top_n)
    for pkg, count in top_packages:
        print(f"{pkg:<30} {count}")

def main():
    parser = argparse.ArgumentParser(description="Debian package file statistics")
    parser.add_argument("arch", help="Architecture (e.g, amd64, arm64, mips)")
    args = parser.parse_args()

    try:
        contents_text = download_contents_file(args.arch)
        package_file_count = parse_contents(contents_text)
        print_top_packages(package_file_count)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
