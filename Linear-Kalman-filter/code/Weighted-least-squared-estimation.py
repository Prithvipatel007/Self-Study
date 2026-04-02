import numpy as np

def CalculateWeightedLeastSquaresSolution(Hmatrix, Rmatrix, Ymatrix):
  # Enter Your Code Here to calculate the least Squares Solution
  Xmatrix = []
  Pmatrix = []

  H = np.array(Hmatrix)
  R = np.array(Rmatrix)
  Y = np.array(Ymatrix)

  Ht = np.transpose(H)
  Rinv = np.linalg.inv(R)
  HtRinv = np.matmul(Ht,Rinv)
  HtRinvH = np.matmul(HtRinv, H)
  HtRinvHinv = np.linalg.inv(HtRinvH)
  HtRinvHinvHt = np.matmul(HtRinvHinv, HtRinv)
  Xmatrix = np.matmul(HtRinvHinvHt, Y)

  Pmatrix = HtRinvHinv

  return Xmatrix.flatten(), Pmatrix
  
def CalculateLineOfBestFitSolution(Dataset):
    n = len(Dataset)

    # Generate the H, R and Y matrices for the Measurement Dataset
    Hmatrix = []
    Rmatrix = np.zeros((n, n))
    Ymatrix = []

    for i, (y,h,r) in enumerate(Dataset):
        Hmatrix.append([h, 1])
        Ymatrix.append([y])
        Rmatrix[i, i] = r**2


    LineParam, LineParamCov = CalculateWeightedLeastSquaresSolution(Hmatrix, Rmatrix, Ymatrix)
    return LineParam

# Example usage:
Dataset = [(65, 1, 1), 
           (65, 2, 2), 
           (81, 3, 2), 
           (92, 4, 2), 
           (97, 5, 1)]

LineParam = CalculateLineOfBestFitSolution(Dataset)
print("Line Parameters (slope, intercept):")
print(LineParam)
