from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from claude_service import generate_image_description

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body>
            <h2>WCAG Image Description Generator</h2>

            <input type="file" id="image"/>
            <button onclick="generate()">Generate Description</button>

            <p id="result"></p>

            <script>
                async function generate(){

                    let file = document.getElementById("image").files[0]

                    let formData = new FormData()
                    formData.append("file", file)

                    let response = await fetch("/generate", {
                        method: "POST",
                        body: formData
                    })

                    let data = await response.json()

                    document.getElementById("result").innerText = data.description
                }
            </script>

        </body>
    </html>
    """


@app.post("/generate")
async def generate(file: UploadFile = File(...)):

    image_bytes = await file.read()

    description = generate_image_description(image_bytes)

    return {"description": description}