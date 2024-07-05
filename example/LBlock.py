# this is LBock cipher differential cryptanalysis example
KEY_SIZE = 80
SUBKEY_SIZE = 32
WORD_SIZE = 4
marker = 0
add_counter = 0

S0_T = [
    (2, 1, 1, 1, -3, 0, 1, 2, 0),
    (-1, 2, -2, -1, 0, 0, -2, -1, 5),
    (0, 1, 0, 0, 1, -1, 1, 0, 0),
    (-1, -1, 1, -3, 3, -1, -2, 2, 5),
    (3, -1, -1, -1, 0, 3, 2, 1, 0),
    (-1, 1, 2, 0, -1, -1, 2, -2, 3),
    (0, -1, 0, 1, -1, 0, -1, 1, 2),
    (0, -1, 0, 0, 1, 1, 1, 0, 0),
    (-1, -1, -1, 0, -1, -1, 0, -1, 5),
    (1, 2, -2, 1, 0, 0, 1, 2, 0),
    (1, 2, 3, -2, 1, 0, -1, 3, 0),
    (-1, 0, 0, 0, 1, 0, 1, 1, 0),
    (1, 1, -2, -2, 0, -1, -1, -2, 6),
    (-1, -1, 1, 0, -1, 1, -1, -1, 4),
    (0, -1, -1, 1, 1, 1, 0, -1, 2),
    (-1, 0, 1, 0, 1, 1, 1, 0, 0),
    (1, 0, 1, 1, 0, -1, -1, -1, 2),
    (1, -2, 1, -1, 2, 3, 1, 1, 0),
    (-1, 1, 0, 0, -1, 1, 1, -1, 2),
    (2, -1, -1, 0, -1, 1, 1, 1, 1),
    (2, 3, 1, 1, 0, -3, 1, 1, 0),
    (1, -1, -1, 0, 1, -1, -1, 1, 3),
    (3, 1, 2, 1, -3, -1, 1, 3, 0),
    (2, -1, -1, 1, -2, 1, 0, 1, 2),
    (1, -1, 1, -1, 0, 1, 0, -1, 2),
    (1, 1, 2, 2, 0, 1, 1, -2, 0),
    (-1, -1, -1, -2, 2, 1, 0, 1, 3),
    (0, -1, 1, 1, 1, -1, -1, -1, 3),
]
S1_T = [
    (2, 1, 1, 1, -3, 0, 2, 1, 0),
    (-1, 2, -2, -1, 0, 0, -1, -2, 5),
    (0, 1, 0, 0, 1, -1, 0, 1, 0),
    (-1, -1, 1, -3, 3, -1, 2, -2, 5),
    (3, -1, -1, -1, 0, 3, 1, 2, 0),
    (-1, 4, 5, 3, -1, -1, -2, 5, 0),
    (0, -1, 0, 1, -1, 0, 1, -1, 2),
    (0, -1, 0, 0, 1, 1, 0, 1, 0),
    (1, 2, -2, 1, 0, 0, 2, 1, 0),
    (-1, -1, -1, 0, -1, -1, -1, 0, 5),
    (0, 1, 2, -2, 1, 0, 2, -1, 1),
    (-1, 0, 0, 0, 1, 0, 1, 1, 0),
    (1, 1, -2, -2, 0, -1, -2, -1, 6),
    (2, 0, 1, 1, -2, -1, 1, -1, 2),
    (-1, -1, 1, 0, -1, 1, -1, -1, 4),
    (-1, 1, -1, 0, -1, 1, -1, 0, 3),
    (1, -1, 1, -1, 0, 1, -1, 0, 2),
    (-1, -1, -1, 0, 1, 1, -1, 0, 3),
    (0, -1, 1, 1, 1, -1, -1, -1, 3),
    (1, -1, -1, 1, 0, 1, -1, 0, 2),
    (2, 3, 1, 1, 0, -3, 1, 1, 0),
    (2, -1, 2, 3, -1, 2, 3, -1, 0),
    (-1, 1, 1, -1, 2, 0, 1, 1, 0),
    (-1, -1, 0, 0, -1, -1, -1, 1, 4),
    (1, -1, 0, 0, 0, 1, 0, 1, 0),
    (3, -1, -1, 0, -1, 2, 2, 2, 0),
    (1, 0, -1, 1, 0, -1, 1, -1, 2),
]
S2_T = [
    (2, 1, 1, 1, 1, -3, 2, 0, 0),
    (-1, 2, -2, -1, -2, 0, -1, 0, 5),
    (0, 1, 0, 0, 1, 1, 0, -1, 0),
    (-1, -1, 1, -3, -2, 3, 2, -1, 5),
    (3, -1, -1, -1, 2, 0, 1, 3, 0),
    (-1, 4, 5, 3, 5, -1, -2, -1, 0),
    (0, -1, 0, 1, -1, -1, 1, 0, 2),
    (0, -1, 0, 0, 1, 1, 0, 1, 0),
    (-1, -1, -1, 0, 0, -1, -1, -1, 5),
    (1, 2, -2, 1, 1, 0, 2, 0, 0),
    (1, -2, 1, -2, 1, 3, 2, 4, 0),
    (1, 1, -2, -2, -1, 0, -2, -1, 6),
    (-1, 0, 0, 0, 1, 1, 1, 0, 0),
    (2, 0, 1, 1, -1, -2, 1, -1, 2),
    (0, -1, 1, 1, -1, 1, -1, -1, 3),
    (0, 1, 1, -1, -1, 0, 1, 0, 1),
    (-1, -1, -1, 0, 0, 1, -1, 1, 3),
    (0, -1, 1, -1, -1, -1, -1, 1, 4),
    (1, -1, -1, 1, 0, 0, -1, 1, 2),
    (-1, 1, 0, 0, 1, -1, -1, 1, 2),
    (3, 2, -1, 3, -1, 0, 3, -1, 0),
    (1, 2, 1, 1, 1, 0, 0, -2, 0),
    (-1, 2, 1, -2, 1, 3, 2, 0, 0),
    (-1, 1, 2, 0, 2, -1, -2, -1, 3),
    (3, 1, 2, 2, 1, -4, 2, 1, 0),
    (-1, -1, 1, 1, -1, -1, 0, 1, 3),
    (3, -1, -1, 0, 2, -1, 2, 2, 0),
]
S3_T = [
    (2, 1, 1, 1, 0, 1, -3, 2, 0),
    (-1, 2, -2, -1, 0, -2, 0, -1, 5),
    (0, 1, 0, 0, -1, 1, 1, 0, 0),
    (-1, -1, 1, -3, -1, -2, 3, 2, 5),
    (3, -1, -1, -1, 3, 2, 0, 1, 0),
    (-1, 1, 2, 0, -1, 2, -1, -2, 3),
    (0, -1, 0, 1, 0, -1, -1, 1, 2),
    (0, -1, 0, 0, 1, 1, 1, 0, 0),
    (-1, -1, -1, 0, -1, 0, -1, -1, 5),
    (1, 2, -2, 1, 0, 1, 0, 2, 0),
    (1, 2, 2, -1, 0, -1, 0, 2, 0),
    (1, 1, -2, -2, -1, -1, 0, -2, 6),
    (-1, 0, 0, 0, 0, 1, 1, 1, 0),
    (1, 0, 1, 1, -1, -1, 0, -1, 2),
    (1, -1, -1, 1, 1, 0, 0, -1, 2),
    (1, -1, 1, -1, 2, 0, 2, 1, 0),
    (-1, 0, 1, 0, 1, 1, 1, 0, 0),
    (-1, 0, -1, 0, 1, -1, 1, -1, 3),
    (-1, 1, -1, 0, 1, 0, -1, -1, 3),
    (0, -1, 1, -1, 1, -1, -1, -1, 4),
    (3, 2, -1, 3, -1, -1, 0, 3, 0),
    (1, 2, -1, 1, -1, 1, 0, 1, 0),
    (3, 1, 2, 0, -1, 1, -2, 2, 0),
    (-1, -1, 1, 1, 1, -1, -1, 0, 3),
    (1, 1, 2, 2, 1, 1, 0, -2, 0),
    (2, -1, -1, 0, 1, 1, -1, 1, 1),
    (0, -1, 1, 1, -1, -1, 1, -1, 3),
]
S4_T = [
    (2, 1, 1, 1, 1, -3, 0, 2, 0),
    (-1, 2, -2, -1, -2, 0, 0, -1, 5),
    (0, 1, 0, 0, 1, 1, -1, 0, 0),
    (-1, -1, 1, -3, -2, 3, -1, 2, 5),
    (3, -1, -1, -1, 2, 0, 3, 1, 0),
    (-1, 4, 5, 3, 5, -1, -1, -2, 0),
    (0, -1, 0, 1, -1, -1, 0, 1, 2),
    (0, -1, 0, 0, 1, 1, 1, 0, 0),
    (-1, -1, -1, 0, 0, -1, -1, -1, 5),
    (1, 2, -2, 1, 1, 0, 0, 2, 0),
    (1, -1, 1, -1, -1, 2, 1, 1, 1),
    (1, 1, -2, -2, -1, 0, -1, -2, 6),
    (-1, 0, 0, 0, 1, 1, 0, 1, 0),
    (-1, -1, -1, 0, 0, 1, 1, -1, 3),
    (1, 0, 1, 1, -1, 0, -1, -1, 2),
    (1, -1, -1, 1, 0, 0, 1, -1, 2),
    (-1, 1, 0, 0, 1, -1, 1, -1, 2),
    (2, 2, 3, -1, -1, 0, -1, 3, 0),
    (0, -1, 1, -1, -1, -1, 1, -1, 4),
    (3, -1, -1, 0, 2, -1, 2, 2, 0),
    (-1, 1, 1, -1, 1, 2, 0, 1, 0),
    (1, -1, 0, 0, 1, 0, 1, 0, 0),
    (-1, -1, 1, 0, -1, 1, -1, -1, 4),
    (2, 3, 1, 1, 1, 0, -3, 1, 0),
    (1, 0, -1, 1, -1, 0, -1, 1, 2),
    (0, 1, 2, -2, -1, 1, 0, 2, 1),
    (-1, -1, 1, 1, -1, -1, 1, 0, 3),
    (-1, 0, 1, 0, 1, -1, -1, -1, 3),
]
S5_T = [
    (2, 1, 1, 1, -3, 1, 0, 2, 0),
    (-1, 2, -2, -1, 0, -2, 0, -1, 5),
    (0, 1, 0, 0, 1, 1, -1, 0, 0),
    (-1, -1, 1, -3, 3, -2, -1, 2, 5),
    (3, -1, -1, -1, 0, 2, 3, 1, 0),
    (-1, 1, 2, 0, -1, 2, -1, -2, 3),
    (0, -1, 0, 1, -1, -1, 0, 1, 2),
    (0, -1, 0, 0, 1, 1, 1, 0, 0),
    (-1, -1, -1, 0, -1, 0, -1, -1, 5),
    (1, 2, -2, 1, 0, 1, 0, 2, 0),
    (1, -1, 1, -1, 2, -1, 1, 1, 1),
    (-1, 0, 0, 0, 1, 1, 0, 1, 0),
    (1, 1, -2, -2, 0, -1, -1, -2, 6),
    (0, 1, 1, -1, 0, -1, 0, 1, 1),
    (-1, 0, 1, 0, 1, 1, 1, 0, 0),
    (1, 0, 1, 1, 0, -1, -1, -1, 2),
    (1, -1, -1, 1, 0, 0, 1, -1, 2),
    (-1, 1, -1, 0, -1, 0, 1, -1, 3),
    (0, -1, 1, -1, -1, -1, 1, -1, 4),
    (-1, -1, -1, 0, 1, 0, 1, -1, 3),
    (2, -1, -1, 0, -1, 1, 1, 1, 1),
    (1, -1, -1, 0, 1, -1, -1, 1, 3),
    (1, 1, 0, 0, 0, 1, -1, 0, 0),
    (5, 2, 4, 1, -4, 1, -2, 4, 0),
    (1, 1, 2, 2, 0, 1, 1, -2, 0),
    (-1, -1, 1, 1, -1, -1, 1, 0, 3),
    (0, -1, 1, 1, 1, -1, -1, -1, 3),
]
S6_T = [
    (2, 1, 1, 1, -3, 0, 2, 1, 0),
    (-1, 2, -2, -1, 0, 0, -1, -2, 5),
    (0, 1, 0, 0, 1, -1, 0, 1, 0),
    (-1, -1, 1, -3, 3, -1, 2, -2, 5),
    (3, -1, -1, -1, 0, 3, 1, 2, 0),
    (-1, 4, 5, 3, -1, -1, -2, 5, 0),
    (0, -1, 0, 1, -1, 0, 1, -1, 2),
    (0, -1, 0, 0, 1, 1, 0, 1, 0),
    (1, 2, -2, 1, 0, 0, 2, 1, 0),
    (-1, -1, -1, 0, -1, -1, -1, 0, 5),
    (0, 1, 2, -2, 1, 0, 2, -1, 1),
    (-1, 0, 0, 0, 1, 0, 1, 1, 0),
    (1, 1, -2, -2, 0, -1, -2, -1, 6),
    (2, 0, 1, 1, -2, -1, 1, -1, 2),
    (-1, -1, 1, 0, -1, 1, -1, -1, 4),
    (-1, 1, -1, 0, -1, 1, -1, 0, 3),
    (1, -1, 1, -1, 0, 1, -1, 0, 2),
    (-1, -1, -1, 0, 1, 1, -1, 0, 3),
    (0, -1, 1, 1, 1, -1, -1, -1, 3),
    (1, -1, -1, 1, 0, 1, -1, 0, 2),
    (2, 3, 1, 1, 0, -3, 1, 1, 0),
    (2, -1, 2, 3, -1, 2, 3, -1, 0),
    (-1, 1, 1, -1, 2, 0, 1, 1, 0),
    (-1, -1, 0, 0, -1, -1, -1, 1, 4),
    (1, -1, 0, 0, 0, 1, 0, 1, 0),
    (3, -1, -1, 0, -1, 2, 2, 2, 0),
    (1, 0, -1, 1, 0, -1, 1, -1, 2),
]
S7_T = [
    (2, 1, 1, 1, -3, 0, 2, 1, 0),
    (-1, 2, -2, -1, 0, 0, -1, -2, 5),
    (0, 1, 0, 0, 1, -1, 0, 1, 0),
    (-1, -1, 1, -3, 3, -1, 2, -2, 5),
    (3, -1, -1, -1, 0, 3, 1, 2, 0),
    (-1, 4, 5, 3, -1, -1, -2, 5, 0),
    (0, -1, 0, 1, -1, 0, 1, -1, 2),
    (0, -1, 0, 0, 1, 1, 0, 1, 0),
    (1, 2, -2, 1, 0, 0, 2, 1, 0),
    (-1, -1, -1, 0, -1, -1, -1, 0, 5),
    (0, 1, 2, -2, 1, 0, 2, -1, 1),
    (-1, 0, 0, 0, 1, 0, 1, 1, 0),
    (1, 1, -2, -2, 0, -1, -2, -1, 6),
    (2, 0, 1, 1, -2, -1, 1, -1, 2),
    (-1, -1, 1, 0, -1, 1, -1, -1, 4),
    (-1, 1, -1, 0, -1, 1, -1, 0, 3),
    (1, -1, 1, -1, 0, 1, -1, 0, 2),
    (-1, -1, -1, 0, 1, 1, -1, 0, 3),
    (0, -1, 1, 1, 1, -1, -1, -1, 3),
    (1, -1, -1, 1, 0, 1, -1, 0, 2),
    (2, 3, 1, 1, 0, -3, 1, 1, 0),
    (2, -1, 2, 3, -1, 2, 3, -1, 0),
    (-1, 1, 1, -1, 2, 0, 1, 1, 0),
    (-1, -1, 0, 0, -1, -1, -1, 1, 4),
    (1, -1, 0, 0, 0, 1, 0, 1, 0),
    (3, -1, -1, 0, -1, 2, 2, 2, 0),
    (1, 0, -1, 1, 0, -1, 1, -1, 2),
]
S8_T = [
    (2, 1, 1, 1, 0, -3, 2, 1, 0),
    (-1, 2, -2, -1, 0, 0, -1, -2, 5),
    (0, 1, 0, 0, -1, 1, 0, 1, 0),
    (-1, -1, 1, -3, -1, 3, 2, -2, 5),
    (3, -1, -1, -1, 3, 0, 1, 2, 0),
    (-1, 4, 5, 3, -1, -1, -2, 5, 0),
    (0, -1, 0, 1, 0, -1, 1, -1, 2),
    (0, -1, 0, 0, 1, 1, 0, 1, 0),
    (1, 2, -2, 1, 0, 0, 2, 1, 0),
    (-1, -1, -1, 0, -1, -1, -1, 0, 5),
    (1, 1, 2, -1, -1, 0, 2, -1, 1),
    (1, 1, -2, -2, -1, 0, -2, -1, 6),
    (-1, 0, 0, 0, 0, 1, 1, 1, 0),
    (3, 2, 3, 3, -1, 0, -1, -1, 0),
    (1, -1, -1, 1, 1, 0, -1, 0, 2),
    (1, -1, 1, -1, 1, 2, 1, -1, 1),
    (-1, -1, -1, 0, 1, 1, -1, 0, 3),
    (-1, 1, 0, 0, 1, -1, -1, 1, 2),
    (0, -1, 1, -1, 1, -1, -1, -1, 4),
    (-1, 2, 1, -2, 0, 3, 2, 1, 0),
    (3, 2, -1, 3, -1, 0, 3, -1, 0),
    (-1, -1, 0, 0, -1, -1, -1, 1, 4),
    (-1, -1, 1, 0, -1, 1, -1, -1, 4),
    (2, 3, 1, 1, -3, 0, 1, 1, 0),
    (3, 1, 2, 2, 1, -4, 2, 1, 0),
    (-1, -1, 1, 1, 1, -1, 0, -1, 3),
    (-1, 1, 0, -1, 0, 0, 1, -1, 2),
    (3, -1, -1, 0, 2, -1, 2, 2, 0),
]
S9_T = [
    (2, 1, 1, 1, 1, 2, 0, -3, 0),
    (-1, 2, -2, -1, -2, -1, 0, 0, 5),
    (0, 1, 0, 0, 1, 0, -1, 1, 0),
    (-1, -1, 1, -3, -2, 2, -1, 3, 5),
    (3, -1, -1, -1, 2, 1, 3, 0, 0),
    (-1, 4, 5, 3, 5, -2, -1, -1, 0),
    (0, -1, 0, 1, -1, 1, 0, -1, 2),
    (0, -1, 0, 0, 1, 0, 1, 1, 0),
    (-1, -1, -1, 0, 0, -1, -1, -1, 5),
    (1, 2, -2, 1, 1, 2, 0, 0, 0),
    (1, -1, 1, -1, -1, 1, 1, 2, 1),
    (1, 1, -2, -2, -1, -2, -1, 0, 6),
    (-1, 0, 0, 0, 1, 1, 0, 1, 0),
    (-1, -1, -1, 0, 0, -1, 1, 1, 3),
    (-1, 1, 0, 0, 1, -1, 1, -1, 2),
    (1, -1, -1, 1, 0, -1, 1, 0, 2),
    (-1, 1, 0, -1, -1, 1, 0, 0, 2),
    (6, 2, 3, 3, -1, 3, -1, -4, 0),
    (0, -1, 1, 1, -1, -1, -1, 1, 3),
    (0, -1, 1, -1, -1, -1, 1, -1, 4),
    (1, -1, 0, 0, 1, 0, 1, 0, 0),
    (2, 3, 1, 1, 1, 1, -3, 0, 0),
    (1, 0, -1, 1, -1, 1, -1, 0, 2),
    (3, -1, -1, -1, 2, 1, 2, -1, 1),
    (-1, 0, 1, -1, 1, 1, 1, 2, 0),
    (-1, 1, 2, 0, 2, -2, -1, -1, 3),
    (-1, -1, 1, 1, -1, 0, 1, -1, 3),
]


