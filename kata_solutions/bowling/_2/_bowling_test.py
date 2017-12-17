from kata_solutions.bowling._2.bowling import score


# zombies
# zero
# one
# many
# boundaries - 10th frame
# interface
# exceptional - spare / strike
# simple

def test_score_zeros():
    frames = [[0, 0] * 10] # 0x

    bowling_score = score(frames)

    assert 0 == bowling_score


def test_score_one():
    frames = [[1, 0]] # 1, 0x
    frames.append([0, 0] * 9)

    bowling_score = score(frames)

    assert 1 == bowling_score


def test_scores_no_strike_no_spare():
    frames = [[5, 4] * 10] # 9, 9, 9, 9, 9, 9, 9, 9, 9, 9

    bowling_score = score(frames)

    assert 90 == bowling_score


def test_spare_zero_next():
    frames = [[1, 9]] # 10, 0x
    frames.append([0, 0] * 9)

    bowling_score = score(frames)

    assert 10 == bowling_score


def test_spare_not_zero_next():
    frames = [[1, 9], [1, 0]] # 11, 1, 0x
    frames.append([0, 0] * 8)

    bowling_score = score(frames)

    assert 12 == bowling_score

def test_spare_multiple_spares():
    frames = [[1, 9], [1, 9], [1, 9]] # 11, 11, 10, 0x
    frames.append([0, 0] * 7)

    bowling_score = score(frames)

    assert 32 == bowling_score

def test_strike_zero_frame_next():
    frames = [[10, 0]] # 10, 0x
    frames.append([0, 0] * 9)

    bowling_score = score(frames)

    assert 10 == bowling_score

def test_strike_score_frame_next_zero_next():
    frames = [[10, 0],[1,1], [0,0]] # 12, 2, 0x
    frames.append([0, 0] * 9)

    bowling_score = score(frames)

    assert 14 == bowling_score


# refactoring ensues!
# def test_strike_score_frame_next_score_next():
#     frames = [[10, 0],[1,1], [1,9]] # 22, 2, 10, 0x
#     frames.append([0, 0] * 9)
#
#     bowling_score = score(frames)
#
#     assert 34 == bowling_score


# Create a program, which, given a valid sequence of rolls for one line of American Ten-Pin Bowling, produces the total score for the game. Here are some things that the program will not do:

# We can briefly summarize the scoring for this form of bowling:
#
# If on his first try in the frame he knocks down all the pins, this is called a “strike”. His turn is over, and
# his score for the frame is ten plus the simple total of the pins knocked down in his next two rolls.
#
# If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. These bonus throws are taken as part of the same turn. If the bonus throws knock down all the pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.
#
# The game score is the total of all frame scores.
