#Busy Beaver II
def str_list(a):
       b =[]
       for i in range(len(a)):
          c = a[i]
          b.append (str(c))
       return b
R,r =  1,1
L,l = -1,-1
HALT, Halt, halt = -2,-2,-2
tape = [0,0,1,0,1,1,1,0,0,0,1,1,0,1,0,0,0,0]
program = (([R,0,0],[R,1,1]),
           ([R,0,1],[L,0,2]),
           ([R,1,3],[halt,1,1]),
           ([R,0,4],[L,0,2]),
           ([halt,0,0],[L,0,2]))
#((<direction to move>,<to print>,<new state>))
done = 0
state = 0
pointer = 0
while done == 0:
    data = tape[pointer]
    stateTemp = program[state][data]
    state = stateTemp[2]

    if state == -2:                     #Halt sequence
        print 'HALT'
        done = 1
    else:    
        printList = str_list(tape)
        
        tape[pointer] = stateTemp[1]
        stateTemp2 = str(stateTemp[1])
        stateTemp2 = '[' + stateTemp2 + ']' 
        printList[pointer] = stateTemp2
        
        pointer = pointer + stateTemp[0]
    
        
    
        if pointer == -1:               #Extensision of tape
            tape.append(0)
            for i in range (len(tape)-1):
                t = len(tape)-(i+1)
                tape[t] = tape[t-1]
            pointer = 0
            tape[0] = 0
        if pointer > (len(tape) -1):
            tape.append(0)
        go = raw_input()
        printList = ''.join(printList)
        print printList
    
    

