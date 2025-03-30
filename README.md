# ThriveAI

ThriveAI is an AI-powered mental health support chatbot developed by me. It is designed to engage in compassionate, supportive conversations with users, offering empathetic responses and guidance when dealing with mental health issues. The system runs entirely offline using a generative conversational model combined with safety and topic filters.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)
- [Example Output](#example-output)

## Overview

ThriveAI uses the pre-trained "microsoft/DialoGPT-medium" model from Hugging Face to generate empathetic and supportive responses to mental health–related inputs. It incorporates safety checks by detecting crisis keywords (such as "suicide", "kill myself", or "self-harm") to immediately provide emergency helpline information. For inputs that are not recognized as mental health–related, it returns a default message indicating it can only assist with mental health topics.

## Features

- Empathetic and supportive generative responses tailored to mental health issues.
- Crisis keyword detection with immediate emergency resource messages.
- Topic filtering: Only responds to mental health–related inputs; other topics receive a default message.
- Offline processing using a local generative model.
- A simple, responsive web interface built with Flask.

## Tech Stack

| Component       | Technology                         |
|-----------------|------------------------------------|
| Backend         | Python 3.10, Flask                 |
| AI Model        | microsoft/DialoGPT-medium          |
| Frontend        | HTML5, CSS3, JavaScript            |
| Deployment      | Local server / Heroku              |

## Prerequisites

Before running the application, ensure you have the following installed on your computer:

1. **Python 3.10 or above**
2. **pip** package installer
3. **CUDA (Optional):**  
   If you have a compatible GPU and wish to use CUDA for faster inference, install CUDA along with the appropriate version of PyTorch. If CUDA is not available, the application will run on CPU.
4. **Required Python libraries:**  
   All necessary libraries are listed in the `requirements.txt` file.

## Installation

1. **Clone the Repository**

   Open your terminal or command prompt and run:
   ```
   git clone https://github.com/virajchoudhary/ThriveAI.git
   cd ThriveAI
2. **Set Up a Virtual Environment (Optional but Recommended)**
   ```
   python -m venv venv
   On Linux/macOS:
   source venv/bin/activate
   On Windows:
   venv\Scripts\activate

3. **Install Dependencies**
   ```
   pip install -r requirements.txt

## Configuration

Since ThriveAI runs offline using a pre-trained generative model, no external API keys are required. However, ensure that your environment is set up correctly:

    If you want to leverage GPU acceleration, confirm that CUDA is installed and that PyTorch is configured for CUDA.

    Review the requirements.txt file for a complete list of dependencies.

## Usage

    Run the Application Locally
    python app.py
    Access the Chatbot Interface

    Open your web browser and navigate to: http://localhost:5000

The application will start a Flask server that hosts the ThriveAI chat interface, allowing users to interact with the chatbot.

## Dependencies

ThriveAI relies on the following Python libraries:

    Flask

    torch

    transformers

    (Optional) CUDA-compatible PyTorch for GPU acceleration

Install all dependencies via:
pip install -r requirements.txt

## Error Handling

The application includes basic error handling for:

    Model Generation Errors: In case of any issues during the response generation, a fallback message is provided.

    Input Processing Errors: If an error occurs while processing user input, the server logs the error and returns a processing error message.

    Critical Input Detection: If the input contains crisis keywords, an immediate helpline message is returned to ensure user safety.

## Contributing

Contributions are welcome! If you would like to help improve ThriveAI:

    Fork the repository.

    Create a new branch for your feature or bugfix.

    Commit your changes with clear messages.

    Push your branch and create a pull request.

Please follow the code style and guidelines provided in the repository.


## License

This project is licensed under the MIT License. See the LICENSE file for details.

© 2024 Viraj Choudhary


## Example Output
```
User Input: "I'm feeling really anxious today."
AI Response:
"Based on what you've shared, it sounds like you're experiencing anxiety. Remember, it's okay to feel this way. It might help to practice some breathing exercises or consider talking to a trusted friend or professional. Your feelings are valid."

User Input: "I have suicidal thoughts."
AI Response:
"Immediate Support: National Suicide Prevention Lifeline (US): 1-800-273-8255"

User Input: "Tell me about the weather."
AI Response:
"I'm sorry, I can only assist with mental health related topics."
