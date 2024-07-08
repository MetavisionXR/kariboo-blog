from jinja2 import Template
import codecs
from pathlib import Path
from slugify import slugify
from tqdm import tqdm
import os
import shutil
from supabase import create_client, Client


supabase_url = os.environ['SUPABASE_URL']
supabase_service_role_key = os.environ['SUPABASE_SERVICE_ROLE_KEY']

client: Client = create_client(supabase_url=supabase_url, supabase_key=supabase_service_role_key)

response = client.table('movie_catalog')\
    .select("title, poster_landscape_url, trailer_url")\
    .eq("active", True)\
    .execute()

slugs = []

for item in os.listdir("../content"):
        item_path = os.path.join("../content", item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)



for idx, row in enumerate(tqdm(response.data)):
    movie_title = row["title"]
    poster_url = row["poster_landscape_url"]
    trailer_url = row["trailer_url"]

    template_data = {}
    template_data["movie_title"] = movie_title
    template_data["poster_url"] = poster_url
    template_data["trailer_url"] = trailer_url

    with open("template.md", "r") as file:
        template = Template(file.read(), trim_blocks=True)
    rendered_file = template.render(template_data=template_data)

    count = 1
    while True:
        slug = slugify(movie_title)
        if count > 1:
            slug += f"-{count}"

        if slug in slugs:
            count += 1
            continue

        slugs.append(slug)
        break

    Path(f"../content/{slug}").mkdir(parents=True, exist_ok=True)

    output_file = codecs.open(f"../content/{slug}/index.md", "w", "utf-8")
    output_file.write(rendered_file)
    output_file.close()
