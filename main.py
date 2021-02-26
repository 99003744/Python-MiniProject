'''
Author : Kinjal Kundu
PS No. : 99003744
Mail ID : kinjal.kundu@ltts.com
This program is about finding any particular word or group of words from any
directory input text file, which in other words known as GREP
Grep stands for Global regular expression print
As the name implies, Grep is used to search text files with regular expressions
It prints the lines or word matching the given pattern in a text file.
'''
import re
# class is created for declaring the function 'occur' with its variables


class word_class:
    # occur func will return the no. of occurance of any word input by user
    def occur(self, word_search, file_string):
        self.word_search = word_search
        self.file_string = file_string
        # finding the times of occurance of the word given
        occ = re.findall(self.word_search, self.file_string, re.M | re.I)
        print("Total no.of "+self.word_search+" in text file is: ", len(occ))
        return (len(occ))
# func for printing the string of 3 words,before and after the word to be found


def word_string(length_occurance):
    f_search = []
    final_output.write(str(length_occurance)+"\n")
    l_file = file_string.split("\n")  # txt file converted to list by split
    for i in range(len(l_file)):
        line = (l_file[i])  # taking elements as str for comparing word_search
        if re.search(word_search, line, re.M | re.I):
            # lines which contain the word_search gets appended in this list
            f_search.append((line.split('\n')))
    for i in range(len(f_search)):
        l_string = (" ".join(f_search[i]))
        # split func will return list of the line which contain the word_search

        def split():
            list_string_split = l_string.split(" ")
            return list_string_split
        for k in range(len(split())):
            if re.search(word_search, split()[k], re.M | re.I):
                if k == 0:
                    op_str = (split()[k] + " " + split()[k+1])
                    final_output.write(op_str + '\n')
                elif k == len(split())-1:
                    op_str = (split()[k-1] + " " + split()[k])
                    final_output.write(op_str + '\n')
                else:
                    op_str = (split()[k-1] + " " + split()[k] +
                              " " + split()[k+1])
                    final_output.write(op_str + '\n')


if __name__ == '__main__':
    file_open = open(r"input.txt")  # opened file and read it in a handler
    file_string = file_open.read()  # file is converted to string
    const = int(input("total words to be searched: "))
    for m in range(const):
        # taken input for the word to be searched
        word_search = input("Enter the word you want to search\n")
        out_file_name = word_search+'.txt'
        obj = word_class()
        final_output = open(out_file_name, "w")  # writing final output in txt
        var = obj.occur(word_search, file_string)
        word_string(var)
        final_output.close()
    file_open.close()
