from flask import render_template, send_from_directory, session, flash, redirect, url_for, send_file
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from . import empresa_bp
import os
import csv


data_dir =  'data'
respostas_file = os.path.join(data_dir, 'respostas_questionario.csv')

@empresa_bp.route('/dados')
def dados():
    """
    Rota GET da página de dados
    """
    if session.get('user_role') == 'empresa':
        with open(respostas_file, mode='r', encoding='utf-8') as arquivo_csv:
            # Armazena os dados em um dicionário
            leitor = csv.DictReader(arquivo_csv, delimiter=';')
            lista = []
            for linha in leitor:
                lista.append(linha)
        return render_template('empresas.html', respostas=lista)
    else:
        flash('Por favor, faça o login como empresa para prosseguir.')
        return redirect(url_for('index'))

@empresa_bp.route('/logout')
def logout_empresa():
    session.pop('user_role', None)
    flash('Logout realizado com sucesso', 'success')
    return redirect(url_for('index'))

@empresa_bp.route('/download')
def baixar_dados():
    """
    lógica para baixar_dados
    """
    caminho_csv = os.path.join('data', 'respostas_questionario.csv')
    caminho_pdf = os.path.join('data', 'relatorio_geral.pdf')

    if not os.path.exists(caminho_csv):
        return "Arquivo CSV ainda não existe", 404

    dados = []

    # Lê o CSV
    with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
        leitor = csv.reader(csvfile, delimiter=';')
        for linha in leitor:
            dados.append(linha)

    pdf = SimpleDocTemplate(caminho_pdf, pagesize=A4)
    elementos = []

    tabela = Table(dados, repeatRows=1)

    estilo = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('ALIGN', (0,1), (-1,-1), 'CENTER'),
    ])

    tabela.setStyle(estilo)
    elementos.append(tabela)

    pdf.build(elementos)

    return send_file(caminho_pdf, as_attachment=True)