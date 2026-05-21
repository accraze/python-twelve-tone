"""Tests for twelve_tone CLI."""
from click.testing import CliRunner

from twelve_tone.cli import main, generate, p, i, r, ri


def test_main():
    """Test the main CLI group."""
    runner = CliRunner()
    result = runner.invoke(main, [])
    assert result.exit_code == 0


def test_generate():
    """Test the generate command."""
    runner = CliRunner()
    result = runner.invoke(generate, [])
    assert result.exit_code == 0
    # Should output 12 pitch classes
    assert len(result.output.strip().split()) == 12


def test_generate_with_pitch():
    """Test generate with custom pitch input."""
    runner = CliRunner()
    result = runner.invoke(generate, ['--pitch', 'C E G B D F A C# F# G# A# D#'])
    assert result.exit_code == 0
    assert 'C' in result.output
    assert 'E' in result.output


def test_generate_integer_format():
    """Test generate with integer output format."""
    runner = CliRunner()
    result = runner.invoke(generate, ['--format', 'integer'])
    assert result.exit_code == 0
    # Should contain only numbers
    output_parts = result.output.strip().split()
    assert len(output_parts) == 12
    for part in output_parts:
        assert part.isdigit()


def test_prime_command():
    """Test the P (Prime) command."""
    runner = CliRunner()
    result = runner.invoke(p, [])
    assert result.exit_code == 0
    assert len(result.output.strip().split()) == 12


def test_inversion_command():
    """Test the I (Inversion) command."""
    runner = CliRunner()
    result = runner.invoke(i, [])
    assert result.exit_code == 0
    assert len(result.output.strip().split()) == 12


def test_retrograde_command():
    """Test the R (Retrograde) command."""
    runner = CliRunner()
    result = runner.invoke(r, [])
    assert result.exit_code == 0
    assert len(result.output.strip().split()) == 12


def test_retrograde_inversion_command():
    """Test the RI (Retrograde-Inversion) command."""
    runner = CliRunner()
    result = runner.invoke(ri, [])
    assert result.exit_code == 0
    assert len(result.output.strip().split()) == 12


def test_matrix_output():
    """Test full matrix output."""
    runner = CliRunner()
    result = runner.invoke(generate, ['--matrix'])
    assert result.exit_code == 0
    # Matrix should have 12 lines (one per row)
    lines = result.output.strip().split('\n')
    assert len(lines) == 12


def test_help():
    """Test that help is available."""
    runner = CliRunner()
    result = runner.invoke(main, ['--help'])
    assert result.exit_code == 0
    assert 'generate' in result.output
    assert 'P' in result.output
    assert 'I' in result.output
    assert 'R' in result.output
    assert 'RI' in result.output
