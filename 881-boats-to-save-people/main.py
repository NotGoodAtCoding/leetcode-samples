def numRescueBoats(self, people: List[int], limit: int) -> int:
    sor_people = sorted(people)
    low = boats = 0
    high = len(people) - 1
    while low < len(people) and high >= low:
        if people[low] + people[high] <= limit:
            low += 1
            high -= 1
        else:
            high -= 1
        boats += 1

    return boats


def numRescueBoats(self, people: List[int], limit: int) -> int:
    sortedPeople = sorted(people, reverse=True)
    first = 0
    last = len(sortedPeople) - 1

    if len(sortedPeople) == 2:
        return 2 if sortedPeople[0] + sortedPeople[1] > limit else 1

    boats = 0

    while first <= last:
        if sortedPeople[first] + sortedPeople[last] > limit:
            first = first + 1
        else:
            first, last = first + 1, last - 1

        boats = boats + 1

    return boats
