from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from typing import List, Dict
import re

def article_preprocessing(filepath : str, article_name : str) -> List:
    with open(filepath, 'r') as file:
        article_string = file.read()
        article_list = re.split('\n', article_string)
    
    return {'title': article_name, 'paragraphs' : article_list}

def render_article(template_path : str, inputs : Dict, output_path : str) -> None:
    """
    inputs: the Dictionaries above
    output_path: starts with current working directory - so you can guide it to whichever page you want it to be in!
    """
    file_loader = FileSystemLoader(Path(template_path).parent)
    env = Environment(loader = file_loader)
    article_html = env.get_template(Path(template_path).name).render(article_dict = inputs)
    with open(output_path, 'w') as file:
        file.write(article_html)

if __name__ == "__main__":
    input_ = article_preprocessing(Path(__file__).parent.joinpath('articles_to_process', 'revisiting_parsing_understat_2.txt'), 'Revisiting Parsing Understat part 2')
    render_article(str(Path(__file__).parent.joinpath('jinja_templates', 'article_template.txt')), input_, str(Path(__file__).parent.joinpath('rendered_templates', 'Maths_Until_18_and_Beyond.html')))
