Use a stack to track best candidate pairs of last min and max, reference that to decide if incoming value fits one of the criteria:

1. Is a solution, return True
2. is a better candidate than the last recorded one: update last recorded best candidate
3. is a beginning to a new candidate: pop the last unsuccessful candidates to replace with a better one. 