def sboxSpecificSubjection(inX, outY, ineqs):
    assert len(inX) == len(outY) and len(inX) == 4
    global marker
    eqn = []
    eqn.append(
        " + ".join([inX[t] for t in range(0, WORD_SIZE)])
        + " - y"
        + str(marker)
        + " >= 0"
    )
    for t in range(0, WORD_SIZE):
        eqn.append(inX[t] + " - " + "y" + str(marker) + " <= 0")

    marker = marker + 1
    temp1 = " + ".join(["4 " + inX[i] for i in range(0, 4)])
    temp2 = " - ".join([outY[i] for i in range(0, 4)])
    eqn.append(temp1 + " - " + temp2 + " >= 0")

    temp1 = " + ".join(["4 " + outY[i] for i in range(0, 4)])
    temp2 = " - ".join([inX[i] for i in range(0, 4)])
    eqn.append(temp1 + " - " + temp2 + " >= 0")
    T = ineqs
    for t in T:
        eqn.append(
            (
                str(t[0])
                + " "
                + inX[0]
                + " + "
                + str(t[1])
                + " "
                + inX[1]
                + " + "
                + str(t[2])
                + " "
                + inX[2]
                + " + "
                + str(t[3])
                + " "
                + inX[3]
                + " + "
                + str(t[4])
                + " "
                + outY[0]
                + " + "
                + str(t[5])
                + " "
                + outY[1]
                + " + "
                + str(t[6])
                + " "
                + outY[2]
                + " + "
                + str(t[7])
                + " "
                + outY[3]
                + " >= "
                + str(-t[8])
            ).replace("+ -", "- ")
        )
    return eqn


