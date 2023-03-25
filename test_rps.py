from rps import is_valid_play, computer_play
from rps import determine_game_result, main


def test_game_asks_until_valid(capsys, monkeypatch):
    answer = {'num': 0}
    answers = ['xyz', 'abc', 'rock']
    
    def fake_input(prompt):
        print(prompt)
        answer['num'] += 1
        return answers[answer['num']-1]

    monkeypatch.setattr('builtins.input', fake_input)
    main()
    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[0].startswith('rock, paper or')
    assert lines[1].startswith('rock, paper or')
    assert lines[2].startswith('rock, paper or')
    assert not lines[3].startswith('rock, paper or')



def test_full_game(capsys, monkeypatch):
    def fake_input(prompt):
        print(prompt)
        return 'rock'
    monkeypatch.setattr('builtins.input', fake_input)
    main()
    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[0].strip() == 'rock, paper or scissors?'
    l1 = lines[1].strip()
    assert l1 in ['rock', 'paper', 'scissors']
    l2 = lines[2].strip()
    assert l2 in ['you win', 'you loose', 'it\'s a tie!']
    assert len(lines) == 3
    if l1 == 'rock':
        assert l2 == 'it\'s a tie!'
    elif l1 == 'paper':
        assert l2 == 'you loose'
    elif l1 == 'scissors':
        assert l2 == 'you win'


def test_paper_beats_rock():
    result = determine_game_result('paper', 'rock')
    assert result == 'human'


def test_rock_beats_scissors():
    result = determine_game_result('rock', 'scissors')
    assert result == 'human'


def test_rock_is_beaten_by_paper():
    result = determine_game_result('rock', 'paper')
    assert result == 'computer'


def test_tie():
    for play in ['rock', 'paper', 'scissors']:
        result = determine_game_result(play, play)
        assert result == 'tie'



def test_computer_play_is_valid():
    for _ in range(10000):
        assert is_valid_play(computer_play())


def test_computer_play_eventually_plays_it_all():
    played = []
    play = computer_play()
    played.append(play)
    counter = 1
    while len(played) < 3:
         play = computer_play()
         counter += 1
         if play not in played:
            played.append(play)
         assert counter < 100, "Too many plays"


def test_rokc_is_not_valid_play():
    assert is_valid_play('rokc') is False


def test_empty_str_is_not_valid_play():
    assert is_valid_play('') is False


def test_rock_valid_play_is_valid_play():
    assert is_valid_play('rock') is True


def test_paper_is_valid_play():
    assert is_valid_play('paper') is True


def test_scissors_is_valid_play():
    assert is_valid_play('scissors') is True

