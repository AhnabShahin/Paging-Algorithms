def take_pages():
    input_Pages = (input('Input queue : ')).strip(' ')
    array = input_Pages.split(' ')
    Total_Pages = len(array)
    print(array)

    return Total_Pages, array


def len_of_memory():
    input_len_of_memory = int(input('Input Memory Size : '))
    return input_len_of_memory


def main_process(m, t, a):
    fault = 0
    hit = 0
    memory_size = m
    total_pages = t
    array = a
    memory = ['-', '-', '-']

    j = 0
    i = 0

    while j < total_pages:
        n, hi, fau = fault_hit(memory_size, total_pages, array, j, memory, fault, hit)
        fault = fau
        hit = hi
        j = n
    print('Number of hit  :' + str(hit))
    print('Number of fault:' + str(fault))


def fault_hit(m, t, a, n, m1, fau, hi):
    fault = fau
    hit = hi
    memory_size = m
    total_pages = t
    array = a
    memory = m1
    j = n
    i = 0

    while i < memory_size:
        inc = 0
        if j < total_pages:
            for f in range(0, memory_size):
                if memory[f] == array[j]:
                    last_page = array[j]
                    # print(j)
                    j = j + 1
                    inc = 1
                    hit = hit + 1
                    print(['-', '-', '-'])

            if inc == 0:
                memory[i] = array[j]
                last_page = array[j]
                # print(j)
                j = j + 1
                i = i + 1
                print(memory)
                fault = fault + 1
        else:
            break
    return j, hit, fault


total_pages, array = take_pages()
memory_size = len_of_memory()
main_process(memory_size, total_pages, array)
