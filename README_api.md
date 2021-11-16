# 1. AIWorkFlow API

---

## 1.1. Table of Contents
- [1. AIWorkFlow API](#1-aiworkflow-api)
  - [1.1. Table of Contents](#11-table-of-contents)
  - [Example](#example)
    - [Request](#request)
      - [endpoint](#endpoint)
      - [Parameters](#parameters)
  - [1.2. AIWorkFlow API Details](#12-aiworkflow-api-details)
    - [1.2.1 Request](#121-request)
      - [1.2.1.1. Endpoint](#1211-endpoint)
      - [1.2.1.2. Accepted Methods](#1212-accepted-methods)
      - [1.2.1.3. Parameters](#1213-parameters)
  - [1.3. AIWorkFlow API Routers](#13-aiworkflow-api-routers)
    - [1.3.1. API for Twitter](#131-api-for-twitter)
      - [1.3.1.1 Endpoint](#1311-endpoint)
      - [1.3.1.2 Accepted Methods](#1312-accepted-methods)
      - [1.3.1.3 POST](#1313-post)
        - [1.3.1.3.1 Parameters](#13131-parameters)
        - [1.3.1.3.2 Results](#13132-results)
      - [1.3.1.4 GET](#1314-get)
        - [1.3.1.4.1 Parameters](#13141-parameters)
        - [1.3.1.4.2 Results](#13142-results)
      - [1.3.1.5 DELETE](#1315-delete)
        - [1.3.1.5.1 Parameters](#13151-parameters)
        - [1.3.1.5.2 Results](#13152-results)


## Example

### Request

#### endpoint

#### Parameters

| Key                    | Type      | Description                       |
| ---------------------- | --------- | --------------------------------- |
| data                   | object    | data for end user                 |
| data                   | boolean   | Whether to forward call           |
| data.is_ivr            | boolean   | Whether to check for numpad input |
| data.ivr_num_of_digits | integer   | Expected number of digits from ivr|
| data.voicebot_time_gap | integer   | (in seconds) Voicebot Time Gap, user speech still be recorded but voicebot will not response within this time gap |
| data.voicebot_timeout  | integer   | (in seconds), if no user speech received after this timeout, voicebot will go to fallback |
| data.speech_speed      | float     | voicebot speech speech<br>`0.6` to `2`. `2` means double speed, `0.6` means 60% speed, (default: `1`) |
| data.message           | list      | displayed/spoken text to user     |
| is_completed           | boolean   | whether the call is completed     |
| message                | string    | API message / current intent      |
| success                | boolean   | intent success                    |
| session_id             | string    | Unique Session ID                 |


```json
{
    "data": {
    },
    "message": "init",
    "session_id": "61903027",
    "success": true
}

## 1.2. AIWorkFlow API Details

API used to interact with twitter

### 1.2.1 Request


#### 1.2.1.1. Endpoint

    /aiworkflow

#### 1.2.1.2. Accepted Methods

POST    

#### 1.2.1.3. Parameters

| Parameter  | Type         | Description                             | Remarks                               |
| ---------- | ------------ | --------------------------------------- | ------------------------------------- |
| user_id    | string       | Unique User ID (i.e. Phone Number)      |                                       |
| text       | string       | User input                              |                                       |
| init       | boolean      | Reset flow (optional, defaults to False)|                                       |
| call_end   | boolean      | Whether call has been ended by the user | optional, defaults to `false`         |
| call_status| string       | Call Status                             | only needed when `call_end` is `true` |





---

## 1.3. AIWorkFlow API Routers

### 1.3.1. API for Twitter

API search in Twitter in Twitter API key with the input keywords

#### 1.3.1.1 Endpoint

    /twitterapi

#### 1.3.1.2 Accepted Methods
GET   POST  DELETE

#### 1.3.1.3 POST

##### 1.3.1.3.1 Parameters

| Parameter  | Type         | Description                             |
| user_id    | string       | Unique User ID (i.e. Phone Number)      |
| key_word   | string       | User input Key Word                     | 
| init       | boolean      | Reset flow (optional, defaults to False)| 
| succe      | boolean      | intent success                          |
    

##### 1.3.1.3.2 Results


{  
    "user_id": "114514",
    "key_word": "IBM666",
    "init": true,
    "success": true
}

#### 1.3.1.4 GET

##### 1.3.1.4.1 Parameters

| Parameter  | Type         | Description                             |
| user_id    | string       | Unique User ID (i.e. Phone Number)      |
| key_word   | string       | User input Key Word                     |


##### 1.3.1.4.2 Results

{  
    "user_id": "114514",
    "key_word": "IBM666",
}

#### 1.3.1.5 DELETE

##### 1.3.1.5.1 Parameters

| Parameter  | Type         | Description                             |
| user_id    | string       | Unique User ID (i.e. Phone Number)      |
| key_word   | string       | User input Key Word                     |

##### 1.3.1.5.2 Results


{  
    "user_id": "114514",
    "key_word": "IBM666",
}
