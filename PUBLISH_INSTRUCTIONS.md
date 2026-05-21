# Complete PyPI Release Instructions for twelve-tone v0.5.0

## Status: Ready to Publish ✅

All preparation work is complete. The package is built and validated:
- ✅ Wheel: `dist/twelve_tone-0.5.0-py2.py3-none-any.whl` (12KB)
- ✅ Source: `dist/twelve_tone-0.5.0.tar.gz` (27KB)
- ✅ Tests: 22/22 passing
- ✅ GitHub Actions workflow: Updated and ready

## Option A: GitHub Actions (Recommended)

### Step 1: Get Your PyPI API Tokens

**For PyPI (Production):**
1. Go to https://pypi.org/manage/account/token/
2. Click "Add API token"
3. Name it: `github-actions-python-twelve-tone`
4. Scope: Select "Entire account"
5. Copy the token (starts with `pypi-`)

**For TestPyPI (Optional testing):**
1. Go to https://test.pypi.org/manage/account/token/
2. Click "Add API token"
3. Name it: `github-actions-python-twelve-tone`
4. Copy the token

### Step 2: Add GitHub Secrets

1. Go to: https://github.com/accraze/python-twelve-tone/settings/secrets/actions
2. Click "New repository secret"
3. Add these secrets:

   **Secret 1:**
   - Name: `PYPI_API_TOKEN`
   - Value: (paste your PyPI token from Step 1)

   **Secret 2 (optional, for TestPyPI):**
   - Name: `TEST_PYPI_API_TOKEN`
   - Value: (paste your TestPyPI token)

### Step 3: Trigger the Release

**Method 1: Push a tag (creates release)**
```bash
cd ~/src/python-twelve-tone
git push origin v0.5.0
```

**Method 2: Manual trigger from GitHub UI**
1. Go to: https://github.com/accraze/python-twelve-tone/actions
2. Click "Publish Python 🐍 distributions 📦 to PyPI and TestPyPI" workflow
3. Click "Run workflow"
4. Select branch: `master`
5. Click "Run workflow"

### Step 4: Monitor the Release

1. Watch the workflow run: https://github.com/accraze/python-twelve-tone/actions
2. The workflow will:
   - Run tests on Python 3.8-3.12 ✅
   - Build the package ✅
   - Upload to TestPyPI (if token provided)
   - Upload to PyPI (if tag pushed)

### Step 5: Verify the Release

After the workflow completes:

1. **Check PyPI**: https://pypi.org/project/twelve-tone/0.5.0/
2. **Test installation**:
   ```bash
   pip install --upgrade twelve-tone
   twelve-tone --version
   twelve-tone generate
   ```
3. **Check GitHub Actions**: Verify all tests passed

---

## Option B: Manual Upload (Alternative)

If you prefer to upload manually:

```bash
cd ~/src/python-twelve-tone

# Install twine if needed
pip install twine

# Upload to PyPI
python -m twine upload dist/*

# Or upload to TestPyPI first
python -m twine upload --repository testpypi dist/*
```

You'll be prompted for your PyPI username (`__token__`) and password (your API token starting with `pypi-`).

---

## What's Included in v0.5.0

### Major Features
- ✅ Pure Python implementation (no numpy)
- ✅ Modern MIDI library (mido instead of miditime)
- ✅ CLI subcommands (p, i, r, ri)
- ✅ Multiple output formats (text, integer, rich, LilyPond)
- ✅ Custom pitch input support
- ✅ Comprehensive documentation

### Changes Since Last Release (0.4.2)
- Removed numpy dependency (#33)
- Replaced miditime with mido (#31)
- Added CLI subcommands (#32)
- Multiple output formats (#29, #30)
- LilyPond export (#29)
- Custom pitch input (#32)

---

## Troubleshooting

### GitHub Actions Fails
- Check the workflow run logs for specific errors
- Verify secrets are set correctly (no extra spaces)
- Ensure the tag v0.5.0 exists: `git tag -l | grep 0.5.0`

### PyPI Upload Fails
- Token must start with `pypi-`
- Token must have "Entire account" scope
- Check PyPI for any existing 0.5.0 release

### Tests Fail
- Run locally: `python -m pytest tests/ -v`
- Check Python version compatibility (3.8+)

---

## Support

- PyPI Help: https://pypi.org/help/#publishing
- GitHub Actions Docs: https://docs.github.com/en/actions
- Package Issues: https://github.com/accraze/python-twelve-tone/issues
