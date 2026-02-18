x = 267
total = 0
while x > 0:
    if total > 500:
        print(f'Total is now over 500! Final Total: {total}')
        break
    total += x
    x = x // 2
    print(f'Total: {total}, Next add x: {x}')