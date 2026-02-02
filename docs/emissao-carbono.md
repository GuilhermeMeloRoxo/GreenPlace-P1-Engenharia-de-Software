Médias:

Média de emissão mundial: 400 kg de CO2 por pessoa
Média de emissão ideal: 200 kg de CO2 por pessoa
Média de consumo de energia elétrica no brasil: 225 kWh/mês / ~17 kg de CO2 mensal (100 kWh/mês ~= 7,5 kg)
Média de tempo de banho no brasil: 10h/mês (2 banhos de 10 min por dia) / ~36 kg de CO2 mensal (10 min ~= 600 g)
Média quilometragem carro: 1000 km/mês / ~169 kg de CO2 mensal (100 km ~= 16,9 kg)
Média quilometragem moto: 475 km/mês / ~22 kg de CO2 mensal (100 km ~= 4,8 kg)
Média km pessoal de ônibus: 300 km/mês / ~26 kg de CO2 mensal (100 km ~= 9 kg)
Lâmpadas: Iluminação representa ~10% do valor de energia. Lâmpadas LED economizam cerca de 4 vezes mais (em relação à uma média de consumo de energia de lâmpadas incandescentes e fluorescentes).
Litros de água: 1000 litros ~= 0.15 kg de CO2
Média dieta carne vermelha: 6 kg/mês (200g de carne diária)/ ~360 kg de CO2 mensal (200 g ~= 12 kg)
Média dieta vegetariana: 114 kg de CO2 mensal (3.8 kg diário)
Custo de transporte alimentar: Em torno de 6% da emissão total de carbono no sistema alimentar
Média de redução de CO2 em caso de reciclagem doméstica: 60 kg de CO2 mensal 
Média de redução de CO2 caso separe o lixo: 15 kg de CO2 mensal
Média descarte de lixo eletrônico de forma errada: 0.5 kg / 0.35 kg de CO2 mensal
Média descarte de lixo eletrônico de forma correta: 0.5 kg / 0.15 kg de CO2 mensa



Lógica da soma de emissão de carbono:
Sempre criar uma variável específica para o tratamento de CO2 emitido no field, para caso seja necessário de tratamento por modificadores para aumentar ou diminuir. Assim que passar completamente por um field, adicionar o valor do field à uma variável de Emissão_Total. O aumento ou redução dos valores serão especificados em seu field apropriado.

Field Transporte: Caso responda carro ou moto, verificar o campo “transporte_público”, caso seja “sempre”, adicionar metade do valor padrão do carro/moto e metade do valor padrão de ônibus, caso seja “as vezes”, adicionar 70% de carro/moto e 30% de ônibus, caso seja “raramente”, 90% carro/moto e 10% ônibus, caso seja “nunca”, adicionar 100% do valor padrão carro/moto.
Caso seja ônibus, bicicleta ou a pé, verificar no campo de transporte público: “sempre” mantém o valor padrão do ônibus, “as vezes” diminui o valor em 40%, “raramente” reduz em 70% e nunca zera o valor padrão do ônibus.
Valores padrão de “bicicleta” e “a pé” são ambos 0.
Valores para carona: “sempre” deve remover 15% do valor total dos passos anteriores, “as vezes” deve remover 5% e “nunca” não deve remover nada.

Field Energia: O valor padrão deve ser aplicado caso a resposta de “apagar as luzes” seja “sempre”. Deve adicionar 5% no caso de “as vezes” e 15% em caso de “nunca”. Dividir o valor de energia elétrica e separar três partes do total com uma parte de 10% do total outra parte de 75% do total e outra variável de 15% em variáveis distintas, Caso campo “lâmpadas” seja “todas”: pegar a variável de 10% e dividir por 4. Caso seja “alguns”, manter o valor como está e caso seja “não uso”, multiplicar por 2. No campo de selo de energia, caso marque “sim”, pegar a variável de 75% e reduzir em 30% do valor guardado na variável, caso seja “não” ou “não sei” manter o valor como está. Caso o campo “tirar da tomada” seja “sempre	“ reduzir em 10% na variável de 75%, caso seja “as vezes”, reduzir em 5%.

Field Água: Caso a resposta do campo “banho” seja “ate_5”, aplicar metade do valor padrão, caso seja “5_10” aplicar o valor padrão, caso seja “mais_10” aplicar 150% do valor padrão.
Caso a resposta do campo “fechar_torneira” seja “sempre”, reduzir 0.15 do valor do field, caso seja “as vezes” manter o valor e caso seja “nunca”, aumentar o valor em 0.15.
Caso a resposta para o campo “reuso_agua” seja “sempre” reduzir 0.90 do valor do field, caso seja “as vezes” reduzir em 0.30, caso seja “nunca” manter o valor como está”.

Field Alimentação: Caso o campo “carne” seja “diario”, aplicar o valor padrão de carne vermelha, caso seja “semanal” aplicar 40% do valor padrão de carne e 60% do valor padrão vegetariano, caso seja “raramente”, aplicar 80% do valor vegetariano e 20% do valor de carne, caso seja “nunca” aplicar apenas o valor vegetariano.
Caso o campo “alimento_local” seja “sempre”, reduzir o valor do field em 6%, caso seja “as_vezes” reduzir em 3%, caso seja “nunca” manter o valor.

Field Resíduos: Caso o campo “reciclagem” seja “sempre”, reduzir do field resíduos o valor padrão de reciclagem, caso seja “as_vezes” reduzir metade do valor padrão, caso seja “nunca” manter como está.
Caso o campo “separar_residuos” seja “sim”, reduzir o valor padrão de separação de resíduos, caso seja “as_vezes”, reduzir metade do valor padrão, caso seja “nao”, manter como está.
Caso o campo “lixo_eletronico” seja “sempre”, adicionar o valor padrão de descarte correto, caso seja “as_vezes” adicionar metade do valor correto e metade do valor incorreto, caso seja “nunca”, adicionar o valor padrão de descarte incorreto


Lógica do cálculo de pontuação:
Caso o valor seja maior ou igual à (media_mundial * 1.5): Atribuir zero
Caso o valor seja abaixo da média mundial, aplicar o cálculo: [(media_mundial - emissao_final) / 4] + 62.5
Caso o valor seja acima da média mundial, aplicar: [(emissao_final - media_mundial) / 4] - 62.5




Fontes:

Emissões Globais
IPCC – Metas de emissão para 1,5°C - ipcc.ch/sr15
Our World in Data – Médias mundiais de CO₂ per capita -ourworldindata.org/co2-emissions

Energia no Brasil
EPE – Consumo residencial de energia - epe.gov.br
MCTI – Fator de emissão da eletricidade - gov.br/mcti

Água e Banho
SNIS – Tempo médio de banho no Brasil - snis.gov.br
Water Footprint Network – Emissão do tratamento de água - waterfootprint.org

Transporte
ANP – Emissões de carros e motos - gov.br/anp
IEMA – Emissões do transporte público - energiaeambiente.org.br

Alimentação
Embrapa – Pegada de carbono da carne - embrapa.br
FAO – Impacto do transporte de alimentos - fao.org
Estudo da Science – Comparação de dietas - science.org/doi/10.1126/science.aaq0216

Resíduos
CEMPRE – Redução de CO₂ com reciclagem - cempre.org.br
ABRELPE – Impacto da separação do lixo - abrelpe.org.br
Green Eletron – Descarte de lixo eletrônico - greeneletron.org.br

Diretrizes e Métodos
IPCC (2006) – Guia para emissões do transporte - ipcc-nggip.iges.or.jp
Governo Federal – Eficiência energética em edificações - gov.br/produtividade
