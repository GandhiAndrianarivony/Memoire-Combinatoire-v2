from itertools import permutations


def is_321(sigma):
    pivot = sigma[0]
    pivot_index = 0
    sigma_len = len(sigma)

    while pivot_index < sigma_len - 1:
        for i in range(pivot_index + 1, sigma_len - 1):
            if i + 1 == sigma_len-1:
                if pivot > sigma[i] > sigma[i+1]:
                    return True

            for j in range(i + 1, sigma_len):
                if pivot > sigma[i] > sigma[j]:
                    return True
                
        pivot = get_pivot(pivot, sigma)

        if not pivot:
            return False
        
        pivot_index = sigma.index(pivot)

    return False


def is_fix_point(p):
    for idx, i in enumerate(p):
        if idx < len(p)-1:
            if i == idx+1:
                return True


def get_pivot(actual, data):
    actual_pivot_index = data.index(actual)
    if actual_pivot_index < len(data) - 1:
        for idx in range(actual_pivot_index + 1, len(data)):
            if data[idx] > actual:
                return data[idx]

def get_Tn(perms):
    iteration = 0
    output = []
    for p in perms:
        if not is_321(list(p)):
            if is_fix_point(p):
                iteration += 1
                output.append(p)

    return f"T_{n}(321) = {iteration}", [''.join(map(str, tpl)) for tpl in output]


if __name__ == "__main__":
    n = int(input(f"Enter n: "))
    perms = permutations(range(1, n + 1))
    print(get_Tn(perms))