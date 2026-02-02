from flask import render_template, request, redirect, url_for, session, flash
from datetime import datetime
from . import user_bp
import os
import csv


data_dir =  'data'
respostas_file = os.path.join(data_dir, 'respostas_questionario.csv')

@user_bp.route('/questionario', methods=['GET', 'POST'])
def questionario():
    '''
    Rota GET/POST /questionario
    Exibe o questionário e processa autenticação
    '''
    if request.method == 'POST':
        # Processa os dados do questionário aqui
        # Obtém data(dia/mês/ano) da resposta
        data_atual = datetime.now().strftime('%d/%m/%Y')

        #Valores padrão para emissão de carbono com valores em Kg(especificados na documentação)
        padrao_carro = 169
        padrao_moto = 22
        padrao_onibus = 26
        padrao_agua = 36
        padrao_energia = 17
        padrao_carne_vermelha = 360
        padrao_vegetariano = 114
        padrao_reciclagem = 60
        padrao_residuos = 15
        padrao_eletronico_correto = 0.35
        padrao_eletronico_incorreto = 0.15
        media_mundial = 400

        # Lógica de cálculo da emissão de carbono
        emissao_final = 0
        #Field Tranporte
        field_transporte = 0
        transporte = request.form.get('transporte')
        transporte_publico = request.form.get('transporte_publico')
        carona = request.form.get('carona')

        if transporte == "carro":
            if transporte_publico == 'sempre':
                field_transporte += padrao_carro * 0.5
                field_transporte += padrao_onibus * 0.5
            elif transporte_publico == 'as_vezes':
                field_transporte += padrao_carro * 0.7
                field_transporte += padrao_onibus * 0.3
            elif transporte_publico == 'raramente':
                field_transporte += padrao_carro * 0.9
                field_transporte += padrao_onibus * 0.1
            elif transporte_publico == "nunca":
                field_transporte += padrao_carro

        elif transporte == 'moto':
            if transporte_publico == 'sempre':
                field_transporte += padrao_moto * 0.5
                field_transporte += padrao_onibus * 0.5
            elif transporte_publico == 'as_vezes':
                field_transporte += padrao_moto * 0.7
                field_transporte += padrao_onibus * 0.3
            elif transporte_publico == 'raramente':
                field_transporte += padrao_moto * 0.9
                field_transporte += padrao_onibus * 0.1
            elif transporte_publico == "nunca":
                field_transporte += padrao_moto  

        else:
            if transporte_publico == 'sempre':
                field_transporte += padrao_onibus
            elif transporte_publico == 'as_vezes':
                field_transporte += padrao_onibus - (padrao_onibus * 0.4)
            elif transporte_publico == 'raramente':
                field_transporte += padrao_onibus - (padrao_onibus * 0.7)

        
        
        if carona == "sempre":
            field_transporte -= field_transporte * 0.15
        elif carona == 'as_vezes':
            field_transporte -= field_transporte * 0.05

        #Fim do Field Transporte
        emissao_final += field_transporte
        #Field Energia
        field_energia = 0
        apagar_luzes = request.form.get('apagar_luzes')
        lampadas = request.form.get('lampadas')
        selo_energia = request.form.get('selo_energia')
        tirar_tomada = request.form.get('tirar_tomada')
        if apagar_luzes == 'sempre':
            field_energia += padrao_energia
        elif apagar_luzes == 'as vezes':
            field_energia += padrao_energia + (padrao_energia * 0.05)
        elif apagar_luzes == 'nunca':
            field_energia += padrao_energia + (padrao_energia * 0.15)

        #Dividindo o field de energia em partes para trabalhar nos cálculos
        field_energia_10 = field_energia * 0.1
        field_energia_75 = field_energia * 0.75
        field_energia_15 = field_energia * 0.15

        if lampadas == 'todas':
            field_energia_10 = field_energia_10 / 4
        elif lampadas == 'nao_uso':
            field_energia_10 = field_energia_10 * 2
        
        if selo_energia == 'sim':
            field_energia_75 =  field_energia_75 - (field_energia_75 * 0.3)
        if tirar_tomada == 'sempre':
            field_energia_75 = field_energia_75 - (field_energia_75 * 0.1)
        elif tirar_tomada == 'as_vezes':
            field_energia_75 = field_energia_75 - (field_energia_75 * 0.05)
        
        field_energia = field_energia_75 + field_energia_10 + field_energia_15
        #Fim do Field Energia
        emissao_final += field_energia
        #Field Água
        field_agua = 0
        banho = request.form.get('banho')
        fechar_torneira = request.form.get('fechar_torneira')
        reuso_agua = request.form.get('reuso_agua')
        if banho == "ate_5":
            field_agua += padrao_agua * 0.5
        elif banho == "5_10":
            field_agua += padrao_agua
        else:
            field_agua += padrao_agua * 1.5
        
        if fechar_torneira == "sempre":
            field_agua -= 0.15
        elif fechar_torneira == "nunca":
            field_agua += 0.15

        if reuso_agua == "sempre":
            field_agua -= 0.9
        elif reuso_agua == "as_vezes":
            field_agua -= 0.3

        #Fim do Field Água
        emissao_final += field_agua
        #Field Alimentação
        field_alimentacao = 0
        carne = request.form.get('carne')
        alimento_local = request.form.get('alimento_local')
        if carne == 'diario':
            field_alimentacao += padrao_carne_vermelha
        elif carne == 'semanal':
            field_alimentacao += (padrao_vegetariano * 0.6) + (padrao_carne_vermelha * 0.4)
        elif carne == 'raramente':
            field_alimentacao += (padrao_vegetariano * 0.8)+(padrao_carne_vermelha * 0.2)
        else:
            field_alimentacao += padrao_vegetariano
        
        if alimento_local == 'sempre':
            field_alimentacao -= field_alimentacao*0.06
        elif alimento_local == 'as_vezes':
            field_alimentacao -= field_alimentacao*0.03
        
        #Fim do Field Alimentação
        emissao_final += field_alimentacao
        #Field de Resíduos
        field_residuos = 0
        reciclagem = request.form.get('reciclagem')
        separar_residuos = request.form.get('separar_residuos')
        lixo_eletronico = request.form.get('lixo_eletronico')
        if reciclagem == 'sempre':
            field_residuos -= padrao_reciclagem
        elif reciclagem == 'as_vezes':
            field_residuos -= padrao_reciclagem * 0.5
        
        if separar_residuos == 'sim':
            field_residuos -= padrao_residuos
        elif separar_residuos == 'as_vezes':
            field_residuos -= padrao_residuos * 0.5
        
        if lixo_eletronico == 'sempre':
            field_residuos += padrao_eletronico_correto
        elif lixo_eletronico == 'as_vezes':
            field_residuos += (padrao_eletronico_correto + padrao_eletronico_incorreto)/2
        else:
            field_residuos += padrao_eletronico_incorreto
        
        #Fim do Field Resíduos
        emissao_final += field_residuos
        #Arredondando o valor para duas casas decimais
        emissao_final = round(emissao_final, 2)
        
        #Calculo da pontuação
        if emissao_final >= media_mundial * 1.5:
            pontuacao = 0
        elif emissao_final < media_mundial:
            pontuacao = ((media_mundial - emissao_final)/4) + 62.5
        else:
            pontuacao = ((emissao_final - media_mundial)/4) - 62.5
        #Arredondando o valor da pontuação para inteiro
        pontuacao = round(pontuacao)
        
        campos = ['data', 'idade', 'genero', 'renda', 'estado', 'emissao_carbono', 'pontuacao']
        with open(respostas_file, mode='a',  encoding='utf-8', newline='') as arquivo_csv:
            escrever = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';')
            dados_respostas = {
                'data': data_atual,
                'idade': request.form.get('idade'),
                'genero': request.form.get('genero'),
                'renda': request.form.get('renda'),
                'estado': request.form.get('estado'),
                'emissao_carbono': str(emissao_final),
                'pontuacao': str(pontuacao),
            }
            escrever.writerow(dados_respostas)
        flash('Obrigado por contribuir com suas respostas!', 'success')
        username = session.get('username')
        return render_template('resultado.html', pontuacao=pontuacao, emissao=emissao_final, username=username)
    return render_template('questionario.html')

@user_bp.route('/logout')
def logout_usuario():
    session.pop('user_role', None)
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('index'))


