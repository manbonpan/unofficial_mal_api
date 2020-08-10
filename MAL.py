import socket
import urllib.request
import re
import time
#Will be removed when converted to object
#query = input('Enter Anime Name :').replace(' ','%20')
initial=time.time()
query='Tokyo%20Ghoul:re'
# Scrapping
with urllib.request.urlopen('https://myanimelist.net/search/all?q='+query) as response:
   html = response.read()
obj=html.decode()

      
def title():
    broadcast=''
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

def new_better():
    returns=[]
##############################################################opening mainpage and getting image#############################################################    
    broadcast=''
    produce=[]
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

    returns.append(img)
######################################################################description of anime##################################################################

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
    returns.append(disc)
#######################################################################anime name in english#####################################################################

    ser='''<span class="dark_text">English:</span>'''
    y=re.search(ser,obj)
    a,b=y.span()
    english=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           english+=n[counter]
    returns.append(english)
##########################################################################alt names for anime####################################################################
    
    if '<span class="dark_text">Synonyms:</span>'in obj:
        ser='''<span class="dark_text">Synonyms:</span>'''
        y=re.search(ser,obj)
        a,b=y.span()
        synonims=''
        n=obj[b-1:]
        counter=0
        while True:
               counter+=1
               if n[counter] == '<':
                   break
               synonims+=n[counter]

    returns.append(synonims)
##########################################################################japanese name##########################################################################

    ser='''<span class="dark_text">Japanese:</span>'''
    y=re.search(ser,obj)
    a,b=y.span()
    jap=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           jap+=n[counter]

    returns.append(jap)
########################################################################type of anime show#######################################################################
    ser='''<span class="information type">'''
    y=re.search(ser,obj)
    a,b=y.span()
        
    
    types=''
    n=obj[b-1:]
    counter=0
    newpattrn='type='
    newt=re.search(newpattrn,n)
    a,b=newt.span()
    n=n[b-1:]
    while True:
           counter+=1
           if n[counter] == '>':
               break
           types+=n[counter]


    returns.append(types)
#######################################################################no of wpisodes############################################################################
    '''ps i think we might encounter issue here coz if it opens a manga page then i think do not have epis but we can fix it later with if stmt XD'''
    ser='''<span class="dark_text">Episodes:</span>'''
    y=re.search(ser,obj)
    a,b=y.span()
    episodes=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           episodes+=n[counter]


    returns.append(episodes)

######################################################################status of completion###########################################################################
    ser='''<span class="dark_text">Status:</span>'''
    y=re.search(ser,obj)
    a,b=y.span()
    status=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           status+=n[counter]


    returns.append(status)
################################################################aired date#########################################################################################
    ser='''<span class="dark_text">Aired:</span>'''
    y=re.search(ser,obj)
    a,b=y.span()
    aired=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           aired+=n[counter]
    returns.append(aired)
###########################################################season info?##########################################################################################
    if "information season" in obj:
        ser='''<span class="information season">'''
        y=re.search(ser,obj)
        a,b=y.span()
            
        
        season=''
        n=obj[b-1:]
        counter=0
        newpattrn='season/'
        newt=re.search(newpattrn,n)
        a,b=newt.span()
        n=n[b-1:]
        while True:
               counter+=1
               if n[counter] == '>':
                   break
               season+=n[counter]
        returns.append(season)


            
##############################################################broadcasted-info###################################################################################
    if '<span class="dark_text">Broadcast:</span>'in obj:
        ser='''<span class="dark_text">Broadcast:</span>'''
        y=re.search(ser,obj)
        a,b=y.span()
        broadcast=''
        n=obj[b-1:]
        counter=0
        while True:
               counter+=1
               if n[counter] == '<':
                   break
               broadcast+=n[counter]

        returns.append(broadcast)
