def spy_game(nums):
    wer = ''
    for x in nums:
        wer += str(x)
    if wer.find('0') != -1:
        qwe =wer.find('0')
        if wer.find('0',qwe,) != -1:
            asd =wer.find('0',qwe,)
            if wer.find('7',asd,) != -1:
                print('True')
            else:
                print('False')


spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])