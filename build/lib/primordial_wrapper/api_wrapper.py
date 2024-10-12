import requests

class PrimordialAPI:
    def __init__(self, api_key: str, base_url: str = "http://dlr-node.kys.gay:4685"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'X-API-Key': self.api_key
        }

    def _handle_response(self, response):
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return {"status": "error", "result": {"message": str(http_err)}}
        except Exception as err:
            return {"status": "error", "result": {"message": str(err)}}

    def generate_ai_response(self, prompt: str):
        """Generates an AI response based on the provided prompt."""
        endpoint = f"{self.base_url}/ai/generate"
        params = {"prompt": prompt}
        response = requests.get(endpoint, headers=self.headers, params=params)
        return self._handle_response(response)

    def generate_ai_image(self, prompt: str):
        """Generates an AI image based on the provided prompt."""
        endpoint = f"{self.base_url}/ai/imagine"
        params = {"prompt": prompt}
        response = requests.get(endpoint, headers=self.headers, params=params)
        return self._handle_response(response)

    def download_media(self, url: str):
        """Downloads media from a provided URL."""
        endpoint = f"{self.base_url}/media/download"
        params = {"url": url}
        response = requests.get(endpoint, headers=self.headers, params=params)
        return self._handle_response(response)

    def create_pastebin(self, content: str):
        """Creates a new pastebin entry."""
        endpoint = f"{self.base_url}/pastebin/create"
        data = {"content": content}
        response = requests.post(endpoint, headers=self.headers, json=data)
        return self._handle_response(response)

    def get_pastebin(self, pastebin_id: str):
        """Retrieves a pastebin entry by ID."""
        endpoint = f"{self.base_url}/pastebin/{pastebin_id}"
        response = requests.get(endpoint, headers=self.headers)
        return self._handle_response(response)

    def get_weather(self, city: str):
        """Gets weather information for a specific city."""
        endpoint = f"{self.base_url}/weather"
        params = {"city": city}
        response = requests.get(endpoint, headers=self.headers, params=params)
        return self._handle_response(response)

    def text_to_speech(self, text: str, lang: str = 'en'):
        """Converts text to speech."""
        endpoint = f"{self.base_url}/text-to-speech"
        data = {"text": text, "lang": lang}
        response = requests.post(endpoint, headers=self.headers, json=data)
        return self._handle_response(response)

    def generate_qr(self, url: str):
        """Generates a QR code for a given URL."""
        endpoint = f"{self.base_url}/utilities/qr-generate"
        params = {"url": url}
        response = requests.get(endpoint, headers=self.headers, params=params)
        return self._handle_response(response)

    def shorten_url(self, url: str):
        """Shortens a given URL."""
        endpoint = f"{self.base_url}/utilities/shorten-url"
        data = {"url": url}
        response = requests.post(endpoint, headers=self.headers, json=data)
        return self._handle_response(response)

    def bypass_link(self, url: str):
        """Bypasses a shortened or intermediary link."""
        endpoint = f"{self.base_url}/utilities/bypass"
        params = {"url": url}
        response = requests.get(endpoint, headers=self.headers, params=params)
        return self._handle_response(response)

    def get_bf_stock(self):
        """Retrieves Blox Fruits stock information."""
        endpoint = f"{self.base_url}/utilities/bf-stock"
        response = requests.get(endpoint, headers=self.headers)
        return self._handle_response(response)

    def scrape_web(self, url: str):
        """Performs web scraping on a given URL."""
        endpoint = f"{self.base_url}/utilities/scrape"
        params = {"url": url}
        response = requests.get(endpoint, headers=self.headers, params=params)
        return self._handle_response(response)

    def upload_image(self, image_path: str):
        """Uploads an image to the service."""
        endpoint = f"{self.base_url}/images"
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            response = requests.post(endpoint, headers=self.headers, files=files)
        return self._handle_response(response)

    def get_image(self, image_id: str):
        """Retrieves an image by its ID."""
        endpoint = f"{self.base_url}/images/{image_id}"
        response = requests.get(endpoint, headers=self.headers)
        if response.status_code == 200:
            return response.content  # Image content, binary data
        return self._handle_response(response)
