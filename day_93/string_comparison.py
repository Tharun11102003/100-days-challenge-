"""
Task: String Compression
Problem Statement:
Given an array of characters, compress it in place by modifying the input array. The array should be compressed such that each group of consecutive repeated characters is replaced by the character followed by the number of repetitions. The function should return the new length of the compressed array.

Steps:
    1.Input: ❖ An array of characters, e.g., ["a", "a", "b", "b", "c", "c", "c"].

    2.Process:
       ● Initialization: 
            ❖ Create two indexes: write_index to track where to write the compressed characters and read_index to traverse the array.

       ● Iteration: 
            ❖ Traverse the array using read_index. 
            ❖ For each character in the array:
               ※ Set current_char to the current character being read.
               ※ Initialize a counter count to 0.
               ※ Count the number of consecutive occurrences of current_char.
               ※ Move read_index forward until a different character is encountered.
               ※ Write current_char to the position indicated by write_index.
               ※ Increment write_index.

       ● Compression: 
            ❖ If the count of consecutive characters is greater than 1:
               ※ Convert count to a string.
               ※ Write each digit of the count to the array at the position indicated by write_index.
               ※ Increment write_index for each digit written.

    3.Output: 
        ❖ The function returns the value of write_index, which represents the new length of the compressed array. ❖ The input array is modified in place to reflect the compressed characters up to the write_index
"""



class TextCompressor:
    def compress(self, characters):
        write_index = 0
        read_index = 0

        while read_index < len(characters):
            current_char = characters[read_index]
            count = 0
            while read_index < len(characters) and characters[read_index] == current_char:
                count += 1
                read_index += 1
            characters[write_index] = current_char
            write_index += 1
            if count > 1:
                for c in str(count):
                    characters[write_index] = c
                    write_index += 1

        return write_index

chars = ["a", "a", "b", "b", "c", "c", "c"]
compressor = TextCompressor()
length = compressor.compress(chars)
print(chars[:length])  










#===================================================


