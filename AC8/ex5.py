def main():
    n = int(input())

    frequencia = {}

    for _ in range(n):
        num = int(input())
        if num in frequencia:
            frequencia[num] += 1
        else:
            frequencia[num] = 1

    for num in sorted(frequencia.keys()):
        print(f"{num} aparece {frequencia[num]} vez(es)")


if __name__ == "_main_":
    main()