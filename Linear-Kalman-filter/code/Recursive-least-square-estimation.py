import numpy as np

def CalculateRecursiveLeastSquaresSolution(Xmatrix, Pmatrix, Hmatrix, Rmatrix, Ymatrix):
    """
    Updates the state estimate and covariance matrix using Recursive Least Squares.
    """
    # 1. Ensure inputs are numpy arrays (if not already)
    # Note: DO NOT set Xmatrix = [] or Pmatrix = [] here, 
    # as it wipes out the data passed into the function.
    P = np.array(Pmatrix)
    X = np.array(Xmatrix)
    H = np.array(Hmatrix)
    R = np.array(Rmatrix)
    Y = np.array(Ymatrix)

    # 2. Calculate the Kalman Gain (K)
    # K = P * H^T * inv(H * P * H^T + R)
    Ht = np.transpose(H)
    PHt = np.matmul(P, Ht)
    HPHt = np.matmul(H, PHt)
    S = HPHt + R
    S_inv = np.linalg.inv(S)
    K = np.matmul(PHt, S_inv)
    
    # 3. Update the State Estimate (X)
    # X = X + K * (Y - H * X)
    innovation = Y - np.matmul(H, X)
    X_new = X + np.matmul(K, innovation)
    
    # 4. Update the Covariance Matrix (P)
    # P = (I - K * H) * P
    I = np.eye(P.shape[0])
    P_new = np.matmul((I - np.matmul(K, H)), P)

    return X_new, P_new
  
def CalculateLineOfBestFitSolution(LineParam, LineParamCov, Dataset):
    """
    Prepares matrices for a linear model y = x1*r + x2 and calls RLS.
    Dataset: [y_i, r_i, sigma_squared_i]
    """
    y_i = Dataset[0]
    r_i = Dataset[1]
    sigma2_i = Dataset[2]
    
    # Hmatrix must be 1x2: [[r_i, 1.0]]
    Hmatrix = np.array([[r_i, 1.0]])
    
    # Rmatrix and Ymatrix should be 1x1 matrices for matrix multiplication
    Rmatrix = np.array([[sigma2_i]])
    Ymatrix = np.array([[y_i]])
    
    # Call the update function
    LineParam, LineParamCov = CalculateRecursiveLeastSquaresSolution(
        LineParam, LineParamCov, Hmatrix, Rmatrix, Ymatrix
    )
    
    return LineParam, LineParamCov

# 1. Dataset: (Temperature, RPM, Variance)
Dataset = [(65, 1, 1), 
           (65, 2, 2), 
           (81, 3, 2), 
           (92, 4, 2), 
           (97, 5, 1)]

# 2. Initialize Parameters
# Initial guess for slope (x1) and intercept (x2)
LineParam = np.array([[0.0], [0.0]]) 

# Initial uncertainty: High values (1000) mean "low confidence" in our initial guess
LineParamCov = np.eye(2) * 1000.0

print("Starting RLS Updates...\n")

# 3. Recursive Loop
for i, data in enumerate(Dataset):
    LineParam, LineParamCov = CalculateLineOfBestFitSolution(LineParam, LineParamCov, data)
    print(f"Iteration {i+1}:")
    print(f"  Slope: {LineParam[0][0]:.4f}, Intercept: {LineParam[1][0]:.4f}")

print("\nFinal Line of Best Fit:")
print(f"y = {LineParam[0][0]:.4f} * RPM + {LineParam[1][0]:.4f}")