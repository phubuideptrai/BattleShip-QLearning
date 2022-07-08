# BattleShip-QLearning

    python3 src/main.py
        Play 10 training games and 1 test game with the QLearning agent.

    python3 src/main.py -g 50 -t 100 -a QLearning -s -S
        Play 100 training games and 50 test games with the QLearning agent vs. a do-nothing agent (NoOp Agent).  Output per game stats, and cumulative all-game stats.

    python3 src/main.py -g 50 -t 100 -a QLearning -r ClassicStationary
        Train QLearning agent with 100 games, then play 50 test games using the ClassicStationary rules.

    python3 src/main.py -g 10 -t 0 -a HuntAndTarget Human Random Random
        Play 10 test games with 1 HuntAndTarget, 1 Human, and 2 Random agents competing.

    python3 src/main.py -g 1 -t 0 -a QLearning Human -n PB_QLearning PB_Human
        Play 1 test game with a QLearning agent (named PB_QLearning) vs. a Human agent (named PB_Human).

    python3 src/main.py -g 1 -t 1 Random -r Classic -R Classic -c
        Play 1 training and 1 test game with the Random agent.  Training using Classic rules, play using Classic rules.  Use the same start state for all games.

    python3 test/TestRunner.py
        Run the unit tests.