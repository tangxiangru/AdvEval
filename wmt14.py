#encoding='utf-8'
import numpy as np

import tqdm
import pandas as pd
huamn_data=np.loadtxt("sim_score.csv",delimiter=",")

def eval_by_kendall(human,scores,k):
    concordant=0
    discordant=0
    tie=0
    maximum=149
    for i in range(0,149):
        for j in range(i,maximum):
            score_diff=scores[i]-scores[j]
            #for k in range(0,9):
            human_diff=human[i,k]-human[j,k]
            if human_diff == 0:
                continue
            if scores == 0:
                tie +=1
            else:
                concordant += int(score_diff * human_diff > 0)
                discordant += int(score_diff * human_diff < 0)
#    print("concordant:", concordant)
#    print("discordant:", discordant)
    corr=(concordant-discordant) / (concordant+discordant+tie)
    print(" %.3f" % corr)
    return corr

metrics=["Bleu_1","Bleu_2","Bleu_3","Bleu_4","EmbeddingAverageCosineSimilairty","EmbeddingAverageCosineSimilarity","GreedyMatchingScore","METEOR","ROUGE_L","VectorExtremaCosineSimilarity","bertf","bertp","bertr","chrf","chrp","chrr","mover"]

for each in metrics:
    print(each)
    df = pd.read_excel("alldata-"+each+".xls",header=None)
    df_li = df.values.tolist()
    result = []
    for s_li in df_li:
        result.append(s_li[0])
    for k in range(0,9):
        eval_by_kendall(huamn_data,result,k)
