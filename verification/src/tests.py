"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Rank_1": [
        {
            "input": [[7, 2, 7, 2, 8], [2, 9, 4, 1, 7], [3, 8, 6, 2, 4], [2, 5, 2, 9, 1], [6, 6, 5, 4, 5]],
            "answer": [3, 3],
            "explanation": [[26, 23, 23, 19, 26], [20, 30, 24, 18, 25]],
        },
        {
            "input": [[7, 2, 4, 2, 8], [2, 8, 1, 1, 7], [3, 8, 6, 2, 4], [2, 5, 2, 9, 1], [6, 6, 5, 4, 5]],
            "answer": [1, 2],
            "explanation": [[23, 19, 23, 19, 26], [20, 29, 18, 18, 25]],
        },
        {
            "input": [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            "answer": [0, 0],
            "explanation": [[3, 3, 3], [3, 3, 3]],
        },
        {
            "input": [[1]],
            "answer": [0, 0],
            "explanation": [[1], [1]],
        },
        {
            "input": [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                      [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                      [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                      [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]],
            "answer": [0, 0],
            "explanation": [[90, 90, 90, 90, 90, 90, 90, 90, 90, 90], [90, 90, 90, 90, 90, 90, 90, 90, 90, 90]],
        },
        {
            "input": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 1],
                      [2, 3, 4, 5, 6, 7, 8, 9, 1, 2],
                      [3, 4, 5, 6, 7, 8, 9, 1, 2, 3],
                      [4, 5, 6, 7, 8, 9, 1, 2, 3, 4],
                      [5, 6, 7, 8, 9, 1, 2, 3, 4, 5],
                      [6, 7, 8, 9, 1, 2, 3, 4, 5, 6],
                      [7, 8, 9, 1, 2, 3, 4, 5, 6, 7],
                      [8, 9, 1, 2, 3, 4, 5, 6, 7, 8],
                      [9, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]],
            "answer": [0, 0],
            "explanation": [[46, 47, 48, 49, 50, 51, 52, 53, 54, 46], [46, 47, 48, 49, 50, 51, 52, 53, 54, 46]],
        },
        {
            "input": [[8, 4, 4, 8, 8, 5, 8], [2, 9, 1, 5, 7, 3, 1], [7, 1, 5, 2, 2, 3, 2], [3, 3, 7, 6, 9, 2, 5],
                      [3, 2, 3, 1, 3, 3, 4], [1, 8, 4, 8, 9, 7, 4], [8, 9, 1, 8, 8, 5, 2]],
            "answer": [4, 2],
            "explanation": [[45, 28, 22, 35, 19, 41, 41], [32, 36, 25, 38, 46, 28, 26]],
        },
        {
            "input": [[7, 5, 1, 5, 1, 9, 6, 3], [1, 6, 1, 5, 2, 4, 4, 2], [1, 5, 2, 8, 4, 3, 8, 3],
                      [2, 9, 7, 5, 1, 8, 3, 3], [7, 9, 9, 5, 7, 6, 2, 6], [2, 9, 9, 2, 5, 1, 8, 3],
                      [8, 9, 1, 1, 7, 5, 7, 7], [7, 5, 1, 3, 1, 6, 1, 3]],
            "answer": [1, 4],
            "explanation": [[37, 25, 34, 38, 51, 39, 45, 27], [35, 57, 31, 34, 28, 42, 39, 30]],
        },
        {
            "input": [[8, 3, 3, 4, 1, 4, 4], [6, 2, 5, 9, 7, 4, 7], [3, 2, 5, 4, 8, 6, 6], [3, 1, 4, 2, 1, 3, 4],
                      [4, 4, 4, 6, 4, 6, 1], [8, 7, 5, 6, 1, 1, 2], [2, 1, 3, 4, 2, 1, 9]],
            "answer": [3, 1],
            "explanation": [[27, 40, 34, 18, 29, 30, 22], [34, 20, 29, 35, 24, 25, 33]],
        },
        {
            "input": [[6, 3, 8, 8, 2, 4, 5], [9, 4, 3, 7, 4, 7, 5], [8, 1, 7, 9, 1, 2, 3], [8, 5, 5, 8, 2, 5, 9],
                      [6, 6, 6, 5, 5, 5, 4], [1, 8, 9, 5, 9, 2, 2], [2, 2, 2, 2, 3, 9, 2]],
            "answer": [6, 4],
            "explanation": [[36, 39, 31, 42, 37, 36, 22], [40, 29, 40, 44, 26, 34, 30]],
        },
        {
            "input": [[1, 9, 2, 6, 5], [3, 6, 3, 3, 6], [4, 8, 4, 2, 5], [3, 9, 7, 4, 3], [3, 7, 3, 4, 3]],
            "answer": [4, 0],
            "explanation": [[23, 21, 23, 26, 20], [14, 39, 19, 19, 22]],
        },
        {
            "input": [[9, 4], [2, 6]],
            "answer": [1, 1],
            "explanation": [[13, 8], [11, 10]],
        },
        {
            "input": [[8, 4, 7, 3, 6], [1, 8, 4, 9, 8], [9, 4, 7, 2, 7], [2, 8, 9, 5, 1], [6, 3, 5, 9, 1]],
            "answer": [4, 4],
            "explanation": [[28, 30, 29, 25, 24], [26, 27, 32, 28, 23]],
        },
        {
            "input": [[2, 5, 9, 1, 3, 7, 7, 7, 6, 2], [7, 6, 1, 9, 3, 7, 6, 5, 9, 4], [9, 6, 3, 8, 7, 8, 1, 8, 7, 4],
                      [7, 5, 1, 9, 2, 8, 4, 4, 1, 4], [8, 3, 9, 8, 6, 2, 9, 1, 3, 2], [3, 4, 1, 3, 1, 6, 1, 2, 6, 9],
                      [9, 4, 1, 3, 4, 2, 3, 6, 8, 5], [1, 1, 1, 4, 5, 4, 9, 6, 6, 5], [7, 8, 5, 4, 7, 6, 6, 1, 4, 9],
                      [1, 3, 3, 5, 2, 4, 3, 3, 9, 1]],
            "answer": [9, 2],
            "explanation": [[49, 57, 61, 45, 51, 36, 45, 42, 57, 34], [54, 45, 34, 54, 40, 54, 49, 43, 59, 45]],
        },
    ]
}