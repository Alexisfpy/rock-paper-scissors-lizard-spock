from RPS_game import RPSGame, GameAction, GameResult

def test_empate():
    game = RPSGame()
    # Spock vs Spock debe ser empate
    assert game.assess_game(GameAction.Spock, GameAction.Spock) == GameResult.Tie

def test_victoria_clasica():
    game = RPSGame()
    # Piedra rompe Tijeras -> Victoria
    assert game.assess_game(GameAction.Rock, GameAction.Scissors) == GameResult.Victory

def test_victoria_lizard_spock():
    game = RPSGame()
    # Lagarto envenena a Spock -> Victoria
    assert game.assess_game(GameAction.Lizard, GameAction.Spock) == GameResult.Victory

def test_derrota():
    game = RPSGame()
    # Piedra pierde contra Papel -> Derrota
    assert game.assess_game(GameAction.Rock, GameAction.Paper) == GameResult.Defeat

def test_derrota_spock():
    game = RPSGame()
    # Tijeras pierden contra Spock (Spock rompe tijeras) -> Derrota
    assert game.assess_game(GameAction.Scissors, GameAction.Spock) == GameResult.Defeat

