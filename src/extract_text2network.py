from networkx import DiGraph
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def preprocess_text(text: str ) -> list[list[str]]:
    """
    Preprocesa el texto proporcionado realizando separación de oraciones, tokenización, limpieza, normalización y eliminación de palabras vacías.

    Args:
        text (str): El texto que se va a preprocesar.

    Returns:
        list: Una lista de palabras preprocesadas (tokens).
    """

    sentences: list = sent_tokenize(text)
    preprocessed_sentences: list = []
    for sentence in sentences:
        # Tokenización
        tokens: list = word_tokenize(sentence)
        # Limpieza y normalización
        words: list = [token.lower() for token in tokens if token.isalpha()]
        # Eliminación de palabras vacías
        filtered_words: list = [word for word in words if word not in stopwords.words('spanish')]
        preprocessed_sentences.append(filtered_words)
    return preprocessed_sentences


def analyze_cooccurrence(sentences: list[str], window_size: int =1) -> list[tuple]:
    """
    Analiza las co-ocurrencias de palabras en una lista de palabras preprocesadas, dada una ventana de co-ocurrencia específica.

    Args:
        words (list): Lista de palabras preprocesadas.
        window_size (int): El tamaño de la ventana de co-ocurrencia. Por defecto es 1, lo que significa que solo se considera la palabra siguiente.

    Returns:
        list: Lista de tuplas representando las co-ocurrencias de palabras.
    """
    cooccurrences: list[str] = []
    for sentence in sentences:
        for i in range(len(sentence) - window_size):
            current_word = sentence[i]
            for j in range(1, min(window_size + 1, len(sentence) - i)):
                cooccurrences.append((current_word, sentence[i + j]))
    
    return cooccurrences


def build_network(cooccurrences: list[tuple]) -> DiGraph:
    """
    Construye una red dirigida a partir de una lista de co-ocurrencias de palabras.

    Args:
        cooccurrences (list): Lista de tuplas que representan las co-ocurrencias de palabras.

    Returns:
        DiGraph: Un objeto de grafo de NetworkX representando la red dirigida construida.
    """

    G: DiGraph = DiGraph()
    for word1, word2 in cooccurrences:
        if not G.has_edge(word1, word2):
            G.add_edge(word1, word2, weight=0)
        G[word1][word2]['weight'] += 1
    return G

def text2network(text: str)-> DiGraph:
    preprocessed_text = preprocess_text(text)
    cooccurrences = analyze_cooccurrence(preprocessed_text, window_size=1)
    return build_network(cooccurrences)

if __name__ == '__main__':
    import json 
    import networkx as nx
    import matplotlib.pyplot as plt

    from models import Libro, Pagina
    
    JSON_EXTRACTED_PATH = "data/pre_processed/proyecto-ley-reforma-salud-msps.json"
    
    with open(JSON_EXTRACTED_PATH, 'r', encoding='utf-8') as json_data:
        json_string: str = json.load(json_data)
        dict_data: dict = json.loads(json_string)
    
    book: Libro = Libro(**dict_data)
    print(book.nombre)
    
    # iterate over the contento to extract the network
    
    coocurrences_all = []
    for pagina in book.contenido:
        
        preprocessed_text = preprocess_text(pagina.contenido)
        cooccurrences_sentences = analyze_cooccurrence(preprocessed_text, window_size=1)
        coocurrences_all += cooccurrences_sentences

    network = build_network(coocurrences_all)
    
    nx.write_graphml(network, 'directed_network.graphml')

    
    