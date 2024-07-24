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
python receive.py
python send.py
```
