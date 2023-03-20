# python3
# Patriks Jasinovics 221RDB082

def parallel_processing(n, m, data):
    output = [] #output
    time = [0] * n #finish time
    # function for simulating parallel tasks, 
    # create the output pairs

    for x in range(m):
        thread = 0
        for z in range(1, n):
            if time[z] < time[thread]:
                thread = z
        output.append((thread, time[thread]))
        time[thread] += data[x]

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    #print  results
    
    #  the function
    result = parallel_processing(n,m,data)
    
    # print out the results, each pair in it's own line
    for thread, start_time in result:
        print(thread, start_time)


if __name__ == "__main__":
    main()

