# python-circleci
[![LDomadia](https://circleci.com/gh/LDomadia/python-circleci.svg?style=svg)](https://app.circleci.com/pipelines/github/LDomadia/python-circleci?branch=main&filter=all)


### Step 1: Create new repo
### Step 2: Make a folder at the root of the repo called ".circleci"
### Step 3: Inside the folder in Step 2, make a file called "config.yml"
### Step 4: Edit config.yml file
    - add version number of circle ci => `version: 2.1`
    - add orb (this is the language you are using) 
        `orb:`
            `python: circleci/python@2.0.1`
    - define a job (the workflow for the test; we'll call ours "build-and-test")
        `jobs:`
            `build-and-test:`
    - Inside the workflow, you'll need to add a docker image and the steps of the workflow. Follow the example below:
                `docker:`
                    `- image: cimg/python:3.10.2`
                `steps:`
                    `- checkout`
                    `- run: python3 -m unitttest TestTriangle.py`
    - Finally, you need to invoke the workflow you want to run
        `workflows:`
            `sample:`
                `jobs:`
                    `- build-and-test`
### Step 5: Commit and push these changes
