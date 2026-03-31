from langchain_community.document_loaders import YoutubeLoader

def load_transcript(url):
    loader = YoutubeLoader.from_youtube_url(url)
    docs = loader.load()
    return docs