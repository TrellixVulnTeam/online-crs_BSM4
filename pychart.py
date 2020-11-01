#piechart

import matplotlib.pyplot as plt
slices=[6,2,2,14]
activities=['playing','eating','working','sleeping']
colos=['c','r','b','m']
plt.pie(slices,
labels=activities,
colors=colos,
shadow=True,
explode=(0,0.1,0.2,0),
autopct='%1.2f%%')
plt.title("My daily routine")
plt.show()