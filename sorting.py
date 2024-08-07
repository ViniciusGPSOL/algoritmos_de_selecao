from modules import selection_sort, insertion_sort, bubble_sort, shell_sort, quick_sort
import time

def main():
    i = 0
    performance_list = []
    while i != 2:
        try:
            # selecionar qual vai ser o método de organização
            print("Select the sorting method:")
            print("1. Selection Sort")
            print("2. Insertion Sort")
            print("3. Bubble Sort")
            print("4. Shell Sort")
            print("5. Quick Sort")
            print("6. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 6:
                break
            #seleciona o arquivo de origem dos numeros: 
            # 1. para C:\Users\Vinicius\algoritmos_de_selecao\numeros_aleatorios.txt 
            # 2. para C:\Users\Vinicius\algoritmos_de_selecao\numeros_ordem_decrescente.txt
            # 3. para C:\Users\Vinicius\algoritmos_de_selecao\numeros_ordenados.txt
            # e armazena os dados do arquivo em uma array
            
            print("Select the file with the numbers:")
            print("1. Random numbers")
            print("2. Descending order numbers")
            print("3. Ascending order numbers")
            file_choice = int(input("Enter your choice: "))
            if file_choice == 1:
                file_path = "C:\\Users\\Vinicius\\algoritmos_de_selecao\\numeros_aleatorios.txt"
            elif file_choice == 2:
                file_path = "C:\\Users\\Vinicius\\algoritmos_de_selecao\\numeros_ordem_decrescente.txt"
            elif file_choice == 3:
                file_path = "C:\\Users\\Vinicius\\algoritmos_de_selecao\\numeros_ordenados.txt"
            else:
                print("Invalid input. Please enter a valid number.")
                continue
            with open(file_path, "r") as file:
                arr = [int(x) for x in file.read().split()]

            #dar a opção de escolher a quantidade de números a serem ordenados depois de escolher o arquivo
            #opções: 1000, 10000, 100000, 1000000

            print("Select the number of elements to be sorted:")
            print("1. 1000")
            print("2. 10000")
            print("3. 100000")
            print("4. 1000000")
            num_choice = int(input("Enter your choice: "))
            if num_choice == 1:
                arr = arr[:1000]
            elif num_choice == 2:
                arr = arr[:10000]
            elif num_choice == 3:
                arr = arr[:100000]
            elif num_choice == 4:
                arr = arr[:1000000]
            else:
                print("Invalid input. Please enter a valid number.")
                continue

            i += 1

            #chama a função de ordenação escolhida e armazena o tempo de execução
            if choice == 1:
                start = time.time()
                comp, mov = selection_sort(arr)
                end = time.time()
                print("Selection Sort")
                algorithm = "Selection Sort"
            elif choice == 2:
                start = time.time()
                comp, mov = insertion_sort(arr)
                end = time.time()
                print("Insertion Sort")
                algorithm = "Insertion Sort"
            elif choice == 3:
                start = time.time()
                comp, mov = bubble_sort(arr)
                end = time.time()
                print("Bubble Sort")
                algorithm = "Bubble Sort"
            elif choice == 4:
                start = time.time()
                comp, mov = shell_sort(arr)
                end = time.time()
                print("Shell Sort")
                algorithm = "Shell Sort"
            elif choice == 5:
                start = time.time()
                comp, mov = quick_sort(arr, 0, len(arr)-1)
                end = time.time()
                algorithm = "Quick Sort"
                print("Quick Sort")
            
            #armazenar as estatisticas de perfomance em uma lista para comparar qual dos dois é o melhor algoritmo de sorting

            performance = [end-start, comp, mov, algorithm]
            performance_list.append(performance)

            print("Time taken: ", end-start)
            print("Number of comparisons: ", comp)
            print("Number of movements: ", mov)
            print("Sorted array: ", arr)
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
    #comparar os algoritmos de sorting e mostrar qual é o melhor
    print("Performance comparison:")
    print("Time taken\tComparisons\tMovements")
    for i in range(len(performance_list)):
        print(performance_list[i][0], "\t", performance_list[i][1], "\t", performance_list[i][2])
    print("The best between the two selected sorting algorithms is:")
    if performance_list[0][0] < performance_list[1][0]:
        print(performance_list[0][3])
        #% better
        print((performance_list[1][0] - performance_list[0][0]) / performance_list[1][0] * 100, "% better")
    else:
        print(performance_list[1][3])
        #% better
        print((performance_list[0][0] - performance_list[1][0]) / performance_list[0][0] * 100, "% better")


if __name__ == "__main__":

    main()