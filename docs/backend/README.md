# 1. AI WorkFlow Backend API Documentation

---

## 1.1. Table of Contents
- [1. AI WorkFlow Backend API Documentation](#1-ai-workflow-backend-api-documentation)
  - [1.1. Table of Contents](#11-table-of-contents)
  - [1.2. API User flow diagram](#12-api-user-flow-diagram)
  - [1.3. Authorization](#13-authorization)
  - [1.4. API Endpoints](#14-api-endpoints)
    - [1.4.1. API for Twitter](#141-api-for-twitter)
      - [1.4.1.1. Save Tweets](#1411-save-tweets)
        - [1.4.1.1.1. Endpoint](#14111-endpoint)
        - [1.4.1.1.2. Accepted Methods](#14112-accepted-methods)
        - [1.4.1.1.3. Parameters](#14113-parameters)
        - [1.4.1.1.4. Results](#14114-results)
      - [1.4.1.2. Search Tweets](#1412-search-tweets)
        - [1.4.1.2.1. Endpoint](#14121-endpoint)
        - [1.4.1.2.2. Accepted Methods](#14122-accepted-methods)
        - [1.4.1.2.3. Parameters](#14123-parameters)
        - [1.4.1.2.4. Results](#14124-results)
    - [1.4.2. API for Users](#142-api-for-users)
      - [1.4.2.1. User Login](#1421-user-login)
        - [1.4.2.1.1. Endpoint](#14211-endpoint)
        - [1.4.2.1.2. Accepted Methods](#14212-accepted-methods)
        - [1.4.2.1.3. Parameters](#14213-parameters)
        - [1.4.2.1.4. Results](#14214-results)
      - [1.4.2.2. User Logout](#1422-user-logout)
        - [1.4.2.2.1. Endpoint](#14221-endpoint)
        - [1.4.2.2.2. Accepted Methods](#14222-accepted-methods)
        - [1.4.2.2.3. Parameters](#14223-parameters)
        - [1.4.2.2.4. Results](#14224-results)

---

## 1.2. API User flow diagram

![user_flow_diagram](
    diagrams/user_flow_diagram.png)

---

## 1.3. Authorization

All paths have to have a Header:

    Authorization: Bearer <access_token>

where `access_token` is the access token of the user. This can be retrieved from using the `/user/login` endpoint.

---

## 1.4. API Endpoints

### 1.4.1. API for Twitter

API search in Twitter in Twitter API key with the input keywords

#### 1.4.1.1. Save Tweets

Saves tweets to database

##### 1.4.1.1.1. Endpoint

    /twitterapi/tweets

##### 1.4.1.1.2. Accepted Methods

```txt
 POST 
```

##### 1.4.1.1.3. Parameters

| Parameter      | Type    | Description           | Optional |
| -------------- | ------- | --------------------- | -------- |
| user_id        | string  | Unique User ID        | No       |
| tweet_text     | string  | Tweet text            | No       |
| keyword        | string  | user keyword          | No       |
| overall_tone   | string  | Detected overall tone | No       |
| specified_tone | string  | Detected tone         | Yes      |
| tone_score     | integer | Detected tone score   | Yes      |

e.g. 

```json
{
    "user_id": "123456789",
    "tweet_text": "This is a tweet",
    "overall_tone": "Negivate",
    "specified_tone":["Anger", "sad"],
    "keyword": "tweet",
    "tone_score": 0.5
}
```

##### 1.4.1.1.4. Results

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

#### 1.4.1.2. Search Tweets

Search tweet search and collect information in twitter according to the key words

##### 1.4.1.2.1. Endpoint

    /twitterapi/tweets

##### 1.4.1.2.2. Accepted Methods

```txt
 GET 
```

##### 1.4.1.2.3. Parameters

**Query Params:**

| Parameter  | Type   | Description                    | Optional |
| ---------- | ------ | ------------------------------ | -------- |
| user_id    | string | Unique User ID                 | No       |
| keywords   | string | User input Key Word            | No       |
| tones      | string | User-specified tone            | No       |
| time_start | string | User input starting time range | Yes      |
| time_end   | string | User input ending time range   | Yes      |

 e.g.

```txt
GET http://hostname.domain/twitterapi/tweets?user_id=123&keywords=tweet,ibm&tones=happy,sad&time_start=2019-01-01&time_end=2019-01-02
```


##### 1.4.1.2.4. Results


**Success:**

```json
{  
    "data": {
      "tweets": [
        {
          "text": "I love IBM",
          "url": "https:/twitter.com/id/8013879718"
        },
        {
          "text": "I dislike IBM",
          "url": "https:/twitter.com/id/231233217"
        }
      ],
    },
    "message": "searched tweet successfully",
    "success": true
}
```


**Failed:**

```json
{  
    "data": {},
    "message": "Cannot search tweet - error",
    "success": false
}
```


### 1.4.2. API for Users

#### 1.4.2.1. User Login

Lets user login to the system

##### 1.4.2.1.1. Endpoint

    /user/login

##### 1.4.2.1.2. Accepted Methods

```txt
 POST 
```

##### 1.4.2.1.3. Parameters

| Parameter | Type   | Description      | Optional |
| --------- | ------ | ---------------- | -------- |
| code      | string | Unique auth code | No       |

e.g. 

```json
{
    "code": "123456789",
}
```

##### 1.4.2.1.4. Results

```json
{  
    "data": {
      "google_object":{

      }
    },
    "message": "login successful",
    "success": true
}
```

#### 1.4.2.2. User Logout

##### 1.4.2.2.1. Endpoint

    /user/logout

##### 1.4.2.2.2. Accepted Methods

```txt
POST
```

##### 1.4.2.2.3. Parameters

| Parameter | Type   | Description    | Optional |
| --------- | ------ | -------------- | -------- |
| user_id   | string | Unique user id | No       |

e.g. 

```json
{
    "user_id": "123456789",
}
```

##### 1.4.2.2.4. Results

```json
{  
    "data": {},
    "message": "logout successful",
    "success": true
}
```
