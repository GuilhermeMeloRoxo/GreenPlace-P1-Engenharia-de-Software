from flask import render_template, send_from_directory, session, flash, redirect, url_for
from . import empresa_bp

@empresa_bp.route('/dados')
def dados():
    """
    lógica da página de dados
    """
    return "dados"

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
