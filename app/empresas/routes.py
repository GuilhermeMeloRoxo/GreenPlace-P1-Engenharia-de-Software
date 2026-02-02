from flask import render_template, send_from_directory, session, flash, redirect, url_for
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
    return "baixar_dados"
