import threading

def ParseFunc(w):

        def qstart(w,s):
            tname = threading.currentThread().getName()
            # print('\t',tname, 'enters state qstart with w=',w, 'and stack =',s)
            s.append('$') #implementation of shorthand notation
            s.append('S0')
            qloop(w,s,0)

            # w is the string
            # s is the stack
            # D is to keep track of how many "loops" we have done in the grammar
        def qloop(w,s,D):
            tname = threading.currentThread().getName()
            #print('\t',tname, 'enters state qloop with w=',w, 'and stack =',s)
            last = s[-1]
            if D<11: #constraining the "recursion depth of the grammar to avoid infinite threads"

                if last == '$':
                    s.pop()
                    qaccept(w,s)

                if last == 'S0':
                    s.pop()
                    s.append('E')
                    qloop(w,s,D)

                if last == 'E':
                    for var in ['O','E1']:
                        t = threading.Thread(target=qloop, args=[w,s[:-1]+[var],D])
                        threads.append(t)
                        t.start()

                if last == 'O':
                    t = threading.Thread(target=qloop, args=[w,s[:-1]+['E1','o','E1'],D])
                    threads.append(t)
                    t.start()

                if last == 'E1':
                    for var in ['R','F','E']:
                        if var == "E":
                            # when we go back to the variable E, we add 5 to our D
                            t = threading.Thread(target=qloop, args=[w,s[:-1]+[var],D+5]) 
                            threads.append(t)
                            t.start()
                        else:
                            t = threading.Thread(target=qloop, args=[w,s[:-1]+[var],D])
                            threads.append(t)
                            t.start()

                if last == 'F':
                    t = threading.Thread(target=qloop, args=[w,s[:-1]+['E','f'],D])
                    threads.append(t)
                    t.start()
                        
                if last == 'R':
                    for comb in ['KN','KN.K','K.NK','-KN','-KN.K','-K.NK','v']:
                        appnd = list(comb)
                        t = threading.Thread(target=qloop, args=[w,s[:-1]+appnd,D])
                        threads.append(t)
                        t.start()

                if last == 'K':
                    # here we allow for more "loops" so that numbers can be somewhat large
                    t1 = threading.Thread(target=qloop, args=[w,s[:-1]+['K','N'],D+1])
                    threads.append(t1)
                    t1.start()

                    t2 = threading.Thread(target=qloop, args=[w,s[:-1],D])
                    threads.append(t2)
                    t2.start()

                if last == 'N':
                    t = threading.Thread(target=qloop, args=[w,s[:-1]+['d'],D])
                    threads.append(t)
                    t.start()

                if w != '':

                    if w[0] == '(':
                        if ')' in w:
                            j=w.rfind(')')
                            qloop(w[1:j]+w[j+1:],s,D)

                    if w[0] == '-':
                        qloop(w[1:],s,D)

                    if w[0] in ['d','v','o','.']:
                        c = w[0]
                        if c == last:
                            s.pop()
                            qloop(w[1:],s,D)

                    if w[0] == 'f':
                        if '(' in w and ')' in w:
                            j = w.rfind(')')
                            f = w[0]
                            if f == last:
                                s.pop()
                                qloop(w[2:j]+w[j+1:],s,D)


        def qaccept(w,s):
            tname = threading.currentThread().getName()
            if w == '':
                tname = threading.currentThread().getName()
                #print('******',tname, 'reached accept state qaccept ***')
                accepting_threads.append(tname)

        # Checking that the input string is of the form f(x)=... or f(x,y)=...
        # and returning the input without those prefixes for simplicity
        # Note that I only allow for variables x and y and when there's a single variable it has to be x
        def syntax_check(w):
            stripped = "".join(w.split())
            print(stripped)
            if len(stripped)<6:
                print("ParseFunc rejects string ", w)
                return False
            else:
                if stripped[:5]=='f(x)=' and 'y' not in stripped:
                    i = w.index("=")
                    return w[i+1:]
                else:
                    if len(stripped)<8:
                        print("ParseFunc rejects string ",w)
                        return False
                    else:
                        if stripped[:7]=='f(x,y)=':
                            i= w.index("=")
                            return w[i+1:]
                        else:
                            print("ParseFunc rejects string ",w)
                            return False

        # to make the simulator more efficient, all digits were translated into 'd'
        # all operators were translated into "o", checking that "-" actually acts as an operator
        # or else is left as the sign of the number
        def simplify_string(w):
            w = w.strip()
            new = ''
            n =  len(w)
            for i in range(n):
                if w[i] in ['0','1','2','3','4','5','6','7','8','9']:
                    new+='d'
                if w[i]=='-':
                    if i>0:
                        if w[i-1] in ['+','-','*','/','(']:
                            pass
                        else:
                            new+='o'
                    else:
                        pass

                if w[i] in ['+','*','/']:
                    new+='o'
                if w[i] in ['x','y']:
                    new+='v'
                if w[i] in ['(',')','.']:
                    new+=w[i]
                if w[i] == 's' and i<n-4:
                    if w[i:i+3]=='sin' or w[i:i+4]=='sqrt':
                        new+='f'
                if w[i] in ['c','t','l'] and i<n-4:
                    if w[i:i+3] in ['tan','cos','log']:
                        new+='f'
            return new

        accepting_threads = []     
        threads = []

        z1 = syntax_check(w)
        if z1:
            z = simplify_string(z1)
            qstart(z,[])
            for x in threads:
                x.join()

            if accepting_threads:
                print("ParseFunc accepts string ",w, 'translated to ', z)

            else:
                print("ParseFunc rejects string ",w, 'translated to ', z)


            print(len(threads))

            return bool(accepting_threads)

