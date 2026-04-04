# Contributing

Thanks for contributing.

## Guidelines

- keep deterministic behavior explicit where possible
- avoid overstating scientific guarantees in docs or code comments
- prefer clear, auditable changes over hidden magic
- keep setup and launch paths honest and runnable
- document any new subsystem entry points and configuration assumptions

## Basic validation

```bash
python3 -m compileall ARC_Console launch.py
python3 launch.py --check
```
