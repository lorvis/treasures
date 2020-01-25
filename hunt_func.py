
def hunt_recursive(data):
    res = []

    def hunt(curr):
        res.append(int(curr))
        next = str(data[int(curr[0])-1][int(curr[1])-1])
        if curr == next:
            return res
        else:
            return hunt(next)
    return hunt








