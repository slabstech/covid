---
layout: post
title: EIP2 - Session1
excerpt: "Contents and Assignment from Session1 : EIP2 "
categories: research
tags: [ study ]
modified: 2018-09-22T14:11:53-04:00
---

EIP2 : External Internship Program is a hands-on machine learning course being taught by [The Inkers](inkers.ai) .

The first session was pretty spot on, presented by Rohan Shravan, major takeaway being that ML and CV is progressing at a rapid pace and many concepts have become absolute due to being replaced by efficient algorithms.

* Table of Contents
{:toc}

## Interesting new items heard during the Session

  1. The Bored Cat Experiment
  2. Speech to Image - this was research project 5 years ago.Can be proud of my idea now :P.
  3. Listening to convolution as feature vectors : Video.
  4. gitxiv.com - Papers which also publish source code for validation.
  5. fast.ai - For gathering latest information.
  6. distill.pub -  opensource ML papers : apart from arxiv.org.
  7. The logic behind top-5 , top-1 errors as accuracy in ML papers.

---

## Assignment Questions for Session 1

Write articles on the topics mentioned below between 50-100 words in a markdown format .

1. Convolution
2. Filters/Kernels
3. Epochs
4. 1x1 convolution
5. 3x3 convolution
6. Feature Maps
7. Feature Engineering (older computer vision concept)

Bonus points if you write on any of these:

1. Activation Function
2. How to create an account on GitHub and upload a sample project
3. Receptive Field.
4. 10 examples of use of MathJax in Markdown


---
## Assignment answers

Name : Sachin S Shetty

Batch : 4


1. Convolution

  It is the basic multiplication of matrices , ie. image matrix of size n x m into the kernel/filter matrix of size p X q .
  The result would be a convoluted matrix which would have either
    1.  increase the dimension of the image, for expanding the feature vectors
    2. Decrease the dimension for analysis.


2. Filters/Kernels

    The kernel/filters are one part of the matrix multiplication for convolution . These matrices are generated in random based for required distribution, ie. Gaussian.  The randomness allows the variety of images/features to be clubbed together by backtracking.

3. Epochs

    Epoch is the counter for running the entire convolution & backtracking operation with a reduced set of images.  All the images from the training set are not taken completely in a single run, the images are taken in batches to train and improve the accuracy. In each epoch, multiple operations take place . The accuracy is calculated at end of each epoch and then experiment can either continue or else stop based on accuracy .

4. 1x1 convolution

    Reduces the dimension of the feature map after conolution operation .


5. 3x3 convolution

    Increase the dimensions of the feature maps after the convolution operation .

6. Feature Maps

    Feature maps are the result of convolution operation, i.e the multiplication of feature matrix(images) with the filter/kernels.

7. Feature Engineering (older computer vision concept)

    The earlier standard for solving computer vision problems before the advent of ML/AI, which in part was helped due to cloud computing was  Feature Engineering.

    Feature Engineering techniques like hough transform for detecting lines/circles, sobel filter are still prevalent for basic CV tasks.

    These technique have the feature vectors/calculation hardcoded .ie. the values have been calculated and fixed to solve a particular problem/domain .

Bonus points if you write on any of these:

1. Activation Function

    The activation functions helps to reduce the range of the matrix values/signal values.  The prevailing standard function used in ML/AI is ReLu : Rectified Linear Unit, it rejects the negative values and passes 0 instead.  
    few other functions used earlier were
      1. sigmoid
      2. tanh

2. How to create an account on GitHub and upload a sample project.
    Link to have a personal website is
    [sample_blog](https://sachinsshetty.github.io/sample_website/).


3. Receptive Field.


4. 10 examples of use of MathJax in Markdown