def getKeyStateAtRound(r):
    keycounter = 0
    if r == 1:
        return ["k" + str(i) for i in range(0, KEY_SIZE)]
    else:
        tempState = getKeyStateAtRound(r - 1)
        newState = ["" for i in range(0, KEY_SIZE)]
        for i in range(0, KEY_SIZE):
            newState[i] = tempState[(i + 29) % KEY_SIZE]
        assert len(newState) == KEY_SIZE
        if r >= 2:
            newState[0] = "vInSbox" + str((r - 2) * WORD_SIZE * 2 + 0)
            newState[1] = "vInSbox" + str((r - 2) * WORD_SIZE * 2 + 1)
            newState[2] = "vInSbox" + str((r - 2) * WORD_SIZE * 2 + 2)
            newState[3] = "vInSbox" + str((r - 2) * WORD_SIZE * 2 + 3)
            newState[4] = "vInSbox" + str((r - 2) * WORD_SIZE * 2 + 4)
            newState[5] = "vInSbox" + str((r - 2) * WORD_SIZE * 2 + 5)
            newState[6] = "vInSbox" + str((r - 2) * WORD_SIZE * 2 + 6)
            newState[7] = "vInSbox" + str((r - 2) * WORD_SIZE * 2 + 7)
        return newState


def keySelfSubjectionAtRound(r):
    global marker
    upKey = getKeyStateAtRound(r)
    downKey = getKeyStateAtRound(r + 1)
    eqn = []
    InBits = [upKey[i] for i in range(29, 37)]
    OutBits = [downKey[i] for i in range(0, 8)]
    in_S9 = InBits[0:4]
    in_S8 = InBits[4:8]
    out_S9 = OutBits[0:4]
    out_S8 = OutBits[4:8]
    eqn = eqn + sboxSpecificSubjection(in_S8, out_S8, S8_T)
    eqn = eqn + sboxSpecificSubjection(in_S9, out_S9, S9_T)
    return eqn


