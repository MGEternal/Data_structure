def search_word(str,word):
    
    word_len = len(word)
    for i in range(len(str)-1):
        j = i+word_len
    
        if j > len(str):
            return -1
        if str[i:j] == word:
            return i
    return -1

word = "helloworld"
input_key ="world"
input_chk = "word"

print(search_word(word,input_chk))
