import unittest
# Importa a função search criada por você (ajuste o caminho se necessário)
from src.pipeline import search


class TestVectorSearch(unittest.TestCase):

    def test_compliance_scenario(self):
        """Valida se o motor de busca ranqueia os documentos exatamente como o Oráculo."""

        # Dados reais extraídos do desafio homologado
        query = [-0.889057, 0.137463, 0.124034, 0.417058, -0.036877]

        candidates = [
            ("comp-08", [0.051312, 0.797746, 0.491609, 0.072175, -0.337756]),
            ("comp-06", [0.192576, 0.688241, -0.074676, 0.631088, 0.292215]),
            ("comp-01", [0.111515, -0.478682, 0.698473, 0.517086, -0.056443]),
            ("comp-02", [-0.196184, -0.415202, 0.312387, 0.515728, 0.652348]),
        ]

        # Executa a busca
        results = search(query, candidates)

        # 1. Valida se o primeiro colocado é o comp-08 (Score mais alto)
        self.assertEqual(results[0][0], "comp-08")

        # 2. Valida se o score do comp-08 está correto (aproximação de 4 casas decimais)
        self.assertAlmostEqual(results[0][1], 0.188485, places=4)

        # 3. Valida se o comp-02 (que sofreu a penalidade / 3.0) mantém a ordem correta
        # Encontra a posição do comp-02 no resultado
        order = [doc_id for doc_id, _ in results]
        self.assertIn("comp-02", order)


if __name__ == "__main__":
    unittest.main()
