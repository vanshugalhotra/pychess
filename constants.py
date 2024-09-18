from enum import Enum

class PIECE(Enum):
    EMPTY = 0
    wP = 1 # white pawn
    wN = 2 # white Knight
    wB = 3 # white bishop
    wR = 4
    wQ = 5
    wK = 6
    bP = 7
    bN = 8
    bB = 9
    bR = 10
    bQ = 11
    bK = 12
    
class FILE(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7
    NONE = 8
    
class RANK(Enum):
    R1 = 0
    R2 = 1
    R3 = 2
    R4 = 3
    R5 = 4
    R6 = 5
    R7 = 6
    R8 = 7
    RNONE = 8
    
class COLORS(Enum):
    WHITE = 0
    BLACK = 1
    BOTH = 2
    

class SQUARES(Enum):
    
    A1 = 21
    A2 = 31
    A3 = 41
    A4 = 51
    A5 = 61
    A6 = 71
    A7 = 81
    A8 = 91
    
    B1 = 22
    B2 = 32
    B3 = 42
    B4 = 52
    B5 = 62
    B6 = 72
    B7 = 82
    B8 = 92
    
    C1 = 23
    C2 = 33
    C3 = 43
    C4 = 53
    C5 = 63
    C6 = 73
    C7 = 83
    C8 = 93
    
    D1 = 24
    D2 = 34
    D3 = 44
    D4 = 54
    D5 = 64
    D6 = 74
    D7 = 84
    D8 = 94
    
    E1 = 25
    E2 = 35
    E3 = 45
    E4 = 55
    E5 = 65
    E6 = 75
    E7 = 85
    E8 = 95
    
    F1 = 26
    F2 = 36
    F3 = 46
    F4 = 56
    F5 = 66
    F6 = 76
    F7 = 86
    F8 = 96
    
    G1 = 27
    G2 = 37
    G3 = 47
    G4 = 57
    G5 = 67
    G6 = 77
    G7 = 87
    G8 = 97
    
    H1 = 28
    H2 = 38
    H3 = 48
    H4 = 58
    H5 = 68
    H6 = 78
    H7 = 88
    H8 = 98
    
    NO_SQ = 99