#!/usr/bin/env python3
import argparse
import re

from data import Node

INFO_SEP = re.compile(r'\s*,\s*')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("list_file", type=str, help="name of list file")
    parser.add_argument("map_file", type=str, help="name of input file")
    args = parser.parse_args()
    all_nodes = list()
    with open(args.map_file, 'r') as f:
        for raw_line in f:
            line = raw_line.strip()
            x, y, name, *items = INFO_SEP.split(line)
            all_nodes.append(Node(float(x), float(y), name, frozenset(items)))
    groceries = list()
    with open(args.list_file, 'r') as f:
        groceries = set(raw_line.strip() for raw_line in f)
    start = all_nodes[0]
    nodes = set(
        node for node in all_nodes
        if node == start
        or (groceries & node.items)
        )
    print("Groceries: %s" % (", ".join(groceries) or "[none]"))
    msg = "Need to visit %s of %s nodes:" % (len(nodes), len(all_nodes))
    print(msg)
    print(", ".join(node.name for node in nodes) or "[none]")

if __name__ == '__main__':
    main()
