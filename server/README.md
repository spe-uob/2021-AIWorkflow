# 1. AIWorkFlow API

---

## 1.1. Table of Contents
- [1. AIWorkFlow API](#1-aiworkflow-api)
  - [1.1. Table of Contents](#11-table-of-contents)
  - [API User flow diagram](#api-user-flow-diagram)
  - [1.3. AIWorkFlow API Routers](#13-aiworkflow-api-routers)
    - [1.3.1. API for Twitter](#131-api-for-twitter)
      - [1.3.1.1. Endpoint](#1311-endpoint)
      - [1.3.1.2. 1.3.1.2 Accepted Methods](#1312-1312-accepted-methods)
      - [1.3.1.3. POST](#1313-post)
        - [1.3.1.3.1. 1.3.1.3.1 Parameters](#13131-13131-parameters)
        - [1.3.1.3.2. 1.3.1.3.2 Results](#13132-13132-results)
      - [1.3.1.4. GET](#1314-get)
        - [1.3.1.4.1. Parameters](#13141-parameters)
        - [1.3.1.4.2. Results](#13142-results)
      - [1.3.1.5. DELETE](#1315-delete)
        - [1.3.1.5.1. Parameters](#13151-parameters)
        - [1.3.1.5.2. 1.3.1.5.2 Results](#13152-13152-results)

---

## API User flow diagram

![user_flow_diagram](../assets/user_flow_diagram.png)

---

## 1.3. AIWorkFlow API Routers

### 1.3.1. API for Twitter

API search in Twitter in Twitter API key with the input keywords

#### 1.3.1.1. Endpoint

    /twitterapi/

#### 1.3.1.2. 1.3.1.2 Accepted Methods

```txt
GET   POST  DELETE
```

#### 1.3.1.3. POST

##### 1.3.1.3.1. 1.3.1.3.1 Parameters

| Parameter | Type    | Description         |
| --------- | ------- | ------------------- |
| user_id   | string  | Unique User ID      |
| key_word  | string  | User input Key Word |
| success   | boolean | request success     |
    

##### 1.3.1.3.2. 1.3.1.3.2 Results


{  
    "user_id": "114514",
    "key_word": "IBM666",
    "init": true,
    "success": true
}

#### 1.3.1.4. GET

##### 1.3.1.4.1. Parameters

| Parameter  | Type         | Description                             |
| user_id    | string       | Unique User ID (i.e. Phone Number)      |
| key_word   | string       | User input Key Word                     |


##### 1.3.1.4.2. Results

{  
    "user_id": "114514",
    "key_word": "IBM666",
}

#### 1.3.1.5. DELETE

##### 1.3.1.5.1. Parameters

| Parameter  | Type         | Description                             |
| user_id    | string       | Unique User ID (i.e. Phone Number)      |
| key_word   | string       | User input Key Word                     |

##### 1.3.1.5.2. 1.3.1.5.2 Results


{  
    "user_id": "114514",
    "key_word": "IBM666",
}
