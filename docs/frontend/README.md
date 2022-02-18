## 1. Table of Contents

- [1. AI Workflow Frontend Documentation](#1-ai-workflow-frontend-documentation)
  - [1.1. Table of Contents](#11-table-of-contents)
  - [Wireframes](#wireframes)
    - [Login](#login)
    - [Node Example](#node-example)
  - [Design Iteration](#design-iteration)

---

## 2. Wireframes

This section contains the initial wireframes for the frontend of the AI Workflow.

### 2.1 Login

![login_page](
    wireframes/login_page.png)

### 2.2 Node Example

![example_node](
    wireframes/gs_node.png)

---

## 3. Design Iteration

The wireframes started out as a rough draft of the frontend design. It was more or less the 'end design', what we wanted to achieve.

### 3.1 MVP

For the Minimum Viable Product this was proven to be too difficult, so we ended with a more realistic design.

We also decided to find a framework for the frontend, which we will use for the rest of the project. It was paramount that we had a good framework such that our designs are coherent and we can provide a consistent user experience.

In the end we found [IBM Carbon Design][1], which is THE framework that IBM uses for all their websites -- be it IBM Cloud or the sitemap, all IBM sites uses the same style. It only made sense to use the same framework for our project.

In our main README we now see the current design:

![mvp_app](../../readme_assets/mvp_website.png)

It is a rather simplistic design -- one that simply achieves the sample flow given by the client, but as you may now have realised, the design is consistent with IBM Design Principles and we can use that structure to continue building our website.

### 3.2 Beta

For the Beta, a dynamic landing page has been added, which looks as follows:

![mvp_app](../../readme_assets/beta_website.png)

A decicated login page has also been added, which uses components from `react-google-login`. The "Get Started" button on the landing page redirects to the login page, and the Workflow demo can only be accessed by logging in.

The UX of the worflow demo page has been improved with a loading screen, to notify the user that a process is running in the backend.

---
[1]:https://github.com/carbon-design-system/carbon
