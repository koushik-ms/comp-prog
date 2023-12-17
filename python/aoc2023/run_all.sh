#!/usr/bin/env sh

for d in day*; do
  time python -m "${d}.${d}"
done

