# 1. AI WorkFlow Backend API Documentation

---

## 1.1. Table of Contents
- [1. AI WorkFlow Backend API Documentation](#1-ai-workflow-backend-api-documentation)
  - [1.1. Table of Contents](#11-table-of-contents)
  - [1.2. API User flow diagram](#12-api-user-flow-diagram)
  - [1.3. API Endpoints](#13-api-endpoints)
    - [1.3.1. API for Twitter](#131-api-for-twitter)
      - [1.3.1.1. Save Tweets](#1311-save-tweets)
        - [1.3.1.1.1. Endpoint](#13111-endpoint)
        - [1.3.1.1.2. Accepted Methods](#13112-accepted-methods)
        - [1.3.1.1.3. Parameters](#13113-parameters)
        - [1.3.1.1.4. Results](#13114-results)
      - [1.3.1.2. Search Tweets](#1312-search-tweets)
        - [1.3.1.2.1. Endpoint](#13121-endpoint)
        - [1.3.1.2.2. Accepted Methods](#13122-accepted-methods)
        - [1.3.1.2.3. Parameters](#13123-parameters)
        - [1.3.1.2.4. Results](#13124-results)

---

## 1.2. API User flow diagram

![user_flow_diagram](
    diagrams/user_flow_diagram.png)

---

## 1.3. API Endpoints

### 1.3.1. API for Twitter

API search in Twitter in Twitter API key with the input keywords

#### 1.3.1.1. Save Tweets

Saves tweets to database

##### 1.3.1.1.1. Endpoint

    /twitterapi/tweets

##### 1.3.1.1.2. Accepted Methods

```txt
 POST 
```

##### 1.3.1.1.3. Parameters

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

#### 1.3.1.2. Search Tweets

Search tweet search and collect information in twitter according to the key words

##### 1.3.1.2.1. Endpoint

    /twitterapi/tweets

##### 1.3.1.2.2. Accepted Methods

```txt
 GET 
```

##### 1.3.1.2.3. Parameters

**Headers:**

| Header | Description      | Optional |
| ------ | ---------------- | -------- |
| code   | Google auth code | No       |

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


##### 1.3.1.2.4. Results


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
