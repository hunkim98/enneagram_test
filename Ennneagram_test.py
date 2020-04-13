# -- coding: utf-8 --
import numpy as np
import random


def quitgame():
    quiting_message1 = input('F U OK? ')
    exit()


def undefined():
    quiting_message2 = input('이 프로그램은 사용자의 성격유형을 분석하지 못합니다. 전문가와 상담하시길 바랍니다')
    exit()


def output():
    print(tarray)
    print('\n')
    if len(result_list) in (0, 3):
        undefined()
    elif len(result_list) is 1:
        print('당신의 성격유형은 %s입니다' % (type_dict[result_list[0]]))
    elif len(result_list) is 2:
        print('당신의 성격유형은 %s일 수도 있고 %s일 수도 있습니다. 자세한 내용을 위해서는 전문가와 상담해주시길 바랍니다' % (
            type_dict[result_list[0]], type_dict[result_list[1]]))


# let us use dictionary for type output and question input
type_dict = {1: '1번유형(Reformer)', 2: '2번유형(Lover)', 3: '3번유형(Achiever)', 4: '4번유형(Creative Individualist)',
             5: '5번유형(Thinker)', 6: '6번유형(Security Seeker)', 7: '7번유형(Adventurer)', 8: '8번유형(Leader)', 9: '9번유형(Peacemaker)'}

question_dict1 = {'I1': '스스로 화가 많다고 생각하지 않지만, 내 가족이나 친구는 내가 자주 화나있어 보인다고 말한다(본인이 화가 많다고 생각할 경우 이 번호를 선택)',
                  'I2': '평상시에는 사소한 것 하나로 내적으로 분노를 느끼는 일이 없지만, 무슨 일로 분노를 느끼게 되면 속에서 강렬한 분노를 속에서 느끼는 편이다.',
                  'F1': '나는 자존감이 낮을 시기가 가끔 있으며, 타인과의 교류를 통해 자존감이 회복되는 편이다.(굳이 타인과의 교류를 통해 자존감이 회복되지는 않더라도 일단 자존감이 낮을 때가 좀 있는 편이면 이 번호를 선택)',
                  'F2': '상대방과 아무리 가깝다고 해도 내 진정한 자신을 남에게 쉽게 보여주지 않는 것 같다',
                  'T1': '내 마음이 고요하게 가라앉는 일은 별로 없는 편이다. 가끔씩 내 마음이 고요하게 가라앉으면 좋겠다고 생각한다.',
                  'T2': '나는 처음부터 독립적이었다기보다는 시간이 지나 가족이 제공하는 보살핌에서 벗어나면서 독립적이게 변한 것 같다. (태어났을 때부터 독립적이었다고 생각하면 해당사항이 아니다)'}

question_dict2 = {'A1': '어느 모임을 가게 되면 많은 사람들이 나에게 주목하면 심적으로 부담이 조금 되겠지만 그래도 기분이 좋을 것이다.(여러 사람의 주목을 받는 심적 부담이 거기에서 얻는 행복보다 크면 해당사항이 아니다)',
                  'A2': '대개의 경우 나는 내가 원하는 것을 잘 알고 있으며 이를 위해 자기주장을 잘하는 편이다.',
                  'C1': '처음 만나는 사람들과 만나는 자리에서 나는 대화자리를 유쾌하게 만드려고 노력하는 편이다(저절로 대화하는 자리가 유쾌해진다고 생각하면 해당사항이 아니다. 노력한다는 점이 중요하다)',
                  'C2': '친구나 연인 관계에 있어서 저절로 무엇을 하게 되기보다는 무엇을 해야한다는 생각에 어떤 행동을 안하거나 하는 경우가 있다.',
                  'W1': '무엇을 결정하는 모임의 자리에서 내가 정말로 원하는 것이 있다 하더라도 그것들 대부분 내 생각 속에 머무르게 하고 입 밖으로 내뱉지 않는 경향이 있다.',
                  'W2': '나는 처음 보는 사람들이 많은 방에 들어갈 때 겉으로는 어울릴 수 있을지라도 뭔가 동떨어져 있다는 느낌이 드는 편이다.'}

