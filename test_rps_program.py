import subprocess

import pytest

@pytest.mark.parametrize('i', range(100))
def test_rps_program(i):
    cp = subprocess.run(
        ['python', 'rps.py'],
        text=True,
        capture_output=True,
        input='rock\n',
    )
    assert cp.returncode == 0
    assert cp.stderr == ''
    outputs = [
        'rock, paper or scissors? scissors\nyou win\n',
        'rock, paper or scissors? paper\nyou loose\n',
        'rock, paper or scissors? rock\nit\'s a tie!\n',
    ]
    assert cp.stdout in outputs
