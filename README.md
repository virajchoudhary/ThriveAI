# ThriveAI - Mental Health Chatbot

This is an AI-powered mental health support chatbot developed by Viraj Choudhary. The chatbot is designed to provide compassionate, supportive, and empathetic responses to users dealing with mental health issues. The system uses an offline generative model for conversation and includes crisis detection and safe handling of sensitive topics.

## Features

- Emotion classification (e.g., sadness, joy, anger, fear)
- Crisis keyword detection and emergency protocols
- Step-by-step therapeutic recommendations
- Responsive chat interface with message history
- Privacy-focused local processing

## Tech Stack

| Component       | Technology                         |
|-----------------|------------------------------------|
| Backend         | Python 3.10, Flask                 |
| AI Model        | microsoft/DialoGPT-medium          |
| Frontend        | HTML5, CSS3, JavaScript            |
| Deployment      | Local server / Heroku              |

## Prerequisites

Before running the application, ensure you have the following installed on your computer:

- **Python 3.10 or above**
- **pip** package installer
- **CUDA** (optional): If you have a compatible GPU and wish to use CUDA for faster inference, ensure that CUDA is installed and configured along with the appropriate version of PyTorch. If CUDA is not available, the application will run on CPU.
- **Required Python libraries**: See the `requirements.txt` file for a complete list.

## Installation

1. **Clone the Repository**

   Open your terminal or command prompt and run:

   ```bash
   git clone https://github.com/virajchoudhary/ThriveAI.git
   cd ThriveAI