question_dict3 = {'P1': '내가 하는 일이 내 뜻대로 잘 되지 않았을 때 나는 실망감이나 좌절감에 사로잡혀있기보다는 일단 좋은 기분에 머무려고 노력하는 편이다. (문제상황을 긍정적인 방식으로 재구성한다)',
                  'P2': '항상 기분이 좋은 것은 아니지만, 나는 다른 사람들에게 항상 긍정적으로 보이고자 노력한다.',
                  'S1': '어려운 상황이 닥치면 나는 일단 상황을 논리적으로 파악하고 해결하려고 한다.',
                  'S2': '친구들이나 동료들은 내가 일 처리할 때면 내가 차갑다고 말한 적이 있다',
                  'R1': '어떤 일에 대해서 내가 화가 나거나 짜증을 느낄 때 나는 다른 사람들도 나와 같이 느끼고 반응하기를 원한다.',
                  'R2': '문제 상황이 벌어지면 나는 일단 내 감정적인 상태(화, 짜증, 실망)를 먼저 다룰 필요를 느낀다.'}


first_trial = 4


while first_trial > 0:
    starting_question = str(
        input('이 프로그램은 당신의 애니어그램 성격유형을 진단을 하기 위해 만들어졌습니다. 본인의 성격유형을 알고 싶으십니까 (Y/N): '))
    if starting_question in ('Y', 'y'):
        break
    elif starting_question in ('N', 'n'):
        print('Really?')
        first_trial -= 1
    else:
        print('Hmm..')
        first_trial -= 1

if first_trial is 0:
    quitgame()


passing_by = ['프로그램이 성격유형을 정확히 분석할 수 있기 위해서 사용자는 각 질문에 신중히 대답해야 합니다.',
              '질문이 18개 밖에 안되기 때문에 더욱이 신중히 할 것을 당부드립니다.', '그럼 시작하겠습니다']
for items in passing_by:
    str(input(items))

print('\n')
print('\n')


tarray = np.zeros((3, 3))


def getkeybyvalue(question_dict, random_list):
    global list_of_keys
    list_of_keys = []
    question_items = question_dict.items()  # .items() output is a list of tuples
    for randomized in random_list:
        for item in question_items:
            if item[1] == randomized:
                list_of_keys.append(item[0])
            else:
                continue


def interpret_total(x, answer):
    if x is 0:
        interpret1(list_of_keys, answer, x)
    elif x is 1:
        interpret2(list_of_keys, answer, x)
    elif x is 2:
        interpret3(list_of_keys, answer, x)


def interpret1(list, b, row):
    index = b - 1
    if list[index] in ('I1', 'I2'):
        tarray[row, 0] += 1
    elif list[index] in ('F1', 'F2'):
        tarray[row, 1] += 1
    elif list[index] in ('T1', 'T2'):
        tarray[row, 2] += 1


def interpret2(list, b, row):
    index = b - 1
    if list[index] in ('A1', 'A2'):
        tarray[row, 0] += 1
    elif list[index] in ('C1', 'C2'):
        tarray[row, 1] += 1
    elif list[index] in ('W1', 'W2'):
        tarray[row, 2] += 1


def interpret3(list, b, row):
    index = b - 1
    if list[index] in ('P1', 'P2'):
        tarray[row, 0] += 1
    elif list[index] in ('S1', 'S2'):
        tarray[row, 1] += 1
    elif list[index] in ('R1', 'R2'):
        tarray[row, 2] += 1

# this def makes questions and finds keys for each question


