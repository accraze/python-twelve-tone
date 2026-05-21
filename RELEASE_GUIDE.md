# Release Guide for twelve-tone v0.5.0

## Summary of Changes Completed

The following updates have been made to prepare for the v0.5.0 release:

### 1. GitHub Actions Workflow Updated (`.github/workflows/publish-to-test-pypi.yml`)
- ✅ Updated from `ubuntu-18.04` to `ubuntu-latest`
- ✅ Updated Python from 3.7 to 3.12
- ✅ Added test matrix for Python 3.8-3.12
- ✅ Updated actions to latest versions (checkout@v4, setup-python@v5, gh-action-pypi-publish@release/v1)
- ✅ Added proper test execution step before publishing
- ✅ Workflow triggers on push to master and tags

### 2. Package Metadata Updated (`setup.py`)
- ✅ Updated Python version classifiers (removed 2.7, 3.3-3.5; added 3.8-3.12)
- ✅ Added `Programming Language :: Python :: 3 :: Only` classifier
- ✅ Added `Topic :: Multimedia :: Sound/Audio :: MIDI` classifier
- ✅ Added `long_description_content_type='text/x-rst'`

### 3. Package Built Successfully
- ✅ Wheel: `dist/twelve_tone-0.5.0-py2.py3-none-any.whl` (12KB)
- ✅ Source: `dist/twelve_tone-0.5.0.tar.gz` (27KB)
- ✅ Package validation: PASSED

## Next Steps to Complete Release

### Option 1: Manual Upload (Recommended for immediate release)

You'll need your PyPI API tokens. Get them from:
- PyPI: https://pypi.org/manage/account/token/
- TestPyPI: https://test.pypi.org/manage/account/token/

```bash
cd ~/src/python-twelve-tone

# Upload to TestPyPI first
python -m twine upload --repository testpypi dist/*

# Upload to PyPI
python -m twine upload dist/*
```

### Option 2: GitHub Actions (Automated)

The workflow is already configured but requires API tokens as GitHub Secrets:

1. Go to: https://github.com/accraze/python-twelve-tone/settings/secrets/actions
2. Add the following secrets:
   - `PYPI_API_TOKEN`: Your PyPI API token
   - `TEST_PYPI_API_TOKEN`: Your TestPyPI API token

3. Trigger the workflow by either:
   - Pushing a new tag: `git tag v0.5.0 && git push origin v0.5.0`
   - Manually from the Actions tab

### Option 3: Using GitHub CLI (if authenticated)

```bash
cd ~/src/python-twelve-tone

# Re-authenticate GitHub CLI
gh auth login

# Check workflow runs
gh workflow list

# Trigger workflow (if needed)
gh workflow run publish-to-test-pypi.yml
```

## Verification Steps

After publishing, verify:

1. **Check PyPI page**: https://pypi.org/project/twelve-tone/0.5.0/
2. **Test installation**: 
   ```bash
   pip install --upgrade twelve-tone
   twelve-tone --version
   ```
3. **Run tests**: 
   ```bash
   python -m pytest tests/ -v
   ```
4. **Check GitHub Actions**: https://github.com/accraze/python-twelve-tone/actions

## What's New in v0.5.0

### Major Changes
- **Removed numpy dependency** - Complete rewrite using pure Python lists (#33)
- **Replaced miditime with mido** - Updated MIDI generation to use actively maintained library (#31)
- **Added CLI subcommands** - New subcommands: `p`, `i`, `r`, `ri` for row forms (#32)
- **Multiple output formats** - Support for text, integer, rich table formats (#29, #30)
- **LilyPond output** - Added `--lilypond` flag for music notation export (#29)
- **Custom pitch input** - Support for custom tone rows via `--pitch` flag (#32)
- **Enhanced documentation** - Updated README with comprehensive examples

### Backward Compatibility
- Old CLI interface maintained via hidden `compose` command
- API remains compatible with existing code

## Files Modified

1. `.github/workflows/publish-to-test-pypi.yml` - Modernized workflow
2. `setup.py` - Updated classifiers and metadata
3. `RELEASE_GUIDE.md` - This file

## Current Status

- [x] Package built and validated
- [x] Tests passing locally (22 tests)
- [x] GitHub Actions workflow updated
- [x] Metadata corrected
- [ ] Uploaded to TestPyPI
- [ ] Uploaded to PyPI
- [ ] GitHub tag pushed
- [ ] GitHub Actions run completed

## Contact

For questions about the release process, refer to:
- PyPI documentation: https://pypi.org/help/#publishing
- GitHub Actions docs: https://docs.github.com/en/actions
