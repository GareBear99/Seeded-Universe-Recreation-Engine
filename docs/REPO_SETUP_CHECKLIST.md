# Repo Setup Checklist

## GitHub settings to configure manually

- Set the About description to the recommended description from `docs/SEO_PROMOTION.md`
- Add the suggested topic tags
- Upload a social preview image if desired
- Enable Issues
- Enable Discussions if you want architectural discussions public
- Add the repository website only if you publish a stable demo page
- Create tagged releases for notable milestones

## Local validation

```bash
python3 -m compileall ARC_Console launch.py
python3 launch.py --check
```

## Release hygiene

- verify README links
- verify launcher opens the intended HTML entry points
- confirm ARC starts locally with installed dependencies
- confirm no stray local artifacts are bundled before release
