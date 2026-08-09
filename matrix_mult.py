import sys
import time

def main():
    if len(sys.argv) < 2:
        print("Uso: python matrix_mult.py <tamaño_N>", file=sys.stderr)
        sys.exit(1)

    N = int(sys.argv[1])
    if N <= 0:
        print("El tamaño N debe ser un entero positivo.", file=sys.stderr)
        sys.exit(1)

    A = [[float(i + j) for j in range(N)] for i in range(N)]
    B = [[float(i - j) for j in range(N)] for i in range(N)]
    C = [[0.0 for _ in range(N)] for _ in range(N)]

    start_time = time.perf_counter()

    for i in range(N):
        for j in range(N):
            total = 0.0
            for k in range(N):
                total += A[i][k] * B[k][j]
            C[i][j] = total

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(f"{elapsed_time:.8f}")

if __name__ == "__main__":
    main()
