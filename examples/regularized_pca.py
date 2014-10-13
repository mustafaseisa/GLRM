from glrm.loss import QuadraticLoss
from glrm.reg import QuadraticReg
from glrm import GLRM
from numpy.random import randn, choice, seed
from numpy import sign
seed(1)

# Generate problem data
m, n, k = 500, 500, 10
eta = 0.1 # noise power
data = randn(m,k).dot(randn(k,n)) + eta*randn(m,n)

# Initialize model
A = data
loss = QuadraticLoss # L = ||XY||_2^2
regX, regY = QuadraticReg(0.1), QuadraticReg(0.1) # r = 0.1 * ||x||_2^2
glrm_pca = GLRM(A, loss, regX, regY, k)

# Fit
print 0.5/abs(data).max()/n
glrm_pca.fit(alpha = 0.5/abs(data).max()/n)

# Results
X, Y = glrm_pca.factors()
A_hat = glrm_pca.predict() # glrm_pca.predict(X, Y) works too; returns decode(XY)
ch = glrm_pca.convergence()