def question_input(x, dictionary):
    print('{QUESTIONS}')
    print('\n')
    question_values = list(dictionary.values())
    # random.sample(list, int) returns a list / different from random.shuffle
    randoms = random.sample(question_values, 6)
    for item in randoms:  # for item in question_values 로 바꾸면 순서가 변하지 않는다.
        print('{}. '.format(randoms.index(item) + 1) + item)  # format 표현 기억하기
        print('\n')
    # now list_of_keys has the information of the key of each question
    getkeybyvalue(dictionary, randoms)

    print('\n')
    print("    <<위에 나온 6가지 설명 중, 본인에게 '매우' 해당되는 두가지를 고르시기 바랍니다>>")

    number_input_total(x)


def number_input_total(number):
    possible_number = [1, 2, 3, 4, 5, 6]
    number_input(number, 0, possible_number)
    number_input(number, 1, possible_number)


# https://stackoverflow.com/questions/11904981/local-variable-referenced-before-assignment
def number_input(row, onetwo, newlist):
    chance = 3
    one_two = ['첫', '두']
    while chance > 0:
        answer = int(input('        %s번째 번호: ' % (one_two[onetwo])))
        if answer in newlist:
            interpret_total(row, answer)
            newlist.remove(answer)
            break
        else:
            print('        다시 입력해주시기 바랍니다')
            chance -= 1

    if chance is 0:
        quitgame()


question_input(0, question_dict1)
print('\n')
print('\n')
question_input(1, question_dict2)
print('\n')
print('\n')
question_input(2, question_dict3)
number = 0


position_array = np.where(tarray >= 0)
position_list = list(zip(position_array[0], position_array[1]))
# this is for convenience, each alphabet is a tuple
[I, F, T, A, C, W, P, S, R] = position_list


YY = np.where(tarray == 2)
list_of_YY = list(zip(YY[0], YY[1]))


list_1 = [I, C, S]
list_2 = [F, C, P]
list_3 = [F, A, S]
list_4 = [F, W, R]
list_5 = [T, W, S]
list_6 = [T, C, R]
list_7 = [T, A, P]
list_8 = [I, A, R]
list_9 = [I, W, P]
total_list = [list_1, list_2, list_3, list_4,
              list_5, list_6, list_7, list_8, list_9]


def define_type1():  # this is made for convenience
    print('define_type1')
    global result_list
    result_list = []
    for items in total_list:  # variable that comes before 'in' doesn't seem to need a pre-statement of the variable
        # this is a command used for finding whether list has the same elements
        if set(list_of_YY) == set(items):
            location = total_list.index(items) + 1
            result_list.append(location)


def define_type2():  # 조금 복잡한 function
    print('define_type2')
    global result_list
    result_list = []
    for items in total_list:  # variable that comes before in doesn't seem to need a pre-statement of the variable
        # this is a command used for finding whether items are contained
        if all(elems in list_of_YY for elems in items):
            location = total_list.index(items) + 1
            result_list.append(location)


def find_case():
    global case_list
    case_list = []
    for i in range(0, 3):
        if 2 not in tarray[i, ]:  # not in은 새로 배운 표현이다
            case_list.append(i)
        elif 2 in tarray[i, ]:
            continue


def make_list1(x, y):  # https://www.codingfactory.net/10034 python function 공부하는 데에 큰 도움이 됨
    first_list = (x, y[0][0])  # this is a tuple
    list_findingNY = first_list
    list_of_YY.append(list_findingNY)


def make_list2(x, y):
    first_list = list(zip([x], [y[0][0]]))
    second_list = list(zip([x], [y[0][1]]))
    list_findingNY = first_list + second_list
    list_of_YY.extend(list_findingNY)


if len(list_of_YY) is 3:
    print('there are 3 YYs!')
    define_type1()
    output()


elif len(list_of_YY) is 2:
    print('there are 2 YYs')
    find_case()
    findingNY = np.where(tarray[case_list[0], ] == 1)
    if len(findingNY[0]) is 2:
        make_list2(case_list[0], findingNY)
        define_type2()
    elif len(findingNY[0]) is 1:
        make_list1(case_list[0], findingNY)
        define_type1()
    output()


