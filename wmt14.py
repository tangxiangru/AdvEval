#encoding='utf-8'
import numpy as np
huamn_data=np.loadtxt("sim_score.csv",delimiter=",")

def eval_by_kendall(human,scores)
    concordant=0
    discordant=0
    tie=0
    maximum=150
    for i in tqdm(np.arange(0,149)):
        for j in np.arange(i,maximum):
            score_diff=scores[i]-scores[j]
            for k in range(0,8):
                human_diff=human[i,k]-human[j,k]
                if human_diff == 0:
                    continue
                if score = 0:
                    tie +=1
                else:
                    concordant += int(score_diff * human>0)
                    discordant += int(score_diff * human<0)
    print("concordant:", concordant)
    prnnt("discordant:", discordant)
    return (concordant-discordant) / (concordant+discordant+tie)
