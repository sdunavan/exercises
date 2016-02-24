def isWordFind(word, matrix):
    '''word: string, that you'd like to find in the matrix
    matrix: string
    '''
    start = 0 
    result = 0

    for letter in word:
        result = matrix.find(letter, start)
        print('result: ' + str(result) + ' start: ' + str(start))
        if result < 0:
            return 'word not found'  
        start = result + 1   
    
    if result > -1:    
        print('word found')