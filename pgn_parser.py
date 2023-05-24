import re

def pgnParser(pgn_string):
    pgn_moves = re.sub("\[.*\]\n|[0-9]\.\s|\s\s", '', pgn_string, flags=re.MULTILINE)
    pgn_moves = re.sub("\n", ' ', pgn_moves, flags=re.MULTILINE)
    print(pgn_moves)

if __name__ == "__main__":
    pgn = '''[Event "Live Chess"]
    [Site "Chess.com"]
    [Date "2023.05.22"]
    [Round "?"]
    [White "jacekszymanski"]
    [Black "ankit2419"]
    [Result "0-1"]
    [ECO "D10"]
    [WhiteElo "1174"]
    [BlackElo "1232"]
    [TimeControl "600"]
    [EndTime "10:52:34 PDT"]
    [Termination "ankit2419 won on time"]

    1. d4 d5 2. c4 c6 3. Nc3 Bf5 4. cxd5 cxd5 5. e3 e6 6. Bb5+ Nc6 7. Qa4 Ne7 8. Nf3
    a6 9. Bxc6+ bxc6 10. Ne5 Qc7 11. O-O f6 12. Nf3 Ng6 13. Re1 Bd6 14. g3 Bg4 15.
    Qd1 O-O 16. e4 e5 17. Kg2 exd4 18. Qxd4 Rae8 19. exd5 Bxf3+ 20. Kxf3 Rxe1 21.
    Ne4 cxd5 22. Qxd5+ Kh8 23. Nxd6 Ne5+ 24. Kg2 Rxc1 25. Rxc1 Qxc1 26. Qe6 Qc6+ 27.
    Kh3 Qd7 28. Qxd7 Nxd7 29. b4 Rb8 30. a3 Ne5 31. f4 Nc6 32. Nf7+ Kg8 33. Nd6 Nxb4
    34. axb4 Rxb4 35. Nc4 Rxc4 36. g4 a5 0-1
    '''
    pgnParser(pgn)