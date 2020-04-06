"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

"""
def main():
    testSequences = [[1, 1, 2, 3],
                [1, 3, 2],
                [1, 2, 1, 2],
                [3, 5, 6, 8, 10, 20, 15],
                [1, 1, 1, 2, 3],
                [0, -2, 5, 6],
                [1, 2, 3, 4, 5, 3, 5, 6],
                [1, 2, 3, 4, 5, 5, 6],
                [5, 4, 3, 2, 1]]
    for sequence in testSequences:
        printstr = "Is {0} almost an increasing sequence? {1}".format(sequence, almostIncreasingSequence(sequence))
        print(printstr)

def almostIncreasingSequence(sequence):
    if(len(sequence) <2):
        return True
    elif(len(sequence) ==2):
        if (sequence[0] <= sequence[1]):
            return True
        else:
            return False
    else:
        for i in range(0, len(sequence)):
            ## When you first encountered a non increasing part of the sequence,
            if(sequence[i] >= sequence[i+1]):
                #Make two checks. 1. By removing i th element
                newSequence1 = sequence[:i] + sequence[i+1:]
                newSequence2 = sequence[:i+1] + sequence[i+2:]

                if((all(i < j for i, j in zip(newSequence1, newSequence1[1:])))):
                    return True
                elif((all(i < j for i, j in zip(newSequence2, newSequence2[1:])))):
                    return True
                else:
                    return False


if __name__ == '__main__':
    main()
