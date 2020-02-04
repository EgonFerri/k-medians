
# PARAMETERS

# Points
param m; 
set M:={0..m-1};

# Euclidean distances matrix
param D{M,M};

# Clusters
param k;


# VARIABLE

# Belonging matrix-> to which cluster belong point M?
var x{M,M} binary;

# OBJECTIVE FUNCTION

minimize obj: sum{i in M, j in M} D[i,j] * x[i,j];

# CONSTRAINTS
# Every point belongs to one cluster 

subject to c_1 {i in M}: sum{j in M} x[i,j]=1;
 
# Exactly k clusters 
subject to c_2 :sum{j in M} x[j,j]=k;

# A point may belong to a cluster only if the cluster exists
subject to c_3 {i in M, j in M}: x[j,j]>=x[i,j];