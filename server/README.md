# 1. AIWorkFlow API

---

## 1.1. Table of Contents
- [1. AIWorkFlow API](#1-aiworkflow-api)
  - [1.1. Table of Contents](#11-table-of-contents)
  - [API User flow diagram](#api-user-flow-diagram)
  - [1.2. AIWorkFlow API Routers](#12-aiworkflow-api-routers)
    - [1.2.1. API for Twitter](#121-api-for-twitter)
      - [1.2.1.1. Save_tweet](#1211-save_tweet)
        - [1.2.1.1.1. Endpoint](#12111-endpoint)
        - [1.2.1.1.2. Accepted Methods](#12112-accepted-methods)
        - [1.2.1.1.3. Parameters](#12113-parameters)
        - [1.2.1.1.4. Results](#12114-results)
      - [1.2.1.2. Search_tweet](#1212-search_tweet)
        - [1.2.1.2.1. Endpoint](#12121-endpoint)
        - [1.2.1.2.2. Accepted Methods](#12122-accepted-methods)
        - [1.2.1.2.3. Parameters](#12123-parameters)
        - [1.2.1.2.4. Results](#12124-results)
      - [1.2.1.3. Delete_tweet](#1213-delete_tweet)
        - [1.2.1.3.1. Endpoint](#12131-endpoint)
        - [1.2.1.3.2. Accepted Methods](#12132-accepted-methods)
        - [1.2.1.3.3. Parameters](#12133-parameters)
        - [1.2.1.3.4. Results](#12134-results)

---

## API User flow diagram

![user_flow_diagram](../assets/user_flow_diagram.png)

---

## 1.2. AIWorkFlow API Routers

### 1.2.1. API for Twitter

API search in Twitter in Twitter API key with the input keywords

#### 1.2.1.1. Save_tweet

Save_tweet save tweets to database

##### 1.2.1.1.1. Endpoint

    /twitterapi/savetweet

##### 1.2.1.1.2. Accepted Methods

```txt
 POST 
```

##### 1.2.1.1.3. Parameters

| Parameter | Type    | Description         |
| --------- | ------- | ------------------- |
| user_id   | string  | Unique User ID      |
| key_word  | string  | User input Key Word |
| success   | boolean | response success     |
    

##### 1.2.1.1.4. Results


{  
    "user_id": "114514",
    "key_word": "IBM666",
    "success": true
}

#### 1.2.1.2. Search_tweet

Search_tweet search and collect information in twitter according to the key words

##### 1.2.1.2.1. Endpoint

    /twitterapi/searchtweet

##### 1.2.1.2.2. Accepted Methods

```txt
 GET 
```

##### 1.2.1.2.3. Parameters

| Parameter | Type    | Description         |
| --------- | ------- | ------------------- |
| user_id   | string  | Unique User ID      |
| key_word  | string  | User input Key Word |
| success   | boolean | request success     |
    

##### 1.2.1.2.4. Results


{  
    "user_id": "114514",
    "key_word": "IBM666",
    "success": true
}


#### 1.2.1.3. Delete_tweet

Delete_tweet delete tweet which is expired, unreleated and invalid.


##### 1.2.1.3.1. Endpoint

    /twitterapi/deletetweet

##### 1.2.1.3.2. Accepted Methods

```txt
 DELETE 
```

##### 1.2.1.3.3. Parameters

| Parameter | Type    | Description         |
| --------- | ------- | ------------------- |
| user_id   | string  | Unique User ID      |
| key_word  | string  | User input Key Word |
    
##### 1.2.1.3.4. Results


{  
    "user_id": "114514",
    "key_word": "IBM666",
}