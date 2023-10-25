This package has been forked from [adamlm/pyransac](https://github.com/adamlm/pyransac). Some modifications have been made to suit my requirements in a university project.  
The following changes have been made:
- Changing line slope calculation to use the furthest away points, rather than the first two in the list. This provides more accurate slope measurements as the first two points in the list could be very close together and not representative of the entire line.
- Added a modified RANSAC algorithm to return the top ten lines found, rather than just the best one.
- Added methods to check the equality of two line models.
- Added an expected slope to the RANSAC algorithm to only generate line models that have a slope similar to what the slope is expected to be.
- Added a conversion from a rise over run slope to an angle in degrees.


# `pyransac` package
This package is a general random sample consensus (RANSAC) framework. For
convenience, some data models (such as a straight line) are already provided.
However, you are free to define your own data models to remove outliers from
arbitrary data sets using arbitrary data models.

# General usage
There are two main components to this package: the RANSAC estimator and a
data model. When calling the estimation function `find_inliers`, you need to
specify the model to which you expect your data to fit.

A data model is class containing the model parameters and an error function 
against which you can test your data. Each data model must implement the
interface defined by the `Model` base class. In other words, you need to
implement the `make_model` and `calc_error` functions.

Additionally, you need to provide parameters for the RANSAC algorithm. These 
parameters are contained in the `RansacParams` class.