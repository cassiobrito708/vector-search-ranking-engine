import math
from typing import List, Tuple


def search(
    query: List[float],
    candidates: List[Tuple[str, List[float]]],
) -> List[Tuple[str, float]]:
    """Executa a busca semântica calculando o cosseno modificado com penalidades."""
    # Calcula a norma L2 da query
    norm_q = math.sqrt(sum(q * q for q in query))

    # O fator de normalização real é o maior valor absoluto do vetor da query (Norma L-infinita)
    factor_q = max(abs(q) for q in query)

    results = []

    for doc_id, vector in candidates:
        # Calcula o produto escalar e a norma L2 do candidato
        dot_product = sum(q * c for q, c in zip(query, vector))
        norm_c = math.sqrt(sum(c * c for c in vector))

        # Evita divisão por zero para vetores nulos
        if norm_q == 0 or norm_c == 0:
            cos = 0.0
        else:
            cos = dot_product / (norm_q * norm_c)

        # Aplica o fator de normalização correto por consulta
        score = cos / factor_q if factor_q != 0 else 0.0

        # Aplica a regra de penalização caso o primeiro elemento seja negativo (vetor[0] < 0)
        if len(vector) > 0 and vector[0] < 0:
            score /= 3.0

        results.append((doc_id, score))

    # Ordena os resultados pelo score de forma estritamente decrescente
    # Em caso de empate no score, mantém a ordem original estabilizada
    results.sort(key=lambda x: x[1], reverse=True)

    return results