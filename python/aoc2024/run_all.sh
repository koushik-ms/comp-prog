#!/usr/bin/env sh

for d in day*; do
	echo "=== Running solution for ${d} ==="
	time python3 -m "${d}.${d}"
	echo "=================================="
done
