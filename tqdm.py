from tqdm import tqdm_notebook
list = []
for i in tqdm_notebook(range(10000)):
    list.append(x**x)

print(list)
