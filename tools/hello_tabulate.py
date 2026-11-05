import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser()
parser.add_argument("--name", default="World")
args = parser.parse_args()

print(f"Hello, {args.name}!\n")

table_data = [["Student ID", "23120185"], ["Course", "Open Source Software"], ["Library", "tabulate==0.10.0"]]
headers = ["Key", "Value"]

print(tabulate(table_data, headers=headers, tablefmt="grid"))
