#  Suppose you are given a set of positive integers A= {a1, . . . , an}and a positive integer B. Assume ai ≤B
# for all i between 1 and n. A subset S is called feasible if the sum of its elements in S satisfies:
# ai ≤B.
# a∈S
# You would like to select a feasible subset S of A whose total sum is as large as possible.
# a. Consider the following greedy algorithm that keeps adding values as long as the sum is less than or
# equal to B:

def subset_sum_greedy(sett, b):
    s = set()
    initial_sum = 0

    for value in sett:
        if initial_sum + value <= b:
            s.add(value)
            initial_sum += value
        elif initial_sum == b:
            break
    return s


result = subset_sum_greedy({2, 3, 4, 5}, 10)
print(result)