def keyScheduleSubjection(totalRound):
    eqn = []
    for i in range(1, totalRound + 1):
        eqn = eqn + keySelfSubjectionAtRound(i)
    return eqn


def extractSubKeyAtRound(r):
    tempState = getKeyStateAtRound(r)
    newState = [tempState[i] for i in range(0, 32)]
    assert len(newState) == SUBKEY_SIZE
    return newState


SubKeys = [None for i in range(0, 33)]
for j in range(1, 33):
    SubKeys[j] = extractSubKeyAtRound(j)


def xorAdditionSubjection(A, B, C):
    assert len(A) == SUBKEY_SIZE and len(B) == SUBKEY_SIZE and len(C) == SUBKEY_SIZE
    global add_counter
    eqn = []
    for j in range(0, len(A)):
        eqn.append(
            " + ".join([A[j], B[j], C[j]]) + " - 2 a" + str(add_counter) + " >= 0"
        )
        eqn.append("a" + str(add_counter) + " - " + A[j] + " >= 0")
        eqn.append("a" + str(add_counter) + " - " + B[j] + " >= 0")
        eqn.append("a" + str(add_counter) + " - " + C[j] + " >= 0")
        eqn.append(" + ".join([A[j], B[j], C[j]]) + " <= 2")
        add_counter = add_counter + 1
    return eqn


