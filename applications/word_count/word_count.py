def word_count(s):
    # Your code here

    ignoreThese = '" : ; , . - + = / \ | [ ] { }( ) * ^ &'.split(' ')
    count = {}

    for el in ignoreThese:
        s = s.replace(el, '')

    for word in s.split():
        word = word.lower()

        if word not in count:
            count[word] = 0
        
        count[word] += 1
    
    return count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))