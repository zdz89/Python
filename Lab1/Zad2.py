def func(str1,str2):
    set1 = str1.split(' ')
    set2 = str2.split(' ')
    counter = 0
    for word in set1:
        for word2 in set2:
            if word.lower() == word2.lower():
                counter += 1
    print('Prawda') if counter >= 2 else print('Falsz')

func('To jest testowy string do sprawdzenia języka','Nie można sprawdzić języka ponieważ jest to testowy string')
func('To jest testowy string do sprawdzenia języka','Nie można sprawdzić jezyka ponieważ string')
