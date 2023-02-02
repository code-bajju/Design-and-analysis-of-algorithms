import os , random

for i in range(30):
    d = str(i) + 'days ago'
    rand = random.randrange(1,30)
    with open('test.txt','a') as file:
        file.write(d+'\n')
    os.system('git add test.txt')
    os.system('git commit --date=" 2023-'+str(1)+'-'+str(rand)+'" -m 1')
os.system('git push -u origin main')

#git commit --amend --no-edit --date="Fri Nov 6 20:00:00 2015 -0600" 
#git fetch origin master
#git rebase origin/master
