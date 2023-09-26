import random
import time



def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def generate_numbers(n, user_input=True):
    if user_input:
        return [int(input(f"Digite o número {i+1}: ")) for i in range(n)]
    else:
        return [random.randint(1, 10**5) for i in range(n)]

def time_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr.copy())
    return time.time() - start_time

def display_sorted_result(name, original, sorted_arr, elapsed_time):
    """Exibe o resultado de uma operação de ordenação em um formato mais claro."""
    print("\n" + "-"*50)
    print(f"Algoritmo: {name}")
    print("-"*50)
    print("Vetor ANTES da ordenação:")
    print(original)
    print("\nVetor APÓS da ordenação:")
    print(sorted_arr)
    print(f"\nTempo de execução: {elapsed_time:.5f} segundos")
    print("-"*50 + "\n")

def main():
    while True:
        print("""
        1- Bubble Sort
        2- Insertion Sort
        3- Selection Sort
        4- Merge Sort
        5- Quicksort
        6- Comparativo de tempo de execução
        7- Sair
        """)

        choice = int(input("Escolha uma opção: "))

        if choice == 7:
            break
        elif choice in [1, 2, 3, 4, 5]:
            n = int(input("Quantos números serão ordenados? "))
            user_input = input("Você vai inserir os números (s/n)? ").lower() == 's'
            arr = generate_numbers(n, user_input)
            
            start_time = time.time()
            
            if choice == 1:
                sorted_arr = bubble_sort(arr.copy())
                display_sorted_result("Bubble Sort", arr, sorted_arr, time.time() - start_time)
            elif choice == 2:
                sorted_arr = insertion_sort(arr.copy())
                display_sorted_result("Insertion Sort", arr, sorted_arr, time.time() - start_time)
            elif choice == 3:
                sorted_arr = selection_sort(arr.copy())
                display_sorted_result("Selection Sort", arr, sorted_arr, time.time() - start_time)
            elif choice == 4:
                sorted_arr = merge_sort(arr.copy())
                display_sorted_result("Merge Sort", arr, sorted_arr, time.time() - start_time)
            elif choice == 5:
                sorted_arr = quicksort(arr.copy())
                display_sorted_result("Quicksort", arr, sorted_arr, time.time() - start_time)
        elif choice == 6:
            sizes = [10000, 30000]
            algorithms = [("Bubble Sort", bubble_sort), ("Insertion Sort", insertion_sort), 
                          ("Selection Sort", selection_sort), ("Merge Sort", merge_sort), 
                          ("Quick Sort", quicksort)]
            
            for size in sizes:
                print(f"\nComparativo para vetor de tamanho {size}:")
                arr = generate_numbers(size, False)
                times = [(name, time_algorithm(func, arr)) for name, func in algorithms]
                times.sort(key=lambda x: x[1])

                for i, (name, t) in enumerate(times):
                    print(f"{i+1}-{name}: {t:.2f} segundos")

if __name__ == "__main__":
    main()