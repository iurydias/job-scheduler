# ⏱️ JOB SCHEDULER

A job scheduler made in order to understand and study python programming language and basic technologies use.  

## Architecture

![alt text](https://github.com/iurydias/job-scheduler/blob/master/arch.png?raw=true "Project Architecture")

**Basically, it:**

✨ gets data from a post request ⤵️

➡️ send to a queue ⤵️

➡️ a consumer gets that data ⤵️

➡️ save in a non-relational database (mongodb) ⤵️

➡️ publish in another queue notifying the finished job ⤵️

➡️ first service gets that finished job ⤵️

➡️ update job's status ✅

## Initiating the application

```shell script
    docker-compose up
```

## Routes

### Create a job

```POST /jobs/create```

**Request**

Body (*application/json*)

* Any data

Exemplo:

```shell script
curl -XPOST -H "Content-type: application/json" -d '{"name":"iury"}' 'localhost:5000/currency'
```

##### Response

+ **Success** 201

```json
{
  "id": "88478d93-361b-4394-810b-4f2f102fba86",
  "data": {
    "name": "iury"
  }
} 
``` 

### Check job status

```GET /jobs```

**Request**

Param (*Via Query*)

* **id**: The job identification (received when created)

Exemplo:

```shell script
curl -XGET 'localhost:5000/jobs?id=88478d93-361b-4394-810b-4f2f102fba86'
```

+ **Success** 200

```json
{
  "id": "88478d93-361b-4394-810b-4f2f102fba86",
  "status": "DONE"
} 
``` 