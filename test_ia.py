import pickle
import ia

file = open("./ia/ia1__1_5_3_1.0", "rb")
morpion_load = pickle.load(file)


def saisir_tuple(lastTuple):
    t = lastTuple
    c = input()
    t = t + (int(c),)
    return t

tup=()
while True:
    nextTup=ia.next_action(morpion_load,tup)
    print(morpion_load.policy[tup])
    print(nextTup)
    tup = saisir_tuple(nextTup)

