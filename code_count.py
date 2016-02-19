#!/bin/python3.5
import os

# Add filetype what you want to scan in the dictionary
code_sum = {'c':0, 'cpp':0, 'html':0, 'py':0, 'css':0, 'total':0}

def coding_count(path):
    print("- Scanning " + path)
    curfiles = os.listdir(path)

    for each in curfiles:
        if os.path.isdir(each):
            new_path = path + '/' + each    #get new path
            coding_count(new_path)   #do the function recursively
            continue

        print("- Reading " + each)
        filetype = each.split('.')[-1]      #get filetype by name
        for types in code_sum:
            if filetype == types:
                fd = open(path + '/' + each, 'r')
                for eachline in fd:
                    code_sum[types] += 1
                    code_sum["total"] += 1

def show_result():
    print("---------Scan over----------------")
    print("\n\nLets see how many lines you typed!")
    print("----------------------------------")
    for each in code_sum:
        if each == "total":
            continue
        print(each + ":\t|" + (str)(code_sum[each]))
    print("----------------------------------\n")
    print("Wow! you typed *%d* lines totally!\n" % code_sum["total"])



def main():
    coding_count(".")
    show_result()

if __name__ == "__main__":
    main()
