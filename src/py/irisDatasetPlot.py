'''

'''
import matplotlib.pyplot as plt
from sklearn import datasets
iris=datasets.load_iris()
X_iris, Y_iris=iris.data,iris.target

colors=['red','green', 'blue']
# for i in range(3)
for i in xrange(len(colors)):
    # considero solo i pattern della classe i
    # estraggo le prime due coordinate (0 e 1) 
    # e le plotto utilizzando il colore i-esimo
    
    # bool_etichetteDiInteresse=Y_iris==i
    # x= X_iris[ bool_etichetteDiInteresse , 0 ]
    x, y=X_iris[Y_iris==i,0],X_iris[Y_iris==i,1]
    
    
    #equivalente
    #x=X_iris[:,0][Y_iris==i]
    #y=X_iris[:,1][Y_iris==i]
    
    plt.scatter(x,y,c=colors[i])
    
plt.legend(iris.target_names)
plt.xlabel('Sepal lenght')
plt.ylabel('Sepal width')

plt.show()

