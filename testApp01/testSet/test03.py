__author__ = 'Administrator'


for i in range(1, 4):
    for j in range(1, 10):

        path = 'xml/body/div[5]/div/div/div[' + str(i) + ']/a[' + str(j) + ']/span'
        print(path)
