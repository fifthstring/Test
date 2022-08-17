
def lex():
    toks = []
    newtoks = []
    var = {}
    f = open('stuff.txt','r')
    for i in f:
        toks.append(i)
        
        

    for i in toks:
        if ' ' in i:
            x = i.index(' ')
            y = i[0:x]
            a = len(i)-1
            z = i[x+1:a]
            newtoks.append([y,z])

            

    for i in newtoks:
        
        for k in range(len(i)):
            if('=' in i[k-1]):
                i[k-1] = i[k-1].replace('=','')
                if ' ' in i[k-1]:
                    i[k-1] = i[k-1].replace(' ','')



        if(i[0] == 'say'):
            p = i[1]
           
            if p in var:
                p= var.get(p)
                        
            print(p)
        
        
        
            


        if('ask' in i[1]):
            i[1] = i[1].replace('ask','')
            i[1] = input(i[1])
            var[i[0]] = i[1]

        if('var' in i[0]):
            i[0] = i[0].replace('var','')
            var[i[0]] = i[1]

    return newtoks


f = open('stuff.txt','r')
l = f.readlines()
tokens= lex()





# IT'S GOING TO RUN THE CODE THAT'S ON ONE OF THE FILES

# \/ THIS IS THE FILE IT IS RUNNING  \/


fp = 'stuff.txt'
the = 99
'''
while the not in ('yes','no'):
  the = input('Remove the words (the that and to) as printables? So you can use them in your code, yes or no?')
'''

the = 'no'
# Try going on the file!


import random
import sys
import os
import time


