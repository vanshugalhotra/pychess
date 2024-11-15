from pychess_engine.globals import Sq120ToSq64, setMask, clearMask
from pychess_engine.helper import FR2SQ
from pychess_engine.constants import Ranks, Files

bitTable = [
  63, 30, 3, 32, 25, 41, 22, 33, 15, 50, 42, 13, 11, 53, 19, 34, 61, 29, 2,
  51, 21, 43, 45, 10, 18, 47, 1, 54, 9, 57, 0, 35, 62, 31, 40, 4, 49, 5, 52,
  26, 60, 6, 23, 44, 46, 27, 56, 16, 7, 39, 48, 24, 59, 14, 12, 55, 38, 28,
  58, 20, 37, 17, 36, 8
  ]

def print_bit_board(bb):
    shiftMe = 1
    sq = 0
    sq64 = 0
    print()
    for rank in range(Ranks.R8, Ranks.R1 - 1, -1): #7-0
        for file in range(Files.A, Files.H+1): #0-7
            sq = FR2SQ(file, rank) # calculating the square for 120 bit
            sq64 = Sq120ToSq64[sq] # converting the square for 64 bit
            if((shiftMe << sq64) & bb):
                print("X", end=" ")
            else:
                print("-", end=" ")
        print()
        
def CountBits(b):
    r = 0
    while(b):
        b = b & b-1
        r += 1
    return r
        
def PopBit(bb): 
    b = bb ^ (bb - 1)
    fold = ((b & 0xffffffff) ^ (b >> 32))
    bb = bb & (bb- 1)
    return bitTable[((fold * 0x783a9b23)%4294967296) >> 26], bb # Modulo 2**32 to keep number in range

def SetBit(bb, sq):
    bb |= setMask[sq]
    return bb

def ClearBit(bb, sq):
    bb &= clearMask[sq]
    return bb
