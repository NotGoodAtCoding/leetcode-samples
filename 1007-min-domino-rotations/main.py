def minDominoRotations(tops: List[int], bottoms: List[int]) -> int:
    valid = {tops[0], bottoms[0]}

    for top, bottom in zip(tops, bottoms):
        valid = valid.intersection({top, bottom})
        if not valid:
            return -1
    top_flips = bot_flips = len(tops)
    for solution in valid:
        top_flips = min(top_flips, len([t for t in tops if t != solution]))
        bot_flips = min(bot_flips, len([b for b in bottoms if b != solution]))

    return min(top_flips, bot_flips)
