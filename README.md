Absolutely, let's walk through setting up your custom GPT—**Codelabs Learning Assistant 2025**—as a Dockerized MCP (Model Context Protocol) server. This will allow your students to run it locally using Docker and interact with it through Visual Studio Code (VS Code).

---

## 🧰 Step 1: Install Docker

### For Windows:

1. **Download Docker Desktop**:

   * Visit the [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop) page.
   * Click on **"Download for Windows"**.([datacamp.com][1])

2. **Install Docker Desktop**:

   * Run the downloaded installer.
   * Follow the installation prompts.
   * During installation, ensure that the option to use **WSL 2** is selected if prompted.([datacamp.com][1])

3. **Start Docker Desktop**:

   * After installation, launch Docker Desktop from the Start menu.
   * Wait for Docker to initialize; you'll see the Docker icon in your system tray when it's ready.([datacamp.com][1])

4. **Verify Installation**:

   * Open **Command Prompt** or **PowerShell**.
   * Type the following command and press Enter:

     ```bash
     docker --version
     ```
   * You should see the Docker version information displayed.([knowledgehut.com][2])

### For macOS:

1. **Download Docker Desktop**:

   * Visit the [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop) page.
   * Click on **"Download for Mac"**.

2. **Install Docker Desktop**:

   * Open the downloaded `.dmg` file.
   * Drag the Docker icon to your Applications folder.([datacamp.com][1])

3. **Start Docker Desktop**:

   * Launch Docker from your Applications folder.
   * Wait for Docker to initialize; the Docker icon will appear in your menu bar when it's ready.

4. **Verify Installation**:

   * Open **Terminal**.
   * Type the following command and press Enter:

     ```bash
     docker --version
     ```
   * You should see the Docker version information displayed.([knowledgehut.com][2])

---

## 🛠️ Step 2: Prepare Your MCP Server Code

1. **Create a Project Directory**:

   * Create a new folder on your computer, e.g., `codelabs-mcp-server`.

2. **Create the Server Script**:

   * Inside this folder, create a file named `server.py`.
   * Open `server.py` in your preferred code editor and paste the following code:

     ```python
     from mcp.server.fastmcp import FastMCP
     import openai
     import os

     mcp = FastMCP("codelabs-assistant")

     @mcp.tool()
     async def answer_question(question: str) -> str:
         """Answers a question using the GPT model."""
         openai.api_key = os.getenv("OPENAI_API_KEY")
         response = openai.ChatCompletion.create(
             model="gpt-4",
             messages=[{"role": "user", "content": question}]
         )
         return response.choices[0].message["content"]

     if __name__ == "__main__":
         mcp.run(transport="stdio")
     ```

3. **Create a Requirements File**:

   * In the same folder, create a file named `requirements.txt`.
   * Add the following lines to specify the dependencies:

     ```
     openai
     mcp
     ```

4. **Create a Dockerfile**:

   * In the same folder, create a file named `Dockerfile` (no file extension).
   * Add the following content to define the Docker image:

     ```Dockerfile
     FROM python:3.11-slim

     WORKDIR /app

     COPY . .

     RUN pip install --no-cache-dir -r requirements.txt

     CMD ["python", "server.py"]
     ```

---

## 🧪 Step 3: Build the Docker Image

1. **Open Terminal**:

   * Navigate to the `codelabs-mcp-server` directory using the `cd` command.

     ```bash
     cd path/to/codelabs-mcp-server
     ```

2. **Build the Docker Image**:

   * Run the following command to build your Docker image:

     ```bash
     docker build -t codelabs-mcp-server .
     ```
   * Docker will process the `Dockerfile` and create an image named `codelabs-mcp-server`.

---

## 🧩 Step 4: Configure VS Code for MCP

1. **Create Configuration Directory**:

   * In your project directory (or the directory where students will work), create a folder named `.vscode`.

2. **Create MCP Configuration File**:

   * Inside the `.vscode` folder, create a file named `mcp.json`.
   * Add the following content to configure the MCP server:

     ```json
     {
       "inputs": [
         {
           "type": "promptString",
           "id": "openai_api_key",
           "description": "Enter your OpenAI API Key",
           "password": true
         }
       ],
       "servers": {
         "codelabs-assistant": {
           "command": "docker",
           "args": [
             "run",
             "-i",
             "--rm",
             "-e",
             "OPENAI_API_KEY=${input:openai_api_key}",
             "codelabs-mcp-server"
           ]
         }
       }
     }
     ```

---

## 🚀 Step 5: Run the MCP Server in VS Code

1. **Open VS Code**:

   * Launch Visual Studio Code.

2. **Open the Project Folder**:

   * Go to **File > Open Folder** and select the directory containing your project.

3. **Access the Command Palette**:

   * Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS) to open the Command Palette.

4. **Start the MCP Server**:

   * Type `MCP: List Servers` and select it.
   * In the list, find `codelabs-assistant` and click **Start**.

5. **Enter OpenAI API Key**:

   * When prompted, enter your OpenAI API key.
   * The server will start, and you can now interact with your custom GPT through VS Code's chat interface.

---

By following these steps, you've successfully set up your custom GPT as a Dockerized MCP server, enabling your students to run and interact with it locally through Visual Studio Code. If you need further assistance or have any questions, feel free to ask!

[1]: https://www.datacamp.com/tutorial/docker-tutorial?utm_source=chatgpt.com "Docker for Beginners: A Practical Guide to Containers"
[2]: https://www.knowledgehut.com/blog/devops/docker-for-beginners?utm_source=chatgpt.com "Docker Tutorial for Beginners [2025 Guide] - KnowledgeHut"
