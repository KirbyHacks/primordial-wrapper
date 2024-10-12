# 🌌 Primordial API Wrapper

Primordial API Wrapper is a Python package that provides a sleek and powerful interface to interact with the Primordial API. This wrapper makes API calls a breeze and handles responses like a pro! 🚀

## 🛠️ Installation

Get the Primordial API Wrapper up and running with a simple pip command:

```bash
pip install primordial-wrapper
```

## 🚀 Usage

To harness the power of the Primordial API Wrapper, import the `PrimordialAPI` class and initialize it with your API key:

```python
from primordial_wrapper import PrimordialAPI

api = PrimordialAPI(api_key="your_api_key")
```

### 🧰 Available Methods

The wrapper comes packed with these awesome methods:

1. 🤖 `generate_ai_response(prompt: str)`: Get an AI-generated response
2. 🎨 `generate_ai_image(prompt: str)`: Create an AI-generated image
3. 📥 `download_media(url: str)`: Download media from a URL
4. 📋 `create_pastebin(content: str)`: Create a new pastebin entry
5. 🔍 `get_pastebin(pastebin_id: str)`: Fetch a pastebin entry
6. ☀️ `get_weather(city: str)`: Get weather info for a city
7. 🗣️ `text_to_speech(text: str, lang: str = 'en')`: Convert text to speech
8. 📱 `generate_qr(url: str)`: Generate a QR code
9. 🔗 `shorten_url(url: str)`: Shorten a URL
10. 🚧 `bypass_link(url: str)`: Bypass shortened links
11. 📊 `get_bf_stock()`: Get Blox Fruits stock info
12. 🕷️ `scrape_web(url: str)`: Scrape a website
13. 📤 `upload_image(image_path: str)`: Upload an image
14. 🖼️ `get_image(image_id: str)`: Retrieve an image

### 💡 Example

Here's a quick example to get you started:

```python
from primordial_wrapper import PrimordialAPI
api = PrimordialAPI(api_key="your_api_key_here")
response = api.generate_ai_response("Tell me a joke about programming")
print(response)
```

## 👨‍💻 Development

Set up your dev environment in a flash:

1. Clone the repo:
   ```bash
   git clone https://github.com/KirbyHacks/primordial-wrapper.git
   cd primordial-wrapper
   ```

2. Install in editable mode with dev dependencies:
   ```bash
   pip install -e .[dev]
   ```

3. Run those tests:
   ```bash
   pytest
   ```

## 🤝 Contributing

We love contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a new branch for your feature or bug fix
3. 🛠️ Make your changes and write tests if applicable
4. ✅ Run the tests to ensure everything's working
5. 📤 Submit a pull request with a clear description of your changes

## 📜 License

This project is licensed under the MIT License. Check out the [LICENSE](LICENSE) file for all the legal stuff.

## 📬 Contact

Got questions? We've got answers!

- 📧 Email: rlow@kys.gay
- 💬 Discord: rlow._
- 🌐 Join our Discord server: [discord.gg/primordial-api](https://discord.gg/primordial-api)

For any other issues, feel free to open an issue on the [GitHub repository](https://github.com/KirbyHacks/primordial-wrapper).

Happy coding! 🎉
