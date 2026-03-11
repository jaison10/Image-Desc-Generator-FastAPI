import base64
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def generate_image_description(image_bytes):

    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    message = client.messages.create(
        model="claude-3-5-sonnet-latest",
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": base64_image,
                        },
                    },
                    {
                        "type": "text",
                        "text": "Generate a clear WCAG-compliant alt text description of this image for visually impaired users."
                    }
                ],
            }
        ],
    )

    return message.content[0].text