##################################################################liscence info##################################################################################
  

    ser='''<div class="spaceit">
    <span class="dark_text">Licensors:</span>'''
    y=re.search(ser,obj)
    a,b=y.span()
    liscence=''
    n=obj[b-1:]
    new='title='
    food=re.search(new,n)
    a,b=food.span()
    counter=0
    k=n[b-1:]
    while True:
           counter+=1
           if k[counter] == '>':
               break
           liscence+=k[counter]
    
    returns.append(liscence)

#############################################################################authorinfo#########################################################################

    ser='''<span class="information studio author"><a href="'''
    y=re.search(ser,obj)
    a,b=y.span()
    studio=''
    n=obj[b-1:]
    counter=0
    pp=re.search('</a></span>',n)
    q,t=pp.span()
    p=n[:t]
    k=re.finditer('title=',p)
    for i in k:
        a,b=i.span()
        j=p[b-1:]
        while True:
               counter+=1
               if j[counter] == '>':
                   break
               studio+=j[counter]
        returns.append(studio)


#####################################################################sourse for anime########################################################################



    ser='''<span class="dark_text">Source:</span>'''
    y=re.search(ser,obj)
    a,b=y.span()
    source=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           source+=n[counter]


    returns.append(source)

#######################################################################duration######################################################################################

    ser='''<span class="dark_text">Duration:</span>'''
    y=re.search(ser,obj)
    a,b=y.span()
    duration=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           duration+=n[counter]


    returns.append(duration)


############################################################esrb rating##############################################################################################


    ser='''<span class="dark_text">Rating:</span>'''
    y=re.search(ser,obj)
    a,b=y.span()
    esrb=''
    n=obj[b-1:]
    counter=0
    while True:
           counter+=1
           if n[counter] == '<':
               break
           esrb+=n[counter]
    returns.append(esrb)

#############################################################background of studio####################################################################################

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
    returns.append(back)


########################################################score-card###############################################################################################



    ser='''<div class="score-label score'''
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
    returns.append(scor)
#####################################################################popularity index##############################################################################
    
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
    returns.append(popu)
############################################################################members#############################################################################           
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
    returns.append(membah)
########################################################################Generes######################################################################################
    '''ps smol formatting issue we can fix it :D'''



    ser='''<span class="dark_text">Genres:</span>'''
    y=re.search(ser,obj)
    a,b=y.span()
    geners=''
    n=obj[b-1:]
    end=re.search('</div>',n)
    k,l=end.span()
    mp=n[:l]
    mpp=re.finditer('title=',mp)
    for i in mpp:
        a,b=i.span()
        j=mp[a:]
        counter=0
        while True:
               counter+=1
               if j[counter] == '>':
                   break
               geners+=j[counter]

    returns.append(geners)
########################################################################opening theme############################################################################




    if 'Opening Theme' in obj:
        ser='''<div class="theme-songs js-theme-songs opnening">'''
        y=re.search(ser,obj)
        a,b=y.span()
        n=obj[b-1:]
        ser='''</div>'''
        ops=''
        y=re.search(ser,n)
        e,r=y.span()
        n=n[0:r]
        ser='''<span class="theme-song">'''
        y=re.finditer(ser,n)
        for i in y:
            a,b=i.span()
            j=n[a+10:]
            while True:
               counter+=1
               if j[counter] == '<':
                   break
               ops+=j[counter]



        returns.append(ops)
            
            
        
#################################################################################ending themes#####################################################    
        
        if 'Ending Theme' in obj:
            ser='''<div class="theme-songs js-theme-songs ending">'''
            y=re.search(ser,obj)
            a,b=y.span()
            n=obj[b-1:]
            ser='''</div>'''
            eds=''
            y=re.search(ser,n)
            e,r=y.span()
            n=n[0:r]
            ser='''<span class="theme-song">'''
            y=re.finditer(ser,n)
            for i in y:
                a,b=i.span()
                j=n[a+10:]
                while True:
                   counter+=1
                   if j[counter] == '<':
                       break
                   eds+=j[counter]


        returns.append(eds)
        



    
        
    return returns
'''god damn finally or should i say finally:   XDDDDDDDDok lame joke ik'''


print(new_better(),time.time()-initial)
