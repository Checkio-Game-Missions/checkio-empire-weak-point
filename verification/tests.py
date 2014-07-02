"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
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
    ],
    "Extra": [
        {
            "input": [6, 3],
            "answer": 9,
            "explanation": "6+3=?"
        },
        {
            "input": [6, 7],
            "answer": 13,
            "explanation": "6+7=?"
        }
    ]
}
