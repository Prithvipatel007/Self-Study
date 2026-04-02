import numpy as np

def CalculateLeastSquaresSolution(Hmatrix,Ymatrix):
  # Enter Your Code Here to calculate the least Squares Solution
  Xmatrix = []
  
  H = np.array(Hmatrix)
  Y = np.array(Ymatrix)
  
  Ht = np.transpose(H)
  HtH = np.matmul(Ht, Hmatrix)
  HtHinv = np.linalg.inv(HtH)
  HtHinvHt = np.matmul(HtHinv, Ht)
  
  Xmatrix = np.matmul(HtHinvHt, Y)
  
  return Xmatrix.flatten();
  
def CalculateLineOfBestFitSolution(Dataset):
    # Generate the H and Y matrices for the Measurement Dataset
    Hmatrix = []
    Ymatrix = []
    for(y,h) in Dataset:
        Hmatrix.append([h, 1])
        Ymatrix.append([y])
    
    print("H Matrix:")
    print(Hmatrix)
    print("Y Matrix:")
    print(Ymatrix)
    
    LineParam = CalculateLeastSquaresSolution(Hmatrix, Ymatrix)
    return LineParam


# Example usage:
Dataset = [(65, 1), 
           (65, 2), 
           (81, 3), 
           (92, 4), 
           (97, 5)]

LineParam = CalculateLineOfBestFitSolution(Dataset)
print("Line Parameters (slope, intercept):")
print(LineParam)