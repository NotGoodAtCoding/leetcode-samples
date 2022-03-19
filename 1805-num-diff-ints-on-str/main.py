  def numDifferentIntegers(self, word: str) -> int:
        nits = {}
        runes = ""
        for s in word:
            if s.isdigit():
                runes += s
            elif len(runes) > 0:
                nits[runes.lstrip("0")] = True
                runes = ""

        if len(runes):
            nits[runes.lstrip("0")] = True

        return len(nits)
