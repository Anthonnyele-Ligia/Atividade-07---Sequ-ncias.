import matplotlib.pyplot as plt
import numpy as np

class VisualizadorMapeamentoLogistico:
    """
    Uma classe para calcular, estilizar e plotar o mapeamento logístico para
    diferentes valores do parâmetro 'k'.

    Esta classe encapsula toda a lógica, desde a geração dos dados
    até a customização e exibição do gráfico final.
    """

    def __init__(self, k_valores, p1, n_geracoes):
        """
        Inicializa o visualizador com os parâmetros necessários.
        """
        self.k_valores = k_valores
        self.p1 = p1
        self.n_geracoes = n_geracoes
        self.iteracoes = range(1, n_geracoes + 1)
        # Calcula todas as sequências de uma vez e as armazena
        self.sequencias_calculadas = self._gerar_todas_sequencias()

    def _gerar_sequencia(self, k):
        """
        Gera a sequência para um único valor de k.
        """
        populacao = [self.p1]
        p_n = self.p1
        for _ in range(1, self.n_geracoes):
            p_n_proximo = k * p_n * (1 - p_n)
            populacao.append(p_n_proximo)
            p_n = p_n_proximo
        return populacao

    def _gerar_todas_sequencias(self):
        """
        Cria um dicionário com os resultados para todos os valores de k.
        """
        return {k: self._gerar_sequencia(k) for k in self.k_valores}

    def plotar(self):
        """
        Cria e exibe os gráficos com o novo tema.
        """
        num_plots = len(self.k_valores)
        # Configura a figura com fundo branco
        fig, axs = plt.subplots(
            num_plots, 1, 
            figsize=(12, 4 * num_plots), 
            sharex=True,
            facecolor='white'
        )

        # Título principal com cor escura
        fig.suptitle(
            'Análise do Mapeamento Logístico',
            fontsize=20,
            color='#333333'
        )
        
        # Paleta de cores profissional para fundo claro
        cores_claras = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

        for i, (k, sequencia) in enumerate(self.sequencias_calculadas.items()):
            ax = axs[i]
            cor_atual = cores_claras[i]

            # --- Aplicação do Estilo Claro ---
            ax.set_facecolor('#f0f0f0')  # Fundo do gráfico levemente acinzentado
            ax.grid(True, color='lightgray', linestyle='--')
            ax.tick_params(colors='#333333') # Cor dos números nos eixos
            for spine in ax.spines.values():
                spine.set_color('gray') # Cor das bordas do gráfico

            # Plotagem dos dados
            ax.plot(self.iteracoes, sequencia, 'o-', markersize=4, color=cor_atual, label=f'k = {k}')

            # Títulos e rótulos
            ax.set_title(f'Comportamento para k = {k}', color='#333333')
            ax.set_ylabel('População ($p_n$)', color='#333333')
            ax.set_ylim(0, 1.05)

            # Estilo da legenda para o tema 
            leg = ax.legend(loc='upper right')
            leg.get_frame().set_facecolor('white')
            leg.get_frame().set_edgecolor('gray')
            for text in leg.get_texts():
                text.set_color('#333333')

        # Rótulo final do eixo X
        axs[-1].set_xlabel('Geração (n)', color='#333333', fontsize=12)
        
        # Ajusta o layout e exibe o gráfico
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.show()


# --- Bloco de Execução Principal ---
# A boa prática em Python é rodar o código dentro deste bloco.
if __name__ == "__main__":
    
    # Define os parâmetros de entrada
    parametros_simulacao = {
        "k_valores": [2.5, 3.3, 3.5, 4.0],
        "p1": 0.5,
        "n_geracoes": 100
    }
    
    # Cria uma instância da classe e manda plotar
    visualizador = VisualizadorMapeamentoLogistico(**parametros_simulacao)
    visualizador.plotar()