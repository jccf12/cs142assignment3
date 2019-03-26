import threading

def Parser1(w):

        def qstart(w,s):
            tname = threading.currentThread().getName()
            #print('\t',tname, 'enters state qstart with w=',w, 'and stack =',s)
            s.append('$') #implementation of shorthand notation
            s.append('S')
            qloop(w,s)

        def qloop(w,s):
            tname = threading.currentThread().getName()
            #print('\t',tname, 'enters state qloop with w=',w, 'and stack =',s)
            last = s[-1]

            if last == '$':
                s.pop()
                qaccept(w,s)

            if last == 'S':
                s.pop()
                s.append('C')
                s.append('V')
                s.append('C')
                qloop(w,s)

            if last == 'C':
                s.pop()
                s.append('N')
                s.append('A')
                qloop(w,s)

            if last == 'N':
                for var in ['M','P']:
                    t = threading.Thread(target=qloop, args=[w,s[:-1]+[var]])
                    threads.append(t)
                    t.start()

            if last == 'V':
                for ter in ['<play>','<jump>','<eat>','<kick>','<tell>']:
                    t = threading.Thread(target=qloop, args=[w,s[:-1]+[ter]])
                    threads.append(t)
                    t.start()

            if last == 'A':
                for ter in ['<cool>','<tall>','<blue>', '<tough>', '<ugly>']:
                    t = threading.Thread(target=qloop, args=[w,s[:-1]+[ter]])
                    threads.append(t)
                    t.start()

                t6 = threading.Thread(target=qloop, args=[w,s[:-1]])
                threads.append(t6)
                t6.start()

            if last == 'M':
                for ter in ['<guy>', '<rabbit>', '<Wes>', '<table>', '<pen>','<bike>', '<door>', '<drink>', '<football>', '<riding>']:
                    t = threading.Thread(target=qloop, args=[w,s[:-1]+[ter]])
                    threads.append(t)
                    t.start()


            if last == 'P':
                for ter in ['<I>', '<you>', '<he>', '<she>', '<they>', '<it>']:
                    t = threading.Thread(target=qloop, args=[w,s[:-1]+[ter]])
                    threads.append(t)
                    t.start()

            if w != '':
                if w[0] == '<':
                    if '>' in w:
                        i = w.index('>')
                        c = w[:i+1]
                        if c == last and last in terminals:
                            s.pop()
                            qloop(w[i+1:],s)

        def qaccept(w,s):
            tname = threading.currentThread().getName()
            if w == '':
                tname = threading.currentThread().getName()
                #print('******',tname, 'reached accept state qaccept ***')
                accepting_threads.append(tname)

        terminals = ['<play>', '<jump>', '<eat>', '<kick>','<tell>','<cool>','<tall>','<blue>', '<tough>', '<ugly>', '<guy>', '<rabbit>', '<Wes>', '<table>', '<pen>',
                 '<bike>', '<door>', '<drink>', '<football>', '<riding>', '<I>', '<you>', '<he>', '<she>', '<they>', '<it>']

        accepting_threads = []     
        threads = []

        qstart(w,[])

        for x in threads:
            x.join()

        if accepting_threads:
            print("Parser1 accepts string ",w)

        else:
            print("Parser1 rejects string ",w)

        return bool(accepting_threads)
