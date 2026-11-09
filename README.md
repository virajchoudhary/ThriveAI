# ThriveAI

A Flask chat prototype that classifies emotion with `bhadresh-savani/distilbert-base-uncased-emotion` and selects preset replies. It does not use the DialoGPT model described in the previous README.

## Routes

`app.py` serves the chat page at `GET /` and accepts chat requests at `POST /chat`.

The source contains a keyword-based crisis branch. Its coverage and response content have not been validated for crisis use.

## Run locally

The repository does not include a root `requirements.txt`. Install compatible Flask and Transformers dependencies, plus a supported model runtime, in a virtual environment. Then run:

```sh
python app.py
```

The model assets and runtime have not been tested in this closeout. The Transformers loader may need network access unless the model is cached. Public deployment has not been verified. `app.py` binds to all interfaces; keep the prototype on a trusted local network.

This prototype has not been evaluated for effectiveness or safety. It is not for diagnosis, treatment, mental-health care, crisis response, or emergency support.