def F_Subjection(inV, sK, middV, outV):
    assert (
        len(inV) == SUBKEY_SIZE
        and len(sK) == SUBKEY_SIZE
        and len(middV) == SUBKEY_SIZE
        and len(outV) == SUBKEY_SIZE
    )
    eqn = []
    eqn = eqn + xorAdditionSubjection(inV, sK, middV)
    eqn = eqn + sboxSpecificSubjection(middV[0:4], outV[8:12], S7_T)
    eqn = eqn + sboxSpecificSubjection(middV[4:8], outV[0:4], S6_T)
    eqn = eqn + sboxSpecificSubjection(middV[8:12], outV[12:16], S5_T)
    eqn = eqn + sboxSpecificSubjection(middV[12:16], outV[4:8], S4_T)
    eqn = eqn + sboxSpecificSubjection(middV[16:20], outV[24:28], S3_T)
    eqn = eqn + sboxSpecificSubjection(middV[20:24], outV[16:20], S2_T)
    eqn = eqn + sboxSpecificSubjection(middV[24:28], outV[28:32], S1_T)
    eqn = eqn + sboxSpecificSubjection(middV[28:32], outV[20:24], S0_T)
    return eqn


def rotationXorSubjection(A, B, C):
    assert len(A) == SUBKEY_SIZE and len(B) == SUBKEY_SIZE and len(C) == SUBKEY_SIZE
    rotA = A[8:16] + A[16:24] + A[24:32] + A[0:8]
    eqn = []
    eqn = eqn + xorAdditionSubjection(rotA, B, C)
    return eqn


