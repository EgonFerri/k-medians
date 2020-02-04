def from_euclid_to_ampl(euclid, name, m):
    f= open(name+'.dat',"w+")
    f.write('data;\n') 
    f.write('param m := '+str(m)+';\n')
    f.write('param D :'+' '.join(map(str, range(0,m)))+':=\n')
    for i in range(0,m):
        f.write('\n')
        f.write(str(i)+' ')
        f.write(' '.join(map(str, euclid[i])))
    f.write(';\n')   
    f.write('param k:= 3\n')
    f.write(';\n')     
    f.close() 

def plot_min_st(minimum_spanning, matrix):
    plt.figure(figsize=(15,6))
    sns.scatterplot(data=result,x='sepal_length', y='sepal_width', hue='species', style='species')
    max_1, max_2, max_points_1_i,max_points_1_j,max_points_2_i, max_points_2_j=0,0,0,0,0,0
    for i in range(0,len(minimum_spanning)):
        for j in range(0,len(minimum_spanning)):
            weigth=minimum_spanning[i][j]
            if weigth!=0:
                plt.plot([matrix[i][1], matrix[j][1]],[matrix[i][0], matrix[j][0]], color='black') 
                
def plot_min_st_solution(minimum_spanning, matrix):
    plt.figure(figsize=(15,6))
    sns.scatterplot(data=result,x='sepal_length', y='sepal_width', hue='species', style='species')
    max_1, max_2, max_points_1_i,max_points_1_j,max_points_2_i, max_points_2_j=0,0,0,0,0,0
    for i in range(0,len(minimum_spanning)):
        for j in range(0,len(minimum_spanning)):
            weigth=minimum_spanning[i][j]
            if weigth!=0:
                plt.plot([matrix[i][1], matrix[j][1]],[matrix[i][0], matrix[j][0]], color='black')
                if weigth>max_2:
                    if weigth>max_1:
                        max_2=max_1
                        max_1=weigth                    
                        max_points_2_i=max_points_1_i
                        max_points_2_j=max_points_1_j
                        max_points_1_i=i
                        max_points_1_j=j
                    else:
                        max_2=weigth
                        max_points_2_i=i
                        max_points_2_j=j
    plt.plot([matrix[max_points_1_i][1], matrix[max_points_1_j][1]],[matrix[max_points_1_i][0], matrix[max_points_1_j][0]], color='pink')
    plt.plot([matrix[max_points_2_i][1], matrix[max_points_2_j][1]],[matrix[max_points_2_i][0], matrix[max_points_2_j][0]], color='pink')
    new_graph=minimum_spanning
    new_graph[max_points_1_i][max_points_1_j]=0
    new_graph[max_points_2_i][max_points_2_j]=0
    return(new_graph)

def geometric_mediod(points):
    distance = euclidean

    return(min(map(lambda p1:(p1,sum(map(lambda p2:distance(p1,p2),points))),points), key = lambda x:x[1])[0])

def from_new_graph_to_obj_function(g):
    g=nx.Graph(g)
    total=0
    for component in nx.connected_components(g):
        points=[]
        for c in component:
            points.append([matrix[c]])
            median=geometric_mediod(points)
            summa=0
            for point in points:
                summa+=euclidean(median,point)
        total+=summa
    return(total)