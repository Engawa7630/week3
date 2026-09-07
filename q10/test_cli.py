import subprocess
import sys

def test_blank_name_exits_with_2():
    result = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", "   "],
        capture_output=True,
        text=True
    )
    assert result.returncode == 2
