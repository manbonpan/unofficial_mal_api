import socket
import urllib.request
import re

#Will be removed when converted to object
query = input('Enter Anime Name :').replace(' ','%20')


# Scrapping
with urllib.request.urlopen('https://myanimelist.net/search/all?q='+query) as response:
   html = response.read()
obj=html.decode()

      
def title():
    x= 'class="hoverinfo_trigger fw-b fl-l'
    y = re.finditer(x,obj)
    titles=[]

    for i in y:
        
        sec=''
        a,b=i.span()
        mini=obj[b:]
        j= re.search('>',mini)
        n,m=j.span()
        k=mini[m-1:]
        counter=0
        while True:
           counter+=1
           if k[counter] == '<':
               break
           sec=sec+k[counter]

        titles.append(sec)
    return titles  
def first_res():
    x='class="information di-tc va-t pt4 pl8">'
    y=re.search(x,obj)
    a,b = y.span()
    k=obj[b:]
    counter=0
    sec=''
    f=re.search('"',k)
    a,b=f.span()
    l=k[b-1:]
    while True:
           counter+=1
           if l[counter] == '"':
               break
            
           sec=sec+l[counter]
    return sec
def gettinfo():
    y=first_res()
    with urllib.request.urlopen(y) as response:
        html = response.read()
    obj=html.decode()
    ser='''lazyload" data-src="'''
    y=re.search(ser,obj)
    a,b=y.span()
    counter=0
    n=obj[b-1:]
    img=''
    while True:
           counter+=1
           if n[counter] == '"':
               break
           img+=n[counter]
    ser='''score-label score-8">'''
    y=re.search(ser,obj)
    a,b=y.span()
    scor=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           scor+=n[counter]
    
    ser='''<span class="numbers popularity">Popularity <strong>'''
    y=re.search(ser,obj)
    a,b=y.span()
    popu=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           popu+=n[counter]
            
    ser='''<span class="numbers members">Members <strong>'''
    y=re.search(ser,obj)
    a,b=y.span()
    membah=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           membah+=n[counter]

    
    ser='''type=movie">'''
    y=re.search(ser,obj)
    a,b=y.span()
    types=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           types+=n[counter]

   
    ser='''<span class="information studio author"><a href="'''
    y=re.search(ser,obj)
    a,b=y.span()
    studio=''
    n=obj[b-1:]
    counter=0
    k=re.search('>',n)
    a,b=k.span()
    j=n[b-1:]
    while True:
           counter+=1
           if j[counter] == '<':
               break
           studio+=j[counter]
    
    ser='''<span itemprop="description">'''
    y=re.search(ser,obj)
    a,b=y.span()
    disc=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           disc+=n[counter]
    
    ser='''Background</h2>'''
    y=re.search(ser,obj)
    a,b=y.span()
    back=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           back+=n[counter]
    return back


print(gettinfo())