def middVars_At_Round(r):
    assert r >= 1
    return ["midd_r" + str(r) + "_" + str(i) for i in range(0, SUBKEY_SIZE)]


def F_Out_At_Round(r):
    assert r >= 1
    return ["fout_r" + str(r) + "_" + str(i) for i in range(0, SUBKEY_SIZE)]


def L_At_Round(r):
    assert r >= 1
    return ["L_r" + str(r) + "_" + str(i) for i in range(0, SUBKEY_SIZE)]


def R_At_Round(r):
    assert r >= 1
    if r == 1:
        return ["R_r" + str(r) + "_" + str(i) for i in range(0, SUBKEY_SIZE)]
    else:
        return L_At_Round(r - 1)


def rotXorOut_At_Round(r):
    assert r >= 1
    return L_At_Round(r + 1)


def genEncryptSubjectionAtRound(r):
    eqn = []
    inF_bits = L_At_Round(r)
    subK_bits = extractSubKeyAtRound(r)
    midd_bits = middVars_At_Round(r)
    fout_bits = F_Out_At_Round(r)
    right_bits = R_At_Round(r)
    rotout_bits = rotXorOut_At_Round(r)
    eqn = eqn + F_Subjection(inF_bits, subK_bits, midd_bits, fout_bits)
    eqn = eqn + rotationXorSubjection(right_bits, fout_bits, rotout_bits)
    return eqn


