from sklearn.neighbors import KNeighborsClassifier

 # [height, weight,shoe size]
A =[[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], 
    [190, 90, 47], [175, 64, 39],
    [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

B = ['male', 'male', 'female', 'female', 'male', 'male', 'female',
     'female', 'female', 'male', 'male']

neigh = KNeighborsClassifier(n_neighbors=3)

neigh.fit(A,B)

prediction = neigh.predict([[180,40,120]])

print (prediction)


