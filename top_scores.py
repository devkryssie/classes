scores = {"alice":85, "bob": 90, "charlie": 78}
top_person = ""
top_score = -1
for person in scores:
    if scores[person] > top_score:
        top_score = scores[person]
        top_person = person
print(top_score)
#average
scores = {"alice":85, "bob": 90, "charlie": 78}
avg = sum(scores.values())/len(scores)
c,m="", "10000"
for p in scores:
    d=scores[p]-avg
    if d<0:d=-d
    if d<int(m):m,c=d,p
print(c)
