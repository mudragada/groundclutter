"""
The master launch sequence consists of several independent sequences for different systems.
Your goal is to verify that all the individual system sequences are in strictly increasing order.
In other words, for any two elements i and j (i < j) of the master launch sequence that belong to the same system (having systemNames[i] = systemNames[j]),
their values should be in strictly increasing order (i.e. stepNumbers[i] < stepNumbers[j]).

Example:

For systemNames = ["stage_1", "stage_2", "dragon", "stage_1", "stage_2", "dragon"] and stepNumbers = [1, 10, 11, 2, 12, 111], the output should be
launchSequenceChecker(systemNames, stepNumbers) = true.

There are three independent sequences for systems "stage_1", "stage_2", and "dragon". These sequences are [1, 2], [10, 12], and [11, 111], respectively. The elements are in strictly increasing order for all three.

For systemNames = ["stage_1", "stage_1", "stage_2", "dragon"] and stepNumbers = [2, 1, 12, 111], the output should be
launchSequenceChecker(systemNames, stepNumbers) = false.

There are three independent sequences for systems "stage_1", "stage_2", and "dragon". These sequences are [2, 1], [12], and [111], respectively. In the first sequence, the elements are not ordered properly.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string systemNames

An array of non-empty strings. systemNames[i] contains the name of the system to which the ith element of the master launch sequence belongs.

Guaranteed constraints:
1 ≤ systemNames.length ≤ 5 · 104,
1 ≤ systemNames[i].length ≤ 10.

[input] array.integer stepNumbers

An array of positive integers. stepNumbers[i] contains the value of the ith element of the master launch sequence.

Guaranteed constraints:
stepNumbers.length = systemNames.length,
1 ≤ stepNumbers[i] ≤ 109.

[output] boolean

Return true if all the individual system sequences are in strictly increasing order, otherwise return false.
"""

def main():
    systemNames = ["stage_1", "stage_1", "stage_2", "dragon"]
    stepNumbers = [2, 1, 12, 111]
    print(launchSequenceChecker(systemNames, stepNumbers))

    systemNames = ["stage_1", "stage_2", "dragon", "stage_1", "stage_2", "dragon"]
    stepNumbers = [1, 10, 11, 2, 12, 111]
    print(launchSequenceChecker(systemNames, stepNumbers))

    systemNames = ["Falcon 9", "Falcon 9", "Falcon 9", "Falcon 9","Falcon 9","Falcon 9"]
    stepNumbers = [1, 3, 5, 7, 7, 9]
    print(launchSequenceChecker(systemNames, stepNumbers))

    systemNames = ["Dragon","Falcon 9","Dragon","Falcon 9","Falcon 9","Dragon","Dragon","Dragon","Falcon 9"]
    stepNumbers = [1, 1, 3, 2, 4, 10, 20, 100, 4]
    print(launchSequenceChecker(systemNames, stepNumbers))

def launchSequenceChecker(systemNames, stepNumbers):
    # Find all unique positions of the list
    systemStepDict = dict()
    for idx in range(0, len(systemNames)):
        systemName = systemNames[idx]
        key = systemName
        value = []
        if systemName not in systemStepDict.keys():
            value.append(stepNumbers[idx])
            systemStepDict[key] = value
        else:
            value = list(systemStepDict[key])
            value.append(stepNumbers[idx])
        systemStepDict[key] = value

    # Verify if every stage is in increasing order
    bIsStrictlyIncreasing = True
    for key, value in systemStepDict.items():
        result = all(value[i] < value[i+1] for i in range(0,len(value)-1))
        if(result == False):
            bIsStrictlyIncreasing = False
            break
    return bIsStrictlyIncreasing




# def launchSequenceChecker(systemNames, stepNumbers):
#     for i in range(0, len(systemNames)-1):
#         if(systemNames[i] == systemNames[i+1]):
#             if(stepNumbers[i] > stepNumbers[i+1]):
#                 return False
#             else:
#                 pass
#     return True


if __name__ == '__main__':
    main()
