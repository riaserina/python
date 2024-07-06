import numpy as np


users_stats = np.array(
    [
        [2, 1, 0, 0, 0, 0],
        [1, 1, 2, 1, 0, 0],
        [2, 0, 1, 0, 0, 0],
        [1, 1, 2, 1, 0, 1],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 0, 5],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 3],
        [1, 0, 0, 2, 1, 4]
    ],
    np.int32
)

next_user_stats = np.array([0, 1, 2, 0, 0, 0])

def cosine(a, b):
    aLength = np.linalg.norm(a)
    bLength = np.linalg.norm(b)

    return np.dot(a, b) / (aLength * bLength)


b = next_user_stats
i = 0
user_dict = {}
for user in users_stats:
    i += 1
    user_dict.update({i: cosine(user, b)})
    # print(round(cosine(user,b),2))
max(user_dict, key=user_dict.get)