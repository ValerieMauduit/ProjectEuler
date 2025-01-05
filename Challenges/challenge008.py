# Challenge #8
# Find the thirteen adjacent digits in this 1000-digit number that have the greatest product. What is the value of this
# product?

import os
import sys
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

THOUSAND_DIGITS_NUMBER = (
    '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891' +
    '1294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966489504452445231617' +
    '3185640309871112172238311362229893423380308135336276614282806444486645238749303589072962904915604407723907138105' +
    '1585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522' +
    '4352584907711670556013604839586446706324415722155397536978179778461740649551492908625693219784686224828397224137' +
    '5657056057490261407972968652414535100474821663704844031998900088952434506585412275886668811642717147992444292823' +
    '0863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421' +
    '7506941658960408071984038509624554443629812309878799272442849091888458015616609791913387549920052406368991256071' +
    '76060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
)


def product(number_list):
    if 0 in number_list:
        return 0
    result = 1
    for n in number_list:
        result = result * n
    return result


def sliding_windows(text, count):
    length = len(text)
    number_lists = []
    for i in range(length - count + 1):
        number_lists += [[int(n) for n in text[i:(i + count)]]]
    return number_lists


def max_product(count):
    number_sets = sliding_windows(THOUSAND_DIGITS_NUMBER, count)
    return max([product(numbers) for numbers in number_sets])


def run():
    solution = max_product(13)
    print(f'The solution is: {solution}')
    return solution
