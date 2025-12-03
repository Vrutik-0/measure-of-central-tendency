def mean_ungrouped(data):
    return sum(data) / len(data)

def median_ungrouped(data):
    data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return data[n // 2]
    else:
        return (data[n//2 - 1] + data[n//2]) / 2

def mode_ungrouped(data):
    freq = {}
    for x in data:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    max_f = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_f]

    if len(modes) == len(freq):
        return "No mode"
    return modes

def mean_grouped(cf, fv):
    total_fx = 0
    total_f = 0
    for f, x in zip(cf, fv):
        total_fx += f * x
        total_f += f
    return total_fx / total_f

def median_grouped(class_intervals, freq):
    cf = []
    s = 0
    for f in freq:
        s += f
        cf.append(s)

    n = s
    median_pos = n / 2
    
    for i in range(len(cf)):
        if cf[i] >= median_pos:
            median_class_index = i
            break
    
    L = class_intervals[median_class_index][0]
    f = freq[median_class_index]
    h = class_intervals[median_class_index][1] - class_intervals[median_class_index][0]
    cf_prev = 0 if median_class_index == 0 else cf[median_class_index - 1]
    
    median = L + ((median_pos - cf_prev) / f) * h
    return median

def mode_grouped(class_intervals, freq):
    m = 0
    for i in range(1, len(freq)):
        if freq[i] > freq[m]:
            m = i

    L = class_intervals[m][0]
    f1 = freq[m]
    f0 = 0 if m == 0 else freq[m - 1]
    f2 = 0 if m == len(freq) - 1 else freq[m + 1]
    h = class_intervals[m][1] - class_intervals[m][0]

    if (f1 - f0 + f1 - f2) == 0:
        return "No mode"
    mode = L + ((f1 - f0) / ((f1 - f0) + (f1 - f2))) * h
    return mode
while True:
    try:
        print("---Choose Data Type:---")
        print("1. Ungrouped Data")
        print("2. Grouped Data")
        print("3. Exit")

        choice = int(input("Enter choice: "))
        if choice == 1:
            n = int(input("Enter number of elements: "))
            data = []
            for i in range(n):
                data.append(float(input(f"Enter value x{i+1}: ")))

            print("\n--- (Ungrouped Data) ---")
            print("Mean =", mean_ungrouped(data))
            print("Median =", median_ungrouped(data))
            print("Mode =", mode_ungrouped(data))

        elif choice == 2:
            n = int(input("Enter number of classes: "))

            class_intervals = []
            freq = []

            print("Enter class intervals (lower upper) and frequency:")
            for i in range(n):
                L = float(input(f"Class {i+1} lower limit: "))
                U = float(input(f"Class {i+1} upper limit: "))
                f = int(input("Frequency: "))
                class_intervals.append([L, U])
                freq.append(f)

            # midpoints for mean
            mid = [(x[0] + x[1]) / 2 for x in class_intervals]

            print("\n--- (Grouped Data) ---")
            print("Mean =", mean_grouped(freq, mid))
            print("Median =", median_grouped(class_intervals, freq))
            print("Mode =", mode_grouped(class_intervals, freq))
        
        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as e:
        print("An error occurred:", e)

