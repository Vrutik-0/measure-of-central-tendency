import matplotlib.pyplot as plt

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
    
    lower = class_intervals[median_class_index][0]
    f = freq[median_class_index]
    h = class_intervals[median_class_index][1] - class_intervals[median_class_index][0]
    cf_prev = 0 if median_class_index == 0 else cf[median_class_index - 1]
    
    median = lower + ((median_pos - cf_prev) / f) * h
    return median

def mode_grouped(class_intervals, freq):
    m = 0
    for i in range(1, len(freq)):
        if freq[i] > freq[m]:
            m = i

    lower = class_intervals[m][0]
    f1 = freq[m]
    f0 = 0 if m == 0 else freq[m - 1]
    f2 = 0 if m == len(freq) - 1 else freq[m + 1]
    h = class_intervals[m][1] - class_intervals[m][0]

    if (f1 - f0 + f1 - f2) == 0:
        return "No mode"
    mode = lower + ((f1 - f0) / ((f1 - f0) + (f1 - f2))) * h
    return mode

def plot_ungrouped(data, mean, median, mode):
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.bar(range(1, len(data) + 1), data, color='skyblue', edgecolor='black')
    plt.axhline(y=mean, color='red', linestyle='--', label=f'Mean = {mean:.2f}')
    plt.axhline(y=median, color='green', linestyle='-.', label=f'Median = {median:.2f}')
    plt.xlabel('Data Point')
    plt.ylabel('Value')
    plt.title('Ungrouped Data - Bar Chart')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.hist(data, bins='auto', color='lightgreen', edgecolor='black')
    plt.axvline(x=mean, color='red', linestyle='--', label=f'Mean = {mean:.2f}')
    plt.axvline(x=median, color='green', linestyle='-.', label=f'Median = {median:.2f}')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Ungrouped Data - Histogram')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def plot_grouped(class_intervals, freq, mean, median, mode):
    plt.figure(figsize=(12, 5))
    
    labels = [f'{int(ci[0])}-{int(ci[1])}' for ci in class_intervals]
    x_pos = range(len(labels))
    
    plt.subplot(1, 2, 1)
    plt.bar(x_pos, freq, color='coral', edgecolor='black')
    plt.xticks(x_pos, labels, rotation=45)
    plt.xlabel('Class Intervals')
    plt.ylabel('Frequency')
    plt.title('Grouped Data - Frequency Bar Chart')
    
    plt.subplot(1, 2, 2)
    midpoints = [(ci[0] + ci[1]) / 2 for ci in class_intervals]
    widths = [ci[1] - ci[0] for ci in class_intervals]
    
    plt.bar(midpoints, freq, width=widths[0], color='lightblue', edgecolor='black', alpha=0.7)
    plt.plot(midpoints, freq, 'ro-', label='Frequency Polygon')
    
    if isinstance(mean, (int, float)):
        plt.axvline(x=mean, color='red', linestyle='--', label=f'Mean = {mean:.2f}')
    if isinstance(median, (int, float)):
        plt.axvline(x=median, color='green', linestyle='-.', label=f'Median = {median:.2f}')
    if isinstance(mode, (int, float)):
        plt.axvline(x=mode, color='blue', linestyle=':', label=f'Mode = {mode:.2f}')
    
    plt.xlabel('Class Midpoints')
    plt.ylabel('Frequency')
    plt.title('Grouped Data - Histogram with Frequency Polygon')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

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
            mean_val = mean_ungrouped(data)
            median_val = median_ungrouped(data)
            mode_val = mode_ungrouped(data)
            print("Mean =", mean_val)
            print("Median =", median_val)
            print("Mode =", mode_val)
            
            plot_ungrouped(data, mean_val, median_val, mode_val)

        elif choice == 2:
            n = int(input("Enter number of classes: "))

            class_intervals = []
            freq = []

            print("Enter class intervals (lower upper) and frequency:")
            for i in range(n):
                lower = float(input(f"Class {i+1} lower limit: "))
                upper = float(input(f"Class {i+1} upper limit: "))
                f = int(input("Frequency: "))
                class_intervals.append([lower, upper])
                freq.append(f)

            mid = [(x[0] + x[1]) / 2 for x in class_intervals]

            print("\n--- (Grouped Data) ---")
            mean_val = mean_grouped(freq, mid)
            median_val = median_grouped(class_intervals, freq)
            mode_val = mode_grouped(class_intervals, freq)
            print("Mean =", mean_val)
            print("Median =", median_val)
            print("Mode =", mode_val)
            
            plot_grouped(class_intervals, freq, mean_val, median_val, mode_val)
        
        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter numeric values.")
    except Exception as e:
        print("An error occurred:", e)