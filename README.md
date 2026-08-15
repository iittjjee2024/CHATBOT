#  Rule-Based Chatbot

A simple chatbot that responds to user input using predefined rules and keyword matching.

## Features

- Handles common greetings (hello, hi, hey, good morning, etc.)
- Answers questions about itself (name, capabilities, age)
- Provides dynamic responses (current time)
- Tells jokes and responds to compliments
- Fallback response for unrecognized input
- Case-insensitive matching

## How It Works

The chatbot uses a dictionary of keyword patterns mapped to responses. When the user types something:

1. The input is converted to lowercase for case-insensitive matching.
2. The chatbot checks the input against each set of keywords in order.
3. The first matching keyword triggers its associated response.
4. If no pattern matches, a helpful fallback message is displayed.

## How to Run

```bash
python chatbot.py
```

No external dependencies required — uses only Python standard library.

## Example Interaction

```
You: hello
Chatbot: Hello! How can I help you today?

You: what can you do
Chatbot: I can respond to greetings, answer basic questions about myself, tell you the time, and have a simple conversation. Try asking me something!

You: tell me a joke
Chatbot: Why do programmers prefer dark mode? Because light attracts bugs!

You: bye
Chatbot: Goodbye! Have a great day!
```

## Supported Topics

| Topic | Example Input |
|-------|--------------|
| Greetings | hello, hi, hey, good morning |
| Farewell | bye, goodbye, exit, quit |
| Bot identity | who are you, your name |
| Capabilities | what can you do, help |
| Time | what time is it |
| Weather | weather, temperature |
| Jokes | tell me a joke |
| Compliments | thanks, awesome, great |
| Philosophy | meaning of life, purpose |

## Technologies

- Python 3.x
- String pattern matching



