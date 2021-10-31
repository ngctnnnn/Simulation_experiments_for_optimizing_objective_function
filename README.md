<div align='center'>

## Simulation experiments for optimizing objective function
</div>

### Table of contents
1. [Prerequisites](#1-prerequisites)
2. [Introduction](#2-introduction-to-objective-function-for-optimization)
3. [Differential Evolution](#3-differential-evolution)
4. [Evolution Strategies](#4-evolution-strategies)
5. [Cross Entropy Method](#5-cross-entropy-method)
6. [Improved Cross Entropy Method](#6-improved-cross-entropy-method)

---

### 1. Prerequisites
```python
pip install -r requirements.txt
```

### 2. Introduction to objective function for optimization
#### a. Sphere function:
<div align='center'>
  
<img width="133" alt="Screen Shot 2021-10-26 at 19 59 54" src="https://user-images.githubusercontent.com/67086934/138883823-646e129f-168b-4a20-a286-fae0d673844b.png">
  
</div>
  
<div align='center'>
  
<img width="514" alt="Screen Shot 2021-10-26 at 19 59 06" src="https://user-images.githubusercontent.com/67086934/138883678-8c647118-8a43-4eb6-a3c1-4592fdcdf1ab.png">
  
 </div>
 
 #### b. Rosenbrock function
 
 <div align='center'>
<img width="293" alt="Screen Shot 2021-10-26 at 20 01 39" src="https://user-images.githubusercontent.com/67086934/138884188-7acac563-8764-4c7d-8249-aaa352ccd3e3.png">
  
 </div>
 
<div align='center'>
<img width="531" alt="Screen Shot 2021-10-26 at 20 03 03" src="https://user-images.githubusercontent.com/67086934/138884414-742837fe-eed3-4d63-8c74-bae83846cfe3.png">

</div>

#### c. Rastrigin function

<div align='center'>
  
<img width="272" alt="Screen Shot 2021-10-26 at 20 05 34" src="https://user-images.githubusercontent.com/67086934/138884815-e0ddb048-8d58-4dbd-b45d-d0f4c054021d.png">
</div>
 
<div align='center'>

<img width="501" alt="Screen Shot 2021-10-26 at 20 05 57" src="https://user-images.githubusercontent.com/67086934/138884870-b0e2a9a1-975b-494f-9eae-fbb36a120bda.png">
  
 </div>
 
#### d. Griewank function

<div align='center'>
  
<img width="261" alt="Screen Shot 2021-10-26 at 20 08 12" src="https://user-images.githubusercontent.com/67086934/138885270-94f7df43-4869-468e-b1ff-acd8ca48479f.png">
  
</div>

<div align='center'>
  
  <img width="530" alt="Screen Shot 2021-10-26 at 20 09 18" src="https://user-images.githubusercontent.com/67086934/138885428-0ea7008a-de7e-474c-a5b0-6941cded238a.png">

</div>

#### e. Ackley function

<div align='center'>
  
<img width="475" alt="Screen Shot 2021-10-26 at 20 12 50" src="https://user-images.githubusercontent.com/67086934/138885983-011708e1-4eb9-4521-95fb-a8daec9fd457.png">
  
</div>

<div align='center'>
  
<img width="515" alt="Screen Shot 2021-10-26 at 20 13 46" src="https://user-images.githubusercontent.com/67086934/138886119-0de498c2-5ee1-4030-a272-fe05270c0aad.png">

</div>

### 3. Differential Evolution
#### a. Sphere

<div align='center'> 
  
![Sphere-DE-1024](https://user-images.githubusercontent.com/67086934/138877880-07734cfb-d726-4362-8c21-9e45ccf96e48.gif)
  
</div>

#### b. Rosenbrock

<div align='center'>
  
![Rosenbrock-DE-512](https://user-images.githubusercontent.com/67086934/138877913-ab6a177e-4243-4a46-856a-b4f227002cf4.gif)

</div>
  
#### c. Rastrigin

<div align='center'>
  
![Rastrigin-DE-512](https://user-images.githubusercontent.com/67086934/138878009-0c024160-cc4c-4cb7-a28a-5509243c2c0b.gif)

</div>
  
#### d. Griewank

<div align='center'>

![Griewank-DE-32](https://user-images.githubusercontent.com/67086934/139563649-04af2b63-fe29-4934-8bc7-552236e18982.gif)

</div>

#### e. Ackley

<div align='center'>
  
![Ackley-DE-1024](https://user-images.githubusercontent.com/67086934/138878031-98c096de-9825-4431-b6a2-4c80ede889f7.gif)
  
</div>
  
### 4. Evolution Strategies
#### a. Sphere 

<div align='center'>
  
  ![Sphere-ES-1024](https://user-images.githubusercontent.com/67086934/139563823-17bca9d5-45d3-42ef-bd02-c146b393a236.gif)

</div>

#### b. Rosenbrock

<div align='center'>
  
  ![Rosenbrock-ES-1024](https://user-images.githubusercontent.com/67086934/139563840-fb1b7ae2-080a-4eed-8fef-4c9b0760dc37.gif)

</div>

#### c. Rastrigin

<div align='center'>
  
  ![Rastrigin-ES-1024](https://user-images.githubusercontent.com/67086934/139563844-41ba0ae2-a4f0-419d-a537-f6c947862d86.gif)

</div>

#### d. Griewank

<div align='center'>
  
  ![Griewank-ES-1024](https://user-images.githubusercontent.com/67086934/139563853-6e1fcc40-1a2e-43fa-abe1-bfaa50ad2557.gif)

</div>

#### e. Ackley

<div align='center'>
  
  ![Ackley-ES-1024](https://user-images.githubusercontent.com/67086934/139563858-9245906b-bfcb-49a5-b93a-b0a619921970.gif)

</div>

### 5. Cross Entropy Method
#### a. Sphere

<div align='center'>
  
  ![Sphere-CEM-1024](https://user-images.githubusercontent.com/67086934/139563888-baa68641-3ff3-4d28-aaca-8bcdb33f3ac9.gif)

</div>

#### b. Rosenbrock

<div align='center'>

  ![Rosenbrock-CEM-1024](https://user-images.githubusercontent.com/67086934/139563891-411ccb35-1209-4e2f-91b2-65f5f9526bd7.gif)

</div>

#### c. Rastrigin

<div align='center'>

  ![Rastrigin-CEM-1024](https://user-images.githubusercontent.com/67086934/139563896-6047c11d-9c8c-4704-a733-10485428c6b8.gif)

</div>

#### d. Griewank

<div align='center'>
  
  ![Griewank-CEM-1024](https://user-images.githubusercontent.com/67086934/139563900-a3af7f25-0979-49e7-b122-f162a726e75b.gif)

</div>

#### e. Ackley

<div align='center'>

  ![Ackley-CEM-1024](https://user-images.githubusercontent.com/67086934/139563902-49f5e277-20be-40cc-9639-3dbb914b1441.gif)

</div>

### 6. Improved Cross Entropy Method
#### a. Sphere

<div align='center'>

  ![Sphere-CEMv2-1024](https://user-images.githubusercontent.com/67086934/139563929-e0244073-31c3-48bd-8f90-7b78e5428172.gif)

</div>

#### b. Rosenbrock

<div align='center'>
  
  ![Rosenbrock-CEMv2-1024](https://user-images.githubusercontent.com/67086934/139563931-d19930e5-502f-4e79-af57-2c793e83abe3.gif)

</div>

#### c. Rastrigin

<div align='center'>
  
  ![Rastrigin-CEMv2-1024](https://user-images.githubusercontent.com/67086934/139563932-e8e66c9b-9407-4368-ab5d-84e04cd23110.gif)

</div>

#### d. Griewank

<div align='center'>

  ![Griewank-CEMv2-1024](https://user-images.githubusercontent.com/67086934/139563936-4e899549-9f6a-439d-a0c5-6a430d5ef197.gif)

</div>

#### e. Ackley

<div align='center'>

  ![Ackley-CEMv2-1024](https://user-images.githubusercontent.com/67086934/139563939-d8ddf5a8-7707-49fa-bbe2-bac918b46f9f.gif)

</div>
