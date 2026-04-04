.PHONY: check compile run arc

check:
	python3 launch.py --check

compile:
	python3 -m compileall ARC_Console launch.py

run:
	python3 launch.py

arc:
	python3 launch.py --arc-only
