func numDifferentIntegers(word string) int {
    integers := make(map[string]bool)
	runes := ""

	for _, c := range word {
		if unicode.IsDigit(c) {
			runes = runes + string(c)
		} else if len(runes) > 0 {
			integers[strings.TrimLeft(string(runes), "0")] = true
			runes = ""
		}
	}

	if len(runes) > 0 {
		integers[strings.TrimLeft(string(runes), "0")] = true
	}

	return len(integers)
}
