import re

class moves:
    board_annotations = []
def pgnParser(pgn_string):
    pgn_moves = re.sub("\[.*\]\n|[0-9][0-9]\.\s|\s\s", '', pgn_string, flags=re.MULTILINE) # REMOVES THE DETAILS OF THE PGN
    pgn_moves = re.sub("\n", ' ', pgn_moves, flags=re.MULTILINE) # REMOVES NEXT LINE CHAR
    pgn_moves = re.sub("\{\[[^\]]*\]\}", ' ', pgn_moves, flags=re.MULTILINE) # REMOVES THE STRINGS LIKE {[%clk 0:02:00]} WHICH PROBABLY MENTION THE TIME THE MOVE WAS PLAYED
    pgn_moves = re.sub("\d\.+", '', pgn_moves, flags=re.MULTILINE) # REMOVES THE MOVE NUMBER
    pgn_moves = re.sub("\s\d-\d\s*", ' ',  pgn_moves, flags=re.MULTILINE) # REMOVES THE OUTCOME OF THE GAME
    pgn_moves = re.sub(r"\s[0-9]\s", ' ',  pgn_moves, flags=re.MULTILINE) # REMOVES STRAY INTS IN THE STRING
    #print(pgn_moves)
    return pgn_moves

if __name__ == "__main__":
    pgn = '''[Event "Live Chess"]
[Site "Chess.com"]
[Date "2014.09.07"]
[Round "-"]
[White "betablokator"]
[Black "123lt"]
[Result "0-1"]
[CurrentPosition "4Q3/5pkp/4p1p1/8/4q3/7P/3r3K/6R1 w - -"]
[Timezone "UTC"]
[ECO "B21"]
[ECOUrl "https://www.chess.com/openings/Sicilian-Defense-McDonnell-Attack-2...d5-3.e5"]
[UTCDate "2014.09.07"]
[UTCTime "03:15:33"]
[WhiteElo "1266"]
[BlackElo "1469"]
[TimeControl "120+1"]
[Termination "123lt won by resignation"]
[StartTime "03:15:33"]
[EndDate "2014.09.07"]
[EndTime "03:18:59"]
[Link "https://www.chess.com/game/live/907776561"]

1. e4 {[%clk 0:02:00]} 1... c5 {[%clk 0:02:00]} 2. f4 {[%clk 0:01:58.9]} 2... d5 {[%clk 0:01:59.6]} 3. e5 {[%clk 0:01:56.8]} 3... Nh6 {[%clk 0:01:58.3]} 4. Nf3 {[%clk 0:01:57.7]} 4... Nf5 {[%clk 0:01:56.4]} 5. Be2 {[%clk 0:01:58.6]} 5... Nc6 {[%clk 0:01:56.4]} 6. O-O {[%clk 0:01:59.5]} 6... e6 {[%clk 0:01:56.9]} 7. d3 {[%clk 0:01:58.9]} 7... Be7 {[%clk 0:01:56.5]} 8. Nbd2 {[%clk 0:01:59.1]} 8... Nfd4 {[%clk 0:01:56.4]} 9. c3 {[%clk 0:01:57]} 9... Nf5 {[%clk 0:01:56.2]} 10. Qc2 {[%clk 0:01:52.3]} 10... Ne3 {[%clk 0:01:56]} 11. Qb1 {[%clk 0:01:50.8]} 11... Nxf1 {[%clk 0:01:56.1]} 12. Kxf1 {[%clk 0:01:50.5]} 12... O-O {[%clk 0:01:55]} 13. d4 {[%clk 0:01:51.2]} 13... cxd4 {[%clk 0:01:48.6]} 14. Nxd4 {[%clk 0:01:52.1]} 14... Nxd4 {[%clk 0:01:46.5]} 15. cxd4 {[%clk 0:01:53]} 15... Qb6 {[%clk 0:01:46.8]} 16. Nf3 {[%clk 0:01:51.8]} 16... Bd7 {[%clk 0:01:46.7]} 17. Be3 {[%clk 0:01:51.1]} 17... Bb5 {[%clk 0:01:46.8]} 18. Bxb5 {[%clk 0:01:48]} 18... Qxb5+ {[%clk 0:01:47]} 19. Kg1 {[%clk 0:01:48.9]} 19... Rac8 {[%clk 0:01:47.3]} 20. Ng5 {[%clk 0:01:48]} 20... g6 {[%clk 0:01:47]} 21. Qd1 {[%clk 0:01:43.2]} 21... Bxg5 {[%clk 0:01:46.7]} 22. fxg5 {[%clk 0:01:42.2]} 22... Qxb2 {[%clk 0:01:46.9]} 23. Rb1 {[%clk 0:01:40.2]} 23... Qxa2 {[%clk 0:01:47.2]} 24. Rxb7 {[%clk 0:01:38.9]} 24... Rc2 {[%clk 0:01:47.1]} 25. Qf1 {[%clk 0:01:37.2]} 25... Qa3 {[%clk 0:01:46.3]} 26. Bf4 {[%clk 0:01:35.7]} 26... Qc3 {[%clk 0:01:45.1]} 27. Rxa7 {[%clk 0:01:33]} 27... Qxd4+ {[%clk 0:01:44.1]} 28. Kh1 {[%clk 0:01:26.9]} 28... Rf2 {[%clk 0:01:38.8]} 29. Qe1 {[%clk 0:01:16.9]} 29... Qxf4 {[%clk 0:01:37.8]} 30. Ra1 {[%clk 0:01:14.6]} 30... d4 {[%clk 0:01:36.5]} 31. Qd1 {[%clk 0:01:07.8]} 31... d3 {[%clk 0:01:36.5]} 32. Qxd3 {[%clk 0:01:06.7]} 32... Qxg5 {[%clk 0:01:36.6]} 33. Rg1 {[%clk 0:01:04]} 33... Rd8 {[%clk 0:01:36.5]} 34. Qa3 {[%clk 0:01:00.4]} 34... Rdd2 {[%clk 0:01:35.4]} 35. Qa8+ {[%clk 0:00:57.2]} 35... Kg7 {[%clk 0:01:35.8]} 36. h3 {[%clk 0:00:56]} 36... Qxe5 {[%clk 0:01:34.1]} 37. Qe8 {[%clk 0:00:49.9]} 37... Rxg2 {[%clk 0:01:30.8]} 38. Rxg2 {[%clk 0:00:48]} 38... Rd1+ {[%clk 0:01:31.1]} 39. Rg1 {[%clk 0:00:46.9]} 39... Qe4+ {[%clk 0:01:31.3]} 40. Kh2 {[%clk 0:00:47]} 40... Rd2+ {[%clk 0:01:31.6]} 0-1 
    '''
    m = pgnParser(pgn)
    print(m)