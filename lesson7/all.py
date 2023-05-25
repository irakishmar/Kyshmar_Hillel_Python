
def all_fun(*args) -> bool:
    false_list = [False, ' ', 0, [], {}, None]
    result = True
    for argument in args:
        if argument in false_list:
            result =  False
    return result



case_for_true1 =[True, True, True]
case_for_true2 =[1, 2, 3, 4]
case_for_true3 =['Bart', 'Liza', 'Homer']
case_for_true4 =[1,2,3, ['Tom'], {1: 'Sara'}]
case_for_true5 =[]

case_for_false1 =[True, True, False]
case_for_false2 =[1, 2, 3, 0]
case_for_false3 =['Bart', [], 'Homer']
case_for_false4 =[1,2,3, ['Tom'], {}]
case_for_false5 =[None]

if __name__ == "__main__":
    result_for_true1 = (all_fun(*case_for_true1))
    result_for_true2 = (all_fun(*case_for_true2))
    result_for_true3 = (all_fun(*case_for_true3))
    result_for_true4 = (all_fun(*case_for_true4))
    result_for_true5 = (all_fun(*case_for_true5))

    result_for_false1 = (all_fun(*case_for_false1))
    result_for_false2 = (all_fun(*case_for_false2))
    result_for_false3 = (all_fun(*case_for_false3))
    result_for_false4 = (all_fun(*case_for_false4))
    result_for_false5 = (all_fun(*case_for_false5))

    print(f'For the {case_for_true1} case, the result is {result_for_true1}')
    print(f'For the {case_for_true2} case, the result is {result_for_true2}')
    print(f'For the {case_for_true3} case, the result is {result_for_true3}')
    print(f'For the {case_for_true4} case, the result is {result_for_true4}')
    print(f'For the {case_for_true5} case, the result is {result_for_true5}')

    print(f'For the {case_for_false1} case, the result is {result_for_false1}')
    print(f'For the {case_for_false2} case, the result is {result_for_false2}')
    print(f'For the {case_for_false3} case, the result is {result_for_false3}')
    print(f'For the {case_for_false4} case, the result is {result_for_false4}')
    print(f'For the {case_for_false5} case, the result is {result_for_false5}')


