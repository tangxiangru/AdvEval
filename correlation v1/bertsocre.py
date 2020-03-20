from bert_score import score
import os
import xlwt
import sys
def load_data(path):
    lines = []
    with open(path, 'r') as f:
        for line in f.readlines():
            l = line.strip()
            lines.append(l)
    return lines

#data = ["mr","yelp","snli","alldata"]
data=["alldata"]
scores={'bertp':[],'bertr':[],'bertf':[]}
metrics=['bertp','bertr','bertf']
for each in data:
    references = load_data("/home/txr/AdvEval/"+each+"-ref.txt")
    translations = load_data("/home/txr/AdvEval/"+each+"-out.txt")
    cands = []
    refs = []
    for k in range(len(references)):
        cands.append(translations[k])
        refs.append(references[k])
        (P, R, F), hashname = score(cands, refs, lang='en', return_hash=True)
        print(f'{hashname}: P={P.mean().item():.6f} R={R.mean().item():.6f} F={F.mean().item():.6f}')

        scores["bertp"].append(P.mean().item())
        scores["bertr"].append(R.mean().item())
        scores["bertf"].append(F.mean().item())

    
    for met in metrics:
        f = xlwt.Workbook()
        sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
        j = 0
        for i in scores[met]:
            sheet1.write(j,0,i)
            j=j+1
        f.save('/home/txr/AdvEval/'+each+'-'+met+'.xls')
