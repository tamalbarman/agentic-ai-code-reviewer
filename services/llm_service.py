import httpx

class LocalLLM:

    def __init__(self, model="llama3.2:3b"):
        self.url = "http://localhost:11434/api/generate"
        self.model = model

    async def generate(self, prompt: str):

        async with httpx.AsyncClient(timeout=120) as client:

            response = await client.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"temperature": 0}
                }
            )

        return response.json()["response"]