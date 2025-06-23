✨ Orçamentador de Visitas Técnicas ✨

Programa simples e eficiente em Python, projetado para otimizar o cálculo para orçamentos de visitas técnicas. Perfeito para autônomos, pequenas empresas de manutenção ou qualquer um que precise de um controle rápido e claro dos custos de serviço e deslocamento.

🚀 Funcionalidades Principais:

Cálculo Inteligente de Deslocamento: 
🗺️ Calcula automaticamente o custo de ida e volta com base na distância informada e um valor de KM configurável.

Gestão de Múltiplos Equipamentos: 
🛠️ Adicione quantos equipamentos forem necessários para a manutenção em uma única visita, com valores de serviço individualizados.

Orçamento Detalhado e Transparente: 
💰 Apresenta um resumo completo, incluindo o valor do deslocamento, o custo de cada serviço e um Total Geral claro e objetivo.

Validação Robusta de Entradas: 
✅ Evita erros com validação de dados, garantindo que apenas números válidos (e positivos) sejam aceitos para distância e valores de serviço.

⚙️ Como Utilizar
Para colocar o "Orçamentador de Visitas Técnicas" em ação, siga estes passos simples:

Clone o Repositório: Baixe o código para sua máquina.
git clone https://github.com/SeuUsuario/NomeDoSeuRepositorio.git

Lembre-se de substituir SeuUsuario e NomeDoSeuRepositorio pelos dados corretos do seu projeto no GitHub.

Navegue até a Pasta do Projeto:
cd NomeDoSeuRepositorio
Execute o Script Python: Inicie o programa a partir do seu terminal.

python seu_script_principal.py
Seu arquivo principal pode se chamar main.py ou orcamento.py, ajuste conforme necessário.

O programa irá guiá-lo interativamente, solicitando as informações necessárias:
-Cidade: Qual a cidade da visita?
-Distância em Km: Quantos quilômetros até lá (o programa calcula ida e volta)?
-Equipamento com problema: Descreva o equipamento.
-Valor do serviço para [Equipamento]: Qual o custo para o serviço?
-Adicionar outro equipamento? [S/N]: Deseja adicionar mais serviços?

🏗️ Estrutura do Projeto / Funções
O código foi cuidadosamente modularizado para promover a legibilidade e facilitar futuras expansões, seguindo boas práticas de desenvolvimento:

coletar_dados_visita(): 
📥 Responsável por coletar todas as entradas do usuário de forma organizada.
calcular_valores(): 
🧮 Concentra a lógica de cálculo dos custos.
formatar_nomes_equipamentos(): 
📝 Ajuda a criar a lista de equipamentos para a exibição.
exibir_orcamento(): 
📈 Apresenta o resultado final do orçamento de maneira clara e formatada.
main(): 
🔗 A função principal que orquestra o fluxo de execução do programa.

🎨 Personalização Fácil
Quer ajustar os valores padrão? É super fácil! Edite as constantes definidas no início do script para se adequarem às suas necessidades:

CUSTO_KM_UNITARIO: Altere o valor por quilômetro conforme sua política de cobrança.
VALOR_DIA_PAGAMENTO: Modifique o prazo padrão de pagamento (e.g., para "30 DDF").

💡 Exemplo de Uso (Saída no Terminal)
****************** Orçamento da Visita Técnica ******************
Visita técnica em Feliz para manutenção em catraca e relógio.

Valor do deslocamento
R$ 200.00

Valor do serviço catraca
R$ 300.00
Valor do serviço relogio
R$ 100.00

Total dos serviços: R$ 400.00
TOTAL GERAL: R$ 600.00

Pagamento: 28 DDF
**************************************************

🤝 Contribuições
Sinta-se à vontade para abrir issues se encontrar algum problema ou tiver sugestões de melhoria, ou até mesmo enviar pull requests com novas funcionalidades!
