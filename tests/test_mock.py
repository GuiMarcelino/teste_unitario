from unittest import TestCase

from unittest.mock import Mock, patch

from mock_exemplo import cadastra_nome

class TesteMockExemplo(TestCase):

    @patch('mock_exemplo.input_nome')
    def test_cadastra_nome(self, mock_funcao_input_nome):
        # arrange(organizar)
        mock_funcao_input_nome.return_value = 'Guilherme'

        # action(ação)
        resultado = cadastra_nome()

        #assertions (afirmações)
        self.assertEqual('Guilherme', resultado)
        mock_funcao_input_nome.assert_called_once_with()


