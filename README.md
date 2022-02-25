# python-circleci
[![LDomadia](https://circleci.com/gh/LDomadia/python-circleci.svg?style=svg)](https://app.circleci.com/pipelines/github/LDomadia/python-circleci?branch=main&filter=all)


### Step 1: Create new repo
### Step 2: Set up CircleCI
This can easily be done through GitHub
1. On GitHub, click on the "Marketplace" tab on the top navigation
2. Search for "CircleCI"
3. Scroll to the bottom and install the integration for FREE! 
    - **You will not be asked to enter credit card information** 
    - If it does not say you can install it for free, you should sign up for the GitHub Education Pack. It's easy to do and you're likely to be approved in a few minutes
4. If integrated correctly, you should be able to see all your repos on CircleCI

<img width="1447" alt="Screen Shot 2022-02-25 at 1 03 23 PM" src="https://user-images.githubusercontent.com/62802533/155765105-c647a006-ef55-43ab-8807-773dad1a24bc.png">

### Step 3: Create configuration file
The configuration file should be created at the root of the repo.
1. Create a folder called ".circleci"
2. Inside the folder, create a file called "config.yml"
### Step 4: Create test results directory
When the build is finished running, the test results will be stored in this directory to be viewd on the CircleCI website
1. Create a folder called "test-results" at the root of the repo
2. Inside the folder, create a file called "results.xml"
### Step 5: Edit config.yml file
This is what CircleCI will use to build and run the test cases on the repo. Note that it is important to follow every step precisely, including indentation!
1. Add CircleCI version number: use 2.1
    
    ```
    version: 2.1
    ```
2. Add python orb: Orbs are essentially lines of the config file condensed into one line of code. This makes running the integration [much easier](https://circleci.com/orbs/). You can find pre-made orbs [here](https://circleci.com/developer/orbs).
    
    ```
    orbs: 
        python: circleci/python@2.0.1
    ```
3. Next, we need to create the job that will be used for the workflow we are creating. We'll need to add the following:
    - First, we'll add the job name. This can be whatever you'd like. I'll be calling it **build-and-test**
    - Inside of the job, we need to add the Docker image. A Docker image is a file used to execute code in a Docker container. In this case, this is used to run the job we are creating. You can find pre-made Docker images [here](https://circleci.com/developer/images).
    - After that, we need to add the steps that will be executed when this job runs.
        - The first command is `- checkout`. This is used to locate where in the directory the job will run. By default, `- checkout` is the root of the directory.
        - Next, we need to add the `- run` command. This will run commands in a bash terminal. We'll add commands to install pytest and a command to run the test cases. **If you are using unittest in your test file, it's okay! Pytest will run unittest as well**
        - Finally, we'll upload the test results to the folder we created using the `store_test_results` command.
    
    ```
    jobs:
      build-and-test:
        docker:
          - image: cimg/python:3.10.2
        steps:
          - checkout
          - run: 
              command: |
                pip install pytest
                pytest --junitxml=test-results/junit.xml TestTriangle.py
          - store_test_results:
              path: test-results
     ```
4. The last step is to define the workflow. We'll need to add a workflow name (mine is called **testing_triangles**) and list the job we created below (mine is called **build-and-test**)

    ```
    workflows:
      testing_triangles:
        jobs:
          - build-and-test
    ```
In the end, this is what the config.yml file should look like:
<img width="1095" alt="Screen Shot 2022-02-25 at 1 40 18 PM" src="https://user-images.githubusercontent.com/62802533/155769979-0f343955-87b1-418a-b42d-9d02e6657ff9.png">

### Step 6: Run the build!
First commit and push these changes to GitHub. Then, navigate to the CircleCI website to set up the project.
1. On the repo you're working on, click on "Set Up Project".
2. Since we added the config.yml file, CircleCI should detect it and then you can select the first option **Fastest** to set up the project.
3. Then the workflow should start for the project! Each time a commit is made on the branch, the workflow is automated to start. You'll be able to see all the builds ever made on the repo!
<img width="1447" alt="Screen Shot 2022-02-25 at 1 47 02 PM" src="https://user-images.githubusercontent.com/62802533/155770880-dd787975-091e-46dc-a9f2-0094942e9bde.png">

When you click on the job, you'll be able to go into further detail of the build, including if the test cases passed or failed. 
<img width="1447" alt="Screen Shot 2022-02-25 at 1 48 35 PM" src="https://user-images.githubusercontent.com/62802533/155771071-f6b687c6-35a9-44b2-92d7-228c60536aae.png">

### Step 7 (LAST STEP!) Adding the build badge to the README.md
Finally, you can add the build badge to the repo to indicate whether CircleCI is currently passing or failing. Use this format and replace the **<GITHUB_USERNAME>** and **REPO_NAME** with your own information:

```
[![<GITHUB_USERNAME>](https://circleci.com/gh/<GITHUB_USERNAME>/<REPO_NAME>.svg?style=svg)](https://app.circleci.com/pipelines/github/<GITHUB_USERNAME>/<REPO_NAME>?branch=main&filter=all)
```
