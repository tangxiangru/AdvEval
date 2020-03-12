import os
import xlwt
import sys
from nlgeval import compute_individual_metrics
def load_data(path):
    lines = []
    with open(path, 'r') as f:
        for line in f.readlines():
            l = line.strip()
            lines.append(l)
    return lines


#data = ["mr","yelp","snli","alldata"]
data=["alldata"]
scores={'Bleu_1':[],'Bleu_2':[],'Bleu_3':[],'Bleu_4':[],'METEOR':[],'ROUGE_L':[],'CIDEr':[],'SkipThoughtCS':[],'EmbeddingAverageCosineSimilarity':[],'EmbeddingAverageCosineSimilairty':[],'VectorExtremaCosineSimilarity':[],'GreedyMatchingScore':[]}
metrics=['Bleu_1','Bleu_2','Bleu_3','Bleu_4','METEOR','ROUGE_L','CIDEr','EmbeddingAverageCosineSimilarity','EmbeddingAverageCosineSimilairty','VectorExtremaCosineSimilarity','GreedyMatchingScore']
for each in data:
    references = load_data("/home/lanyanyan/AdvEval/"+each+"-ref.txt")
    translations = load_data("/home/lanyanyan/AdvEval/"+each+"-out.txt")

    for k in range(len(references)):
        metrics_dict = compute_individual_metrics(references[k],translations[k])
        print(metrics_dict)
        for met in metrics:
            scores[met].append(metrics_dict[met])

    for met in metrics:
        f = xlwt.Workbook()
        sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
        j = 0
        for i in scores[met]:
            sheet1.write(j,0,i)
            j=j+1
        f.save('/home/lanyanyan/AdvEval/'+each+'-'+met+'.xls')
                                                                    
