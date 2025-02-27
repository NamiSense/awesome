# Japanese long audio transcription

## Introduction

- Request

```json
{
  "id": "task_id",
  "type": "analysis",
  "url": "url to download the audio file",
  "lang": "jp",
  "num_speakers": 2
}
```

`Note`: Using mono channel audio

- Response
We use queue system, after request is put into input queue, once file is successfully handle, there will be a response on output queue with a signed URL to get the JSON result:
```json
{"url_result": "https://nmw-for-qa.s3.ap-southeast-1.amazonaws.com/res/86fe8527-e34a-47a6-bc85-c372525160d1.json?AWSAccessKeyId=AKIAU5ATHYMXO5U2X6JS&Signature=tBqVuJ2eO2fxG1OBtrRWsS8gb5w%3D&Expires=1737694853", "status": "success", "length_raw": 190.98, "id": "1058e5e2-3b15-400b-88df-de344f8d95c8", "version": "2.13.7", "env": "saas.jp.prod"}
```
Json result itself going to have value like below:
```json
{
  "length_raw": 1432.25,
  "length_speech": 1305.62,
  "segments": [
    {
      "index": 0,
      "start": 5.41,
      "end": 5.87,
      "transcript": "こちら",
      "transcript_norm": "こちら。",
      "snr_result": false,
      "snr_score": -24.87,
      "words": [],
      "label": "01",
      "conf_avg": 0
    },
    {
      "index": 1,
      "start": 8.1,
      "end": 28.01,
      "transcript": "生のテキスト",
      "transcript_norm": "標準テキスト。",
      "snr_result": true,
      "snr_score": 17.9,
      "words": [],
      "label": "01",
      "conf_avg": 0
    }
  ],
  "status": "success",
  "id": "task_id"
}
```

## Setup to run

```bash
pip install -r requirements.txt
python rmq_receive.py
python rmq_send.py
```
