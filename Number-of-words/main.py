import sys

def WordRepetition(file)->dict[str, int]:
    """
        Calculate the number of word repetitions
    """

    Pool = dict()

    for line in file :
        for w in line.split(' '):
            w = w.strip()

            if not Pool.get(w): 
                Pool[w] = 1 # Create New Word
            else : 
                Pool[w] += 1

    return Pool
# End Function    

def get_file_name()-> str:
    """
    Get the name of the file from the user 
        and ensure its existence
    """

    file_name = input("Enter File Name : ") or 'file.txt'

    try :
        file = open(file_name, 'r')
    except FileNotFoundError:
        print('File Not Found !')
        sys.exit()
    else:
        file.close()

    return file_name
# End Function

def show_data(data:dict)-> None:
    """
        Display the collected data in a table
    """

    head = ['Word', 'Repet']
    space, max_len_word = 28, 28

    print(
        f"{head[0]}{' '*space}{head[1]}",
        '- '*space,
        sep='\n')
    
    for word, repetition in data.items():
        if len(word) >= max_len_word :
            _word = list()

            for i in range(0, len(word), max_len_word):
                _word.append(word[i: i+max_len_word])
            
            word = '\n'.join(_word)
            _space = (space + 5) - (len(_word[-1]))
        else:
            _space = (space + 5) - (len(word))
        
        print(f"{word}{' '*_space}{repetition}")
# End Function


if __name__ == '__main__':
    file_name = get_file_name()
    file = open(file_name, 'r')
    data =  WordRepetition(file)
    show_data(data)


