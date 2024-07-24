# Janpanese realtime transcription

## API

- URL: `wss://jppoc.namisense.ai/connect?sample_rate=16000`
- Query parameters: `sample_rate` (8000-8kHz or 16000-16kHz default 16000)

`Note`: Using mono channel audio

## Setup to run

```bash
pip install -r requirements.txt
python main.py
```

![output.png](output.png)