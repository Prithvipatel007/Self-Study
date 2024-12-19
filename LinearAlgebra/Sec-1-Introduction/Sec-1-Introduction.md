# What is Linear Angebra?

Topics covered :
- Understand what Linear Algebra is
- Learn some adavantages of Linear Algebra
- Know the distinction between Linear Algebra and matrix analysis

Linear Algebra is the branch of Mathematics concernded with vectors and matrices, their Linear combinations and operations acting upon them. Linear algebra has a long history in pure mathematics, in part because it provides a compact notation that is really powerful and general enough to be used in geometry, calculus, differential equations, and many other areas of mathematics. But linear algebra in modern times, has emerged as one of the most important branches of mathematics for computing, for statistics, for data science, for computer graphics and all sort of modern scientific numerical and statistical applications. 

So Linear Algebra is really all about vectors and matrixes and how to use them. A vector is an ordered list of numbers which can be arranged in rows as well as columns as well as matrix. Vectors can also represent functions, for example a function of time. A matrix is a spreadsheet. Now in pure mathematics, you can have infinitely long vectors and matrices with infinite number of rows or columns. 

But nowadays, most people are learning linear algebra because they need it for computer science or programming, data science or physical or biological modelling. So therefore, in this course, we are going to be discussing vectors and matrices that have finite number of rows and columns. Now, vectors and matrices have a algebric interpretation - a list of numbers. And vectors and matrices also have geometric interpretation that provide really powerful insights into the mechanisms of linear algebra. 

In this course, we will try to integrate both the algrbraic and geometric concepts to really facilitate learning the core ideas of linear algebra. One of the really great things about linear algebra is that it provides a compact form for expressing ideas in large datasets. That is why linear algebra is so important for big data. For example, imagine that you have a large dataset containing  time series data from 100 sensors and millions of time points. You can represent that large dataset using a matrix. And you can describe all the linear relationships across all possible pairs of 100 sensors over time using this very simple compact expression. 

 $C = X * X^T$

And if you want to determine whether this large dataset can be characterizeed by a small number of important features, you can use a procedure called eigen decomposition on the covariance matrix. Thats expressed using this formula: 

$CW = WL$

This equation is also called a principal component analysis and its one of the key formulas is dimensionality reduction in Statistics. Another important aspect of linear algebra is Combining vectors or features and matrices in different ways to achieve computational goals. For example, you can use vectors to define axes in a high dimensional space and then use a transformation matrix to wrap datasets or objects or other mathematical structures into and out of these spaces. These is really useful because some kinds of analysis are better done in certain spaces. 

Further more, there is often structure embedded in a high dimensional dataset that is difficult to see in the original dataset, but can be easily extracted using a different kind of dimension reduction technique such as eigen decomposition. 

Matrices can be used to encode translations, rotations or stretching or compressing factors. So its really easy to take an image and compres it, expand it, or rotate it along some axis. 

There is a direct link between linear algebra and geometry, and matrices can be interpreted as descriptions of geometric objects like lines or conics. 

The function that defines this surface is called the normalized quadratic form. It is used to extract key features in the matrix in statistics and in data compression. Ofcourse you will learn all about this particular operation later. 


Linear Algebra : Focus on theory and proof <br />
Matrix Algebra : Focus on applications 


# Linear Algebra Applications

 * See a few real world applications of linear algebra
 * Understand why linear algebra is increasingly important
 * Be super-excited to learn linear algebra!

## First Example

 The first example is data analysis and Big data. First of all, data is typicallay stored as matrices. Most of the analyses performed in statistics and machine learning are represented using vectors and matrices.  These analyses are implemented using Matrix operations, for example, one way to try to understand these structures and the features of a large dataset is to build a model of the data.

 $ s1 = ß1c1 + ß2 $<br />
 $ s2 = ß1c2 + ß2 $<br />
 $ s3 = ß1c3 + ß2 $<br />
 $ s4 = ß1c4 + ß2 $<br />
 $ s5 = ß1c5 + ß2 $<br />

A model is a set of equations that captures what you assume are the underlying dynamics of the important features in the data. The  model is then fit to data by estimating values of free parameters. As mentioned the equations above, these equations are then re-expressed in a mroe compact form using matrices and vectors. The matrix form is given below:

$[s1] = [c1 1] * [ß1 ß2]^T$<br />
$[s2] = [c2 1] * [ß1 ß2]^T$<br />
$[s3] = [c3 1] * [ß1 ß2]^T$<br />
$[s4] = [c4 1] * [ß1 ß2]^T$<br />
$[s5] = [c5 1] * [ß1 ß2]^T$<br />

Here is the matrix equation that represnets this system of equations:<br /><br />
$ y = X*ß $

This system of equations, in other words, the model of data -> The matrix equation is much more compact that the previous set of equations. 

Then, fitting the model to the data involves computing the ß as solution. 

$ ß = inv(X^T*X) * X^T*y $

Here, inv is the inverse of the matrix.

## Second Example

Second example comes from computer graphics. The idea of computer graphics is to have an image that you can move around on the screen. Translations and rotations in 3 dimensions can be implemented by multiplying the coordinates of image by the matrix below: <br /><br />

$\begin{bmatrix} cos(θ) & -sin(θ) & 0 \\ sin(θ) &cos(θ)  &0 \\ 0 & 0 & 1 \end{bmatrix}$

This is called a rotation matrix and its a really compact way and an efficient way to manipulate the location and the prespective of pictures on the screen. Actually, many modern computer graphics applications and algorithms rely on something called quaternions which are vectors containing 4 dimensional complex numbers: <br />

$\begin{bmatrix} a \\ bi \\ cj \\ dk  \end{bmatrix}$

These quarternions are a little bit more computationally efficient, but the principle is exactly the same as the translational and rotational matrix. 

## Example 3: 

A third example is from graph theory. Graph theory is a mathematical framework that is used to understand networks. Graph theory is crucial to a wide range of topics, including air traffic control, the internet, social media and even a brain. Many problems in graph theory can be solved by using matrices to represent the information in the graphs of the nodes and all connectivities across different nodes. Here is an example, some of the core features of the connectivity.

## And so on...

* Linear algebra is used to solve problems in engineering, calculus, differential equations, finance, economics, biology, etc. 
* Linear algebra is a rerequisite for multivariate calculus and differential equations. 
* The compactness and elegance of linear algebra is intrinsically satisfying. 
* The smooth links betweek algrbra and geometric is beautiful. 
* Matrices are so compact and yet they contain so much rich information and the link to geometry is fascinating. 
* Linear algebra is the backbone of most modern computational algorithms, and therefore learning linear algebra will improve your programming skills. 


# Singular Value Decomposition

The goal of singular value decomposition is to take a matrix and decompose that matrix into 3 other matrices. These 3 matrices are basically telling use about important spatial patterns in this image or more generally, important directions in the space in which this matrix lives. In our case, this matrix is basically a picture, then this is going to find patterns in the image that are important. 

# Some advices about this course:

* Take notes by hand! (Not on a keyboard)
* Rewatch the videos or parts of videos
* Solve the practice problems (Several times if you need to!)
* Go through the code and understand the link between theory and implementation.