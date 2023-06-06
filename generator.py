import argparse
import os
import re
import openai
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

class ArticleGenerator:
    def __init__(self, api_key, context):
        openai.api_key = api_key
        self.context = context

    def generate_article(self, topic, variation):
        prompt = f"{topic}. Variation {variation}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": self.context + prompt}]
        )
        return response.choices[0].message.content.strip()


class FolderCreator:
    def create_topic_folder(self, topic):
        folder_name = re.sub(r'\s+', '_', topic.lower())
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        return folder_name


class ArticleSaver:
    def save_article(self, folder_name, prompt, article):
        max_filename_length = 50  # Maximum length of the filename
        truncated_prompt = prompt[:max_filename_length].strip()
        filename = re.sub(r'\s+', '_', truncated_prompt.lower()) + ".md"
        filepath = os.path.join(folder_name, filename)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(f"# {prompt}\n\n")
            file.write(article)


def main():
    parser = argparse.ArgumentParser(description="Generate articles using OpenAI's ChatGPT 3.5 Turbo API.")
    parser.add_argument("topic", type=str, help="The topic for the articles")
    parser.add_argument("num_variations", type=int, help="The number of article variations to generate")
    parser.add_argument("--context", type=str, default="Pretend you are a content writer and create a full article on the topic: ", help="Global context for the prompt")
    args = parser.parse_args()

    topic = args.topic
    num_variations = args.num_variations
    context = args.context

    api_key = os.getenv("OPENAI_API_KEY")
    article_generator = ArticleGenerator(api_key, context)
    folder_creator = FolderCreator()
    article_saver = ArticleSaver()

    folder_name = folder_creator.create_topic_folder(topic)

    with tqdm(total=num_variations, desc="Generating Articles") as pbar:
        for i in range(1, num_variations + 1):
            article_prompt = article_generator.generate_article(topic, i)
            article_saver.save_article(folder_name, article_prompt, article_prompt)
            pbar.update(1)

    print(f"\n{num_variations} variations of articles generated and saved in the '{folder_name}' folder.")


if __name__ == "__main__":
    main()
