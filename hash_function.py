


k = 10
li = [x for x in range(10, 50 + 1, 10)]
for k in li:
    hashh = ((10 * k + 5) % 11) % 5
    
    print(f'k: {k}, hash: {hashh}')