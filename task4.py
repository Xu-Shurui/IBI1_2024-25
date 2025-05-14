
'''
input: query sequence, target sequence, seed_length(11 is recommended)
to get all 11 nucleotide "seeds" from query sequence
for-loop: using the seeds to search the target sequence
          if corresponding, to expand on both sides of the seed to get the longest length of the corresponding sequence
                match_length+= corresponding length
the final score = match_length / half of(length of the query sequence+length of the target sequence)
output: the final score 
'''



def compare_mrna(query, target,seed_length):
    query_seeds={}#to initialize the seeds and correlation
    corre=[]
    score=0
    for i in range(len(query)):#to check if the query sequence is an mRNA
        if(query[i]!="A"and query[i]!="U" and query[i]!="G" and query[i]!="C"):
            print ("The query sequence is not an mRNA, because it contains",i, query[i])
            return
    for i in range(len(target)):#to check if the target sequence is an mRNA
        if(target[i]!="A"and target[i]!="U" and target[i]!="G" and target[i]!="C"):
            print ("The query sequence is not an mRNA, because it contains", target[i])
            return
    for i in range(len(query) - seed_length + 1):#to explore and record all possible 11-length seeds
        seed=query[i:i + seed_length]
        if seed in query_seeds:  #if the seed is already in the dictionary, skip it
            continue
        query_seeds[seed] = i  #record as a dictionary
        #print("query_seeds:", query_seeds)    
    for i in range(len(target) - seed_length + 1):#to compare and record corresponding seeds in two sequences
        seed=target[i:i + seed_length]
        if seed in query_seeds:
            corre.append((query_seeds[seed], i))#record as an array
    if len(corre) == 0:  #if no corresponding seeds are found
        print(0)
        return
    for i in range(len(corre)-1):#to extend and calculate the scores
        match=0
        left_query=corre[i][0]
        left_target=corre[i][1]
        right_query=corre[i][0] + seed_length - 1
        right_target=corre[i][1] + seed_length - 1
        while(left_query> corre[i-1][0] + seed_length - 1 and left_target>corre[i-1][1] + seed_length - 1 and query[left_query-1] == target[left_target-1]):
            match+=1
            left_query-=1
            left_target-=1
        while(right_query< corre[i+1][0] and right_target<corre[i+1][1] and query[right_query] == target[right_target]):
            match+=1
            right_query+=1
            right_target+=1
        score+=right_query - left_query +1
        
    #print("query_seeds and their positions:", query_seeds)
    #print("corre:", corre)
    #print("score:", score)
    #print("len(query):", len(query))
    #print("score:",len(corre)/(len(target)-seed_length)*score/((len(query)+len(target))/2))
    #print("corre",len(corre))
    #print(len(query_seeds))
    #print(score)
    score=score/((len(query)-seed_length)*seed_length)
    print("score:", score)
    
#compare_mrna("AUGGCCAUUGUAAUGGCCAUUGUAG", "AUGGCCAUUGUAAUGGCCAUUGUAU", 11)