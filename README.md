# article-generator

Generates articles using OpenAI's ChatGPT completion API.

## How to Use the Article Generator

Follow the steps below to generate articles using OpenAI's ChatGPT 3.5 Turbo API:

1. Set up the environment:

   - Clone the project repository.
   - Install the required dependencies listed in the `requirements.txt` file.

2. Obtain an API key:

   - Sign up for OpenAI and obtain an API key.
   - Create a `.env` file in the project directory.
   - Add the following line to the `.env` file:
     ```
     OPENAI_API_KEY=YOUR_API_KEY
     ```
   - Replace `YOUR_API_KEY` with your actual OpenAI API key.

3. Run the script:

   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Execute the following command:

     ```
     python generator.py topic_name num_variations --context "New context: "
     ```

     - Replace `generator.py` with the name of the Python script file.
     - Replace `topic_name` with the desired topic for the articles.
     - Replace `num_variations` with the number of article variations to generate.
     - Use the `--context` option to specify a custom global context (optional).

     Here is an example

     ```
     python generator.py "how to make pasta" 2 --context="Pretend you are an expert pastamaker and write an article about:"
     ```

4. Generated articles:

   - The script will create a folder based on the topic name (converted to lowercase with spaces replaced by underscores).
   - Inside the folder, you will find the generated articles in Markdown format.
   - Each article will have a filename corresponding to the prompt used.

5. Review and use the generated articles as needed.

That's it! You can now generate articles using the Article Generator project.
