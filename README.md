# 1. AI Workflow Integration

---

- [1. AI Workflow Integration](#1-ai-workflow-integration)
  - [1.1. Project Brief](#11-project-brief)
  - [1.2. User Stories](#12-user-stories)
    - [1.2.1. End user 1: John McNamara](#121-end-user-1-john-mcnamara)
    - [1.2.2. End user 2: IBM Marketing Team](#122-end-user-2-ibm-marketing-team)
    - [1.2.3. End user 3: IBM Software Developers](#123-end-user-3-ibm-software-developers)
  - [1.3. Deployment Instructions](#13-deployment-instructions)
    - [1.3.1. Requirements](#131-requirements)
      - [1.3.1.1. Development](#1311-development)
      - [1.3.1.2. Deployment](#1312-deployment)
    - [1.3.2. To Deploy](#132-to-deploy)
      - [1.3.2.1. With Kubernetes (Recommended)](#1321-with-kubernetes-recommended)
      - [1.3.2.2. With Docker Compose](#1322-with-docker-compose)

---

##  1.1. Project Brief

"Create a tool which will allow a user to connect a defined set of 3rd party applications and execute actions when conditions have been met e.g. when a tweet containing 'ibm' is detected place content of tweet onto a Google sheet and use Watson tone analyser to determine of tweet was positive or negative on tone. If a positive tweet then place content of tweet onto Google slide."

---

## 1.2. User Stories

In this section we document the 3 main users of such an application.

### 1.2.1. End user 1: John McNamara

As an individual in IBM, John wants to find out what people are saying about the company on Twitter and present his findings. He would like a tool where he can configure actions on a website, where he asks the website to go on Twitter and grab tweets relating to IBM and sends it to the Tone analyser and sort them into different slides. For example, when an IBM customer posts a tweet compaining that the IBM Cloud does not work well sometimes, the application automatically recoginze its tone and put it into the pile of slides where the user is sad.

### 1.2.2. End user 2: IBM Marketing Team

As a part of the IBM marketing team, they'd want to analyse the success of our marketing campains and the public's opinion on IBM products so that we can increase the success of future campains and communicate with our developers over how our products can be improved.

### 1.2.3. End user 3: IBM Software Developers

As a software developer, the team would like to create a bot that replies to user Tweets. Using the application, the developer can use the data collected by the application and stored in the database to train a machine learning model and create an AI chatbot that can reply to tweets, e.g. if a user praised an IBM service, the developer's bot will be able to reply to the user saying thank you.

---

## 1.3. Deployment Instructions

### 1.3.1. Requirements

#### 1.3.1.1. Development

If you are developing this project, you will need to install the following: 

- React [link][2]
- Python 3.8 or above [link][3]
- Docker [link][4]
- Docker Compose [link][5]
- kubectl [link][6]

Ensure that you have the dependencies installed as well once you have cloned and entered the repository:

```sh
cd client && npm install
cd ..
cd server && pip3 install -r requirements.txt
cd ..
```

#### 1.3.1.2. Deployment

If you simply want to run the application, you can just download Docker Desktop and/or Docker + Docker Compose.

### 1.3.2. To Deploy

![beta_app](readme_assets/beta_website.png)

The script creates a Compose network that has two containers -- frontend and backend. The `frontend` container is a React website that will use IBM's NODE-RED library (as requested by the client) in the future. 

For the Beta it displays a website that is created using React, built on [IBM's Carbon Design System][7]. The forms allows you to run a default workflow.

The `backend` container is a python [FastAPI][8] REST application that will be used to interact with a database and act as a portal to other services e.g. the tone analyser and other 3rd party APIs.

There is also a `dongo` container that is the mongoDB database used to store user data. The reason it is called dongo is due to Mitch was thinking docker and mongo together, therefore misspeaking and said the word 'dongo' instead of 'mongo'.

For documentation regarding the `frontend` and `backend`, please consult the [`docs`][9] folder.

#### 1.3.2.1. With Kubernetes (Recommended)

Simply run `./make_kubernetes.sh <context>` in a bash shell and go to http://localhost:8080, the application should run.

You can see what `context`s are available by using `kubectl config get-contexts` and choose one `kubectl config set-context <context>` (We recommend using docker-desktop for development).

#### 1.3.2.2. With Docker Compose

Simply run `./make_compose.sh` in a bash shell and go to http://localost:8080, the application should run.


---

[2]:https://reactjs.org
[3]:https://www.python.org
[4]:https://docs.docker.com/get-docker/
[5]:https://docs.docker.com/compose/install/
[6]:https://kubernetes.io/docs/tasks/tools/
[7]:https://github.com/carbon-design-system/carbon
[8]:https://fastapi.tiangolo.com
[9]:https://github.com/spe-uob/2021-AIWorkflow/tree/main/docs