class lang():
    def lex(self):
        self.arrvars = []
        #global isbreak
        self.lasttrue = False
        global x
        self.arr = []
        self.ifdict = {}
        self.isbreak = False
        global loopnumbs
        global loopnumbcount
        global loopcoords
        #multip = 0
        #ltoks = []
        #loopnumcbount = 0
        self.loopnumbs = []
        loopcoords = []
        self.counts = 0
        self.functionnames = []
        isbreak = False
        global ifs
        global var
        global toks
        global newtoks
        toks = []
        newtoks = []
        var = {}
        ifs = []
        f = open(fp, 'r')
        for i in f:
            toks.append(i)
          
        for i in toks:
            if ' ' in i:
                x = i.index(' ')
                y = i[0:x]
                a = len(i) - 1
                z = i[x + 1:a]
                newtoks.append([y, z])

        #for i in range(multip):

        workn = list(newtoks)

        #print(workn)
        #print(loopcoords)
        v = 0
        for i in newtoks:
            #print('v',v)
            #print(i)

            #print('l',loopcoords)
            if 'loop' == i[0]:
                v += 1
                loopcoords.append(workn.index(i) + v)
                workn.remove(i)
                self.loopnumbs.append(1)
                try:
                    self.loopnumbs.append(int(i[1]))
                except:
                    self.loopnumbs.append(i[1])

            elif 'end' == i[0] and 'loop' == i[1]:

                v += 1
                loopcoords.append(workn.index(i) + v)

                workn.remove(i)

        loopcoords.append(len(newtoks))
        #from numpy import array

        for i in range(len(loopcoords)):
            if loopcoords[i] > 0:
                loopcoords[i] -= 1
        ''' 
      print('LL',loopcoords)
      print('LN',loopnumbs)
      '''
        return newtoks

    def check(self):
        tem = []
        for i in self.loopnumbs:
            #print(i)
            if i in var:
                tem.append(int(var.get(i)))
            else:
                tem.append(i)
        #print(tem)
        self.loopnumbs = tem

    def brek(self, i):
        #print(i)
        if i[0] == 'exit':
            sys.exit('You stopped the code!')

        if i[0] == 'sleep':
            try:
              try:
                  time.sleep(int(i[1]))
              except:
                  c = var.get(i[1])
                  time.sleep(int(c))
            except:
              sys.exit('Um... You have either misspelled a variable or are trying to sleep something other than a number')
        if i[0] == 'clear':
            os.system('clear')

    def endloopif(self, i):
        #print('i0',i)

        if 'stop' == i[0]:
            self.isbreak = True
        else:
            #self.isbreak = False
            pass

    def endloop(self, i):

        if i[0] == 'stop':
            return True

    def math(self, i):
        if i[0] == 'do' or i[0] == 'math' or i[0] == 'solve' or i[0] == 'sum':
            #print(i)
            t = i[1]
            
            isvar1 = False
            isvar2 = False
            #print(t)
            t = t.split(' ')
            #print(t)
            try:
              vv1 = t[0]
              vv2 = t[2]
            except:
              sys.exit("You might be doing something wrong! Look at the do statement, is it executed properly, maybe you're mising a closing token?")
            k = i[1]
            b = var.keys()
            for i in b:
              if i in k:
                k = k.replace(i, var[i])
            
            #print(k)
            ans = eval(k)

            var[t[0]] = ans

    def say(self, i):
        #print(i)
        if (i[0] == 'say' or i[0] == 'display' or i[0] == 'print'
                or i[0] == 'show'):
            j = i
            q = i[1:]
            p = q[0]

            p = p.split(' ')

            
            
            '''
            if p[0] in var:
                p = var.get(p[0])
            '''

            #print('p',p)

            
            for i in p:
              if i in var:
                try:
                  p[p.index(i)] = int(var[i])
                except:
                  p[p.index(i)] = (var[i])
            
            c = False
            #print(p)
            k = q[0]
            for i in q[0]:


              if i in ('+','-','*','/'):
                c = True
              
            

            #if type(p) == list:
            if c == True:
              k = ''
              for i in p:
                k += (str(i) +' ')
              print(eval(k))


            #print(j[1])
            if j[1].split()[0] == 'choice':
              ch = random.choice(var[j[1].split(' ')[-1]])
              if ch == int(ch):
                print(int(ch))
              else:
                print(ch)

            else:


              for i in p:
                x = str(i)
                print(x.replace('^',''), end=' ')
              print('')
            '''
            else:
                p = str(p)
                #print(p[-1])
                p = p.replace('.0', '')
                print(p)
            '''
    
    
    
    def function(self, i):
      
      if 'function' == i[0]:
        self.arrvars.append([])
        self.arr.append([])

        self.f = i[1].split(' ')

        self.arr[self.counts].append(self.f[0])
        self.functionnames.append(self.f[0])

        self.f.remove(self.f[0])
        for l in self.f:
          self.arrvars[self.counts].append(l)
          var[l] = 0

        
        self.arr[self.counts].append(newtoks[newtoks.index(i)+1:newtoks.index([self.arr[self.counts][0],'end'])])
        #print('arr',self.arr)

        self.counts += 1



      if i[0] == 'call':
        w = i[1].split(' ')
        #print(w)
        count = 0
        if w[0] in self.functionnames:
          for i in self.arrvars[self.functionnames.index(w[0])]:
            count += 1
            if str(w[count]) in var:
              var[i] = var.get(str(w[count]))
            else:
              var[i] = str(w[count])
          
          #print('WORKS')
          x = self.arr[self.functionnames.index(w[0])][1:]
          x= x[0]
          #print('0',x)
          for i in range(len(x)):
            x[i][0] = x[i][0].replace('.','')
            #print(x[i])
        #print('x',x)
        #print('x',x)
        lc = []
        ln = []
        for i in x:
          #print(i)
          
          #print(i)
          if i[0] == 'loop':
            lcode = self.arr[self.functionnames.index(w[0])]
            #print('Loop',lcode[1])
            for j in lcode[1]:
              #print(j)
              if j[0] == 'loop':
                lc.append(lcode[1].index(j))
                ln.append(int(j[1]))
          
              if j[0] == 'stop':
                lc.append(lcode[1].index(j))

          
          print(lc,ln)
          #print(i)
          self.check()
          self.brek(i)
          self.endloopif(i)
          self.math(i)
          self.ask(i)
          self.say(i)
          self.function(i)
          self.varss(i)
          self.ifstuff(i)
            



            

    def ask(self, i):
        
        w = i[1].split(' ')
        #print(w)
        try:
          w.remove('=')
        except:
          pass

        if ('ask' == w[0] or 'input' == w[0] or 'question' == w[0]):
            '''
          if 'ask' in i[1]:
              i[1] = i[1].replace('ask', '')
          if 'input' in i[1]:
              i[1] = i[1].replace('input', '')
          if 'question' in i[1]:
              i[1] = i[1].replace('question', '')
          
          #if ' ' == i[1][0]:
            #i[1] = i[1].replace(' ','',1)
          
          '''

            message = i[1]
            
            try:
                message = message.replace('=','')
            except:
                pass
            try:
                message = message.replace('ask', '')
            except:
                pass
            try:
                message = message.replace('question', '')
            except:
                pass
            try:
                message = message.replace('input', '')
            except:
                pass

            if message[0] == ' ':
                message = message.replace(' ', '', 1)
            
            if message[1] == ' ':
                message = message.replace(' ', '', 1)
            xc = input(message).lower()
            #print('XX',newtoks[newtoks.index(i)][1])
            #newtoks[newtoks.index(i)][1] += 'ask'
            var[i[0]] = xc

    def varss(self, i):
        j = i
        q = i[1].split(' ')
        #print(q)
        if '=' in q:
            q.remove('=')
        if ('var' == i[0] or '=' == i[0]):
            if 'randnum' in q:
                var[q[0]] = random.randint(int(q[2]), int(q[3]))

            elif 'do' in q:
                s = q
                q = i[1][i[1].index('do'):]
                #print(q)

                c = q.replace('do ','')
                if c[0] == ' ':
                  c= c[1:]

                l = var.keys()
                for i in c.split():

                  if i in l:
                    c=c.replace(i,var[i])



                #print(c)
                var[s[0]] = eval(c)

            

            elif 'choice' in q:
              #print(q,j[1])
              ch = random.choice(var[j[1].split(' ')[-1]])
              if ch == int(ch):
                var[q[0]] = (int(ch))
              else:
                var[q[0]] = (ch)

            else:
                if q[1] in var:
                    b = var.get(q[1])
                else:
                    b = ''
                    xx = q[1:]

                    for i in xx:
                        b += i

                var[q[0]] = b


        if ('list' == i[0] or '=' == i[0]):
            w = i[1].split(' ')
            slave = i[1].split(',')
            slave[0]=slave[0].replace(w[0],'')
            #print(slave)
            v = w[0]
            var[v] = []
            for q in slave:
              #print(q)
              
              if 'randnum' in q:
                  b = random.randint(int(q[2]), int(q[3]))
              elif 'choice' in q:
                #print(q,7,j[1])
                ch = random.choice(var[q.split(' ')[-1]])
                if ch == int(ch):
                  b = (int(ch))
                else:
                  b = (ch)
              elif 'do' in q:


                #print(q)
                c = q.replace('do ','')
                if c[0] == ' ':
                  c= c[1:]

                l = var.keys()
                for i in c.split():

                  if i in l:
                    c=c.replace(i,var[i])



                #print(c)
                b= eval(c)
                  

              else:
                #print('q',q)
                h = q
                if h[0] == ' ':
                  h = h[1:]
                if h in var:
                    b = var.get(h)
                
                      



                else:
                    b = ''
                    xx = q

                    for i in xx:
                        b += i
              try:
                if b[0] == ' ':
                  b = b[1:]
              except:
                pass
              try:b = float(b)
              except: pass
              var[v].append(b)

    def ifstuff(self, i):
        #print(i)
        try:
            p = i
            for i in p[1].split(' '):
              if i in var:
                p[1] = p[1].replace(i,var[i])


            self.t= t = p
            iftok = p[1]
            ciftok = iftok
            c = iftok.split(' ')
        except:

            pass
        
        
        if ('if' in p[0]):
            
         
            #print('h')
            num = p[0][-1]
            #print(num)
            #print(c)
            whattodo = []
            for i in c:
                if  i in ('say','do','var','talk'):
                    whattodo = c[c.index(i):]
                    iftok = c[:c.index(i)]


                    break
                elif i in ('ask','input'):
                  whattodo = c[c.index(i)-1:]
                  break


            
            #print('wh',whattodo)
            #print(iftok)
            ift = ''
            for i in iftok:
                ift += (i)
                ift += (' ')
            #print(ift)
            l = []
            for i in ift.split(' '):
              if i=='and' or i=='or':
                l.append(i)

            #print(l)


            v = ift.split(' and ')
            for i in v:
              if i[-1] == ' ':
                c = v[v.index(i)]
                v[v.index(i)] = c[:-1]

            #print(v)

            for i in v:
              g = i.replace(' ','')
              #print(g)
              if '>' in g:
                #print(9999,g[0:g.index('>')])
                #print(100000,g[g.index('>')+1:])
                if int(g[0:g.index('>')]) > int(g[g.index('>')+1:]):
                  v[v.index(i)] = True
                  self.lasttrue = True
                else:
                  v[v.index(i)] = False


              if  '<' in g:
                if int(g[0:g.index('<')]) < int(g[g.index('<')+1:]):
                  v[v.index(i)] = True
                  self.lasttrue = True
                else:
                  v[v.index(i)] = False


              if '=' in g and '!' not in g:
                #print(9999,g[0:g.index('=')])
                #print(100000,g[g.index('=')+1:])
                if str(g[0:g.index('=')]) == str(g[g.index('=')+1:]):
                  #print(2)
                  v[v.index(i)] = True
                  self.lasttrue = True
                else:
                  #print(1)
                  v[v.index(i)] = False
              #print(g)

              if '!=' in g:
                #print(v)
                #print(9999,g[0:g.index('!=')])
                #print(100000,g[g.index('!=')+2:])
                if str(g[0:g.index('!=')]) != str(g[g.index('!=')+2:]):
                  v[v.index(i)] = True
                  self.lasttrue = True
                else:
                  #print('y')
                  v[v.index(i)] = False


            h = []
            #print('ihope',v)
            #print(2,l)
            cx = 0
            cy = 1
            cb = 0
            if len(v) > 1:
              for i in range(len(v)-1):

                if l[cb] == 'and':
                  if v[cx] and v[cy]:
                    h.append(True)
                  else:
                    h.append(False)

                if l[cb] == 'or':
                  if v[cx] or v[cy]:
                    h.append(True)
                  else:
                    h.append(False)
                

                cx+= 1
                cy+=1
                cb+=1
            else:

              h = v
                  

            #print('WH',whattodo)
            #print('Final',h)
            #print(t[1])
            b = ift
            if False not in h:
                for i in range(3):
                  whattodo.insert(0,0)
                self.lasttrue = True
                self.dostuff(whattodo)
            else:
                self.lasttrue = False

                
            self.ifdict[str(num)] = self.lasttrue


        elif ('else' in p[0]):
          nu = p[0][-1]
          #print(self.lasttrue)
          #print('We did it bois')
          if self.ifdict[str(nu)] == False:
            b = ciftok.split(' ')
            b.insert(0,'5')
            b.insert(1,'5')
            b.insert(2,'5')
            #print(b)
            self.dostuff(b)

        else:

            pass
    
  
    def list(self,i):

      #print(i)
      pass

    def dostuff(self, iftok):
        #print(iftok)
        iftok = iftok[3:]
        iftoks = []
        #print(iftok)
        andcount = iftok.count('and')
        loc = [0]
        for i in range(andcount):
          loc.append(iftok.index('and'))
          iftok.remove('and')
        loc.append(len(iftok))


        a = 0
        b = 1
        #print('LOC',loc)
        for i in range(len(loc)):
          try:
            iftoks.append(iftok[loc[a]:loc[b]])
          except:
            pass
          
          a+=1
          b+=1

        print('SPLIT',iftoks)

        #print(iftok)
        todo = []
        
        for i in iftoks:
          temp = []
          temp.append(i[0])
          xy = i[1:]
          msg = ''
          for i in xy:
            msg += (i)
            msg += ' '

          temp.append(msg)
          
          iftok = temp
          
          todo.append(temp)

        #print('Todo',todo)
        #print(todo)
        for iftok in todo:
          self.endloopif(iftok)
          self.check()
          self.brek(iftok)
          self.math(iftok)
          self.say(iftok)
          self.ask(iftok)
          self.varss(iftok)
          self.ifstuff(iftok)
          self.list(iftok)
          self.function(iftok)

    def compile(self, newtoks):
        self.x = False
        self.check()
        loopcounter = 0
        count1 = 0
        count2 = -1
        #end = 0
        a = loopcoords[count1]
        b = 0
        self.loopnumbs.append(1)
        #print('LN',loopnumbs)
        for i in range(len(self.loopnumbs)):
            #global x
            

            for i in range(self.loopnumbs[loopcounter]):
                #print(loopnumbs[loopcounter])
                
                                
                if self.isbreak == False:
                  for i in newtoks[b:a + 1]:
                      
                      #print(newtoks[b:a+1])
                      #print(i)
                      

                      if self.isbreak == False:
                        self.check()
                        self.brek(i)
                        self.endloopif(i)
                        self.math(i)
                        self.ask(i)
                        self.say(i)
                        self.function(i)
                        self.varss(i)
                        self.ifstuff(i)
                      
                      #print(end)

            loopcounter += 1
            count1 += 1
            count2 += 1
            if self.isbreak == True:
              self.isbreak = False
                  
            try:
                a = loopcoords[count1]
            except IndexError:
                pass

            try:
                b = loopcoords[count2]
            except:
                pass


pcode = lang()
newtok = pcode.lex()
if the == 'yes':
  for i in newtok:
    #print(i)
    if 'the' in i[1]:
      
      newtoks[newtoks.index(i)][1] = i[1].replace('the','')
      #print('2',newtoks[newtoks.index(i)][1])
    if 'that' in i[1]:
      newtoks[newtoks.index(i)][1] = i[1].replace('that','')
    
    if 'to' in i[1]:
      newtoks[newtoks.index(i)][1] = i[1].replace(' to','')
    if i[1][0] == ' ':
      newtoks[newtoks.index(i)][1] = i[1].replace(' ','',1)
    #print('2', newtoks[newtoks.index(i)][1])

pcode.compile(newtok)



