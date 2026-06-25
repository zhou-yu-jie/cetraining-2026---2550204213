def calculateaverage(num_list):
    if len(num_list) == 0:
        return 0
    total = sum(num_list)
    avg = total / len(num_list)
    return avg


if __name__ == "__main__":
    data = [85, 90, 78, 92]
    print("平均值：", calculateaverage(data))