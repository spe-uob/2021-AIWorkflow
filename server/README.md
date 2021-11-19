# 1. AIWorkFlow API Documentation

---

## 1.1. Table of Contents
- [1. AIWorkFlow API Documentation](#1-aiworkflow-api-documentation)
  - [1.1. Table of Contents](#11-table-of-contents)
  - [1.2. API User flow diagram](#12-api-user-flow-diagram)
  - [1.3. API Endpoints](#13-api-endpoints)
    - [1.3.1. API for Twitter](#131-api-for-twitter)
      - [1.3.1.1. Save Tweet](#1311-save-tweet)
        - [1.3.1.1.1. Endpoint](#13111-endpoint)
        - [1.3.1.1.2. Accepted Methods](#13112-accepted-methods)
        - [1.3.1.1.3. Parameters](#13113-parameters)
        - [1.3.1.1.4. Results](#13114-results)
      - [1.3.1.2. Search_tweet](#1312-search_tweet)
        - [1.3.1.2.1. Endpoint](#13121-endpoint)
        - [1.3.1.2.2. Accepted Methods](#13122-accepted-methods)
        - [1.3.1.2.3. Parameters](#13123-parameters)
        - [1.3.1.2.4. Results](#13124-results)
      - [1.3.1.3. Delete_tweet](#1313-delete_tweet)
        - [1.3.1.3.1. Endpoint](#13131-endpoint)
        - [1.3.1.3.2. Accepted Methods](#13132-accepted-methods)
        - [1.3.1.3.3. Parameters](#13133-parameters)
        - [1.3.1.3.4. Results](#13134-results)

---

## 1.2. API User flow diagram

![user_flow_diagram](../readme_assets/user_flow_diagram.png)

---

## 1.3. API Endpoints

### 1.3.1. API for Twitter

API search in Twitter in Twitter API key with the input keywords

#### 1.3.1.1. Save Tweet

Saves tweets to database

##### 1.3.1.1.1. Endpoint

    /twitterapi/tweets

##### 1.3.1.1.2. Accepted Methods

```txt
 POST 
```

##### 1.3.1.1.3. Parameters

| Parameter  | Type    | Description         |
| ---------- | ------- | ------------------- |
| user_id    | string  | Unique User ID      |
| tweet_text | string  | Tweet text          |
| keyword    | string  | user keyword        |
| tone       | string  | Detected tone       |
| tone_score | integer | Detected tone score |
| success    | boolean | response success    |

e.g. 

```json
{
    "user_id": "123456789",
    "tweet_text": "This is a tweet",
    "tone": "Anger",
    "keyword": "tweet",
    "tone_score": 0.5,
    "success": true
}
```

##### 1.3.1.1.4. Results

**Success:**

```json
{  
    "data": {
      "tweet_id": "123456789",
    },
    "message": "saved tweet successfully",
    "success": true
}
```

**Failed:**

```json
{  
    "data": {},
    "message": "Cannot save tweet - error",
    "success": false
}
```

#### 1.3.1.2. Search_tweet

Search_tweet search and collect information in twitter according to the key words

##### 1.3.1.2.1. Endpoint

    /twitterapi/searchtweet

##### 1.3.1.2.2. Accepted Methods

```txt
 GET 
```

##### 1.3.1.2.3. Parameters

| Parameter | Type    | Description         |
| --------- | ------- | ------------------- |
| user_id   | string  | Unique User ID      |
| key_word  | string  | User input Key Word |
| success   | boolean | request success     |
    

##### 1.3.1.2.4. Results


{  
    "user_id": "114514",
    "key_word": "IBM666",
    "success": true
}


#### 1.3.1.3. Delete_tweet

Delete_tweet delete tweet which is expired, unreleated and invalid.


##### 1.3.1.3.1. Endpoint

    /twitterapi/deletetweet

##### 1.3.1.3.2. Accepted Methods

```txt
 DELETE 
```

##### 1.3.1.3.3. Parameters

| Parameter | Type   | Description         |
| --------- | ------ | ------------------- |
| user_id   | string | Unique User ID      |
| key_word  | string | User input Key Word |
    
##### 1.3.1.3.4. Results


{  
    "user_id": "114514",
    "key_word": "IBM666",
}