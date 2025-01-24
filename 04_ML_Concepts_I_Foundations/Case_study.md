# ML Case Study I
- Dailin Li 
- 2025-1-24

## What problems are facing the organization?
### 1. The size of the dataset, response biases and inconsistencies could lead to noise in the data, complicating the initial modeling process.
### 2. Post-implementation feedback from districts can be difficult to access and incorporate into the system’s iterative improvement
### 3. Promoting the software to a nationwide scale requires a unbiased data sampling.

## What is the target variable and what type (reg or class) of solution are they developing?
### 1. Target variable: Mathematics recommender software
### 2. Solution: Minimal Viable Product (collaborative filtering/hybrid recommenders) + Exploratory Data Analysis(Discrete cluster sample) 

## How would they know the solution was working (business metric)?
### They could look at how much money was saved and how high the adoption rate of the product was among the schools.

## What other issues might the team be facing?
### 1. Technical issue: the drastic variance among educational priorities, budgets, and cultural factors
### 2. Ethical issue: the over-representation of certain regions while some others being mitigated

## How difficult is the data to gather?
### It initially require heavy reliance on human expertise, with educators and software specialists annotating or validating model outputs to ensure recommendations align with real-world constraints. However, once the machine learning process starts to loop more autonomous survey data will be generated

## Is the target difficult to measure or break into smaller parts?
### Yes. There are a lot of independent casual variables to the results.

## What level of uncertainty (risk) are you willing to accept?
### Moderate level of uncertainty. The lack of sufficient data makes it hard to generate the first model while guaranteeing the accuracy.