elif len(list_of_YY) is 1:
    print('there is one YY')
    find_case()
    findingNY1 = np.where(tarray[case_list[0], ] == 1)
    findingNY2 = np.where(tarray[case_list[1], ] == 1)

    if len(findingNY1[0]) is 1 and len(findingNY2[0]) is 1:
        make_list1(case_list[0], findingNY1)
        make_list1(case_list[1], findingNY2)
        define_type1()
        output()
    elif len(findingNY1[0]) is 2 and len(findingNY2[0]) is 1:
        make_list2(case_list[0], findingNY1)
        make_list1(case_list[1], findingNY2)
        define_type2()
        output()
    elif len(findingNY1[0]) is 1 and len(findingNY2[0]) is 2:
        make_list1(case_list[0], findingNY1)
        make_list2(case_list[1], findingNY2)
        define_type2()
        output()
    elif len(findingNY1[0]) is 2 and len(findingNY2[0]) is 2:
        make_list2(case_list[0], findingNY1)
        make_list2(case_list[1], findingNY2)
        define_type2()
        output()


elif len(list_of_YY) is 0:
    print('there are no YYs')
    find_case()
    findingNY1 = np.where(tarray[case_list[0], ] == 1)
    findingNY2 = np.where(tarray[case_list[1], ] == 1)
    findingNY3 = np.where(tarray[case_list[2], ] == 1)

    if len(findingNY1[0]) is 1 and len(findingNY2[0]) is 1 and len(findingNY3[0]) is 1:
        make_list1(case_list[0], findingNY1)
        make_list1(case_list[1], findingNY2)
        make_list1(case_list[2], findingNY3)
        define_type1()
        output()
    elif len(findingNY1[0]) is 2 and len(findingNY2[0]) is 1 and len(findingNY3[0]) is 1:
        make_list2(case_list[0], findingNY1)
        make_list1(case_list[1], findingNY2)
        make_list1(case_list[2], findingNY3)
        define_type2()
        output()
    elif len(findingNY1[0]) is 1 and len(findingNY2[0]) is 2 and len(findingNY3[0]) is 1:
        make_list1(case_list[0], findingNY1)
        make_list2(case_list[1], findingNY2)
        make_list1(case_list[2], findingNY3)
        define_type2()
        output()
    elif len(findingNY1[0]) is 1 and len(findingNY2[0]) is 1 and len(findingNY3[0]) is 2:
        make_list1(case_list[0], findingNY1)
        make_list1(case_list[1], findingNY2)
        make_list2(case_list[2], findingNY3)
        define_type2()
        output()
    elif len(findingNY1[0]) is 2 and len(findingNY2[0]) is 2 and len(findingNY3[0]) is 1:
        make_list2(case_list[0], findingNY1)
        make_list2(case_list[1], findingNY2)
        make_list1(case_list[2], findingNY3)
        define_type2()
        output()
    elif len(findingNY1[0]) is 2 and len(findingNY2[0]) is 1 and len(findingNY3[0]) is 2:
        make_list2(case_list[0], findingNY1)
        make_list1(case_list[1], findingNY2)
        make_list2(case_list[2], findingNY3)
        define_type2()
        output()
    elif len(findingNY1[0]) is 1 and len(findingNY2[0]) is 2 and len(findingNY3[0]) is 2:
        make_list1(case_list[0], findingNY1)
        make_list2(case_list[1], findingNY2)
        make_list2(case_list[2], findingNY3)
        define_type2()
        output()
    elif len(findingNY1[0]) is 2 and len(findingNY2[0]) is 2 and len(findingNY3[0]) is 2:
        make_list2(case_list[0], findingNY1)
        make_list2(case_list[1], findingNY2)
        make_list2(case_list[2], findingNY3)
        define_type2()
        output()