def genEncrypSubjection(totalRound):
    eqn = []
    for i in range(1, totalRound + 1):
        eqn = eqn + genEncryptSubjectionAtRound(i)
    return eqn


def getVariables(C):
    V = set([])
    for s in C:
        temp = s.strip()
        temp = temp.replace("+", " ")
        temp = temp.replace("-", " ")
        temp = temp.replace(" >=", " ")
        temp = temp.replace(" <=", " ")
        temp = temp.split()
        for v in temp:
            if not v.isdecimal():
                V.add(v)
    return V


if __name__ == "__main__":
    ROUND_TO_COUNT = 12
    print("Minimize ")
    print(" + ".join(["y" + str(i) for i in range(0, ROUND_TO_COUNT * 10)]))
    print("Subject To ")
    beginBits = R_At_Round(1) + L_At_Round(1)
    masterKey = ["k" + str(i) for i in range(0, KEY_SIZE)]
    print(" + ".join(masterKey) + " >= 1")
    AA = keyScheduleSubjection(ROUND_TO_COUNT)
    BB = genEncrypSubjection(ROUND_TO_COUNT)
    for x in AA:
        print(x)
    for x in BB:
        print(x)
    print("Binary ")
    for v in getVariables(AA + BB):
        print(v)
    for v in range(0, 80):
        print("k" + str(v))
    print("End ")
