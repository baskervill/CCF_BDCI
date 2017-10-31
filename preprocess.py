def conver_to_string(records):
    out_string = ''
    for record in records:
        out_string += '/Users/hp/tensorflow-yolo/data/fangyi/'
        for i in record:
            if isinstance(i, str):
                out_string += i 
            else:
                out_string += ' ' + str(i)
        out_string += '\n'
    return out_string
def filter(ss):
    for i in range(2,6):
        if ss[i] > 1024:
            ss[i] = 1023
    if ss[2] > ss[4]:
        tmp = ss[2]
        ss[2] = ss[4]
        ss[4] = tmp
    if ss[3] > ss[5]:
        tmp = ss[3]
        ss[3] = ss[5]
        ss[5] = tmp
    return ss 
def preprocess(input_file):
    #input_file = open('gt_yuchuan.txt')
    dict = {"huochuan":1, "youlun":2, "youting":3, "yuchuan":4}
    record_list = []
    index = 0
    ss1 = []
    for line in input_file.readlines():
        line = line.strip()
        ss = line.split(' ')
        ss[1] = dict[ss[1]]
        ss[1:] = [int(num) for num in ss[1:]]
        ss = filter(ss)
        if len(ss1) == 0:
            ss1.append(ss[0])
            for i in range(2,6):
                ss1.append(ss[i])
            ss1.append(ss[1])
            continue
        elif ss[0] == ss1[0] :
            for i in range(2,6):
                ss1.append(ss[i])
            ss1.append(ss[1])
            continue
        else  :
            index = 0
            record_list.append(ss1)
            ss1 = []
            ss1.append(ss[0])
            for i in range(2,6):
                ss1.append(ss[i])
            ss1.append(ss[1])
    if len(ss1) != 0:
        record_list.append(ss1)
    return record_list

def merge_join(list1, list2):#sorted and unique
    record_list = []
    i, j = 0, 0
    print 
    while i < len(list1):
        while j < len(list2):
            if list1[i][0] == list2[j][0]:
                record_list.append(list1[i] + list2[j][1:])
                j = j + 1
                i = i + 1
            elif list1[i][0] < list2[j][0]:
                record_list.append(list1[i])
                i = i + 1
            else :
                record_list.append(list2[j])
                j = j + 1
        if j >= len(list2):
            record_list.append(list1[i])
            i = i + 1
    return record_list
            

def main():
    input_file1 = open('gt_huochuan.txt')
    record_list1 = preprocess(input_file1)
    input_file2 = open('gt_youlun.txt')
    record_list2 = preprocess(input_file2)
    input_file3 = open('gt_youting.txt')
    record_list3 = preprocess(input_file3)
    input_file4 = open('gt_yuchuan.txt')
    record_list4 = preprocess(input_file4)
    record_list = merge_join(merge_join(merge_join(record_list1,record_list2),record_list3),record_list4)
    output_file = open('merge.txt', 'w')
    output_file.write(conver_to_string(record_list))
    output_file.close()
if __name__ == '__main__':
    main()