Changelog
=========

0.5.0 (2026-05-20)
-----------------------------------------

### Major Changes

* **Removed numpy dependency** - Complete rewrite of matrix implementation using pure Python lists (#33)
* **Replaced miditime with mido** - Updated MIDI generation to use actively maintained mido library (#31)
* **Added CLI subcommands** - New subcommands for row forms: p, i, r, ri (#32)
* **Multiple output formats** - Support for text, integer, and rich table formats (#29, #30)
* **LilyPond output** - Added --lilypond flag for music notation export (#29)
* **Custom pitch input** - Support for custom tone rows via --pitch flag (#32)
* **Enhanced documentation** - Updated README with comprehensive examples

### Backward Compatibility

* Old CLI interface maintained via hidden `compose` command
* API remains compatible with existing code

0.4.2 (2021-03-11)
-----------------------------------------

### 0.4.1 (2021-3-11)

* requirements: added missing dependency click - (#22) - @jgarte

0.4.1 (2019-12-31)
-----------------------------------------

### 0.4.1 (2019-12-31)

* composer: matrix should only hold values of type 'int' (#20)

0.4.0 (2018-7-08)
-----------------------------------------

* composer: added/fixed column tonerow support

0.3.0 (2018-7-04)
-----------------------------------------

* cli: added random melody generator command

0.2.1 (2016-8-27)
-----------------------------------------

* build: added `miditime` to setup install requirements

0.2.0 (2016-8-27)
-----------------------------------------

* composer: Added save to MIDI capability

0.1.0 (2016-8-20)
-----------------------------------------

* First release on PyPI.
