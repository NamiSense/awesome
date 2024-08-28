# Vietnamese text to speech

## Introduction

Using rabbitmq client to send text to speech request to a remote server, then receive by consumer.

- Request

```json
{
  "id": "task_id",
  "type": "tts",
  "content": "text cần chuyển đổi",
  "rate": 1,
  // rate: 0.8 → 1.2
  "accent": 1,
  // accent: 1 → 5
  "audio_format": "mp3"
  // audio_format: "mp3" | "wav"
}
```

| accent | name                      |
|--------|---------------------------|
| 1      | Hannah-Southern-Female    |
| 2      | ThuThuy-North-Female      |
| 3      | KimChi-North-Female       |
| 4      | HongPhuong-North-Female   |
| 5      | PhuongAnh-Southern-Female |

- Response

```json
{
  "status": "success",
  "url": "url",
  "id": "task_id"
}
```

## Setup to run

```bash
pip install -r requirements.txt
python rmq_receive.py
python rmq_send.py
```
