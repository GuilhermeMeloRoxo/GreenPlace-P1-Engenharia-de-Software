from flask import render_template, request, redirect, url_for, session, flash
from . import user_bp

@user_bp.route('/questionario', methods=['GET', 'POST'])
def questionario():
    '''
    lógica do formulário
    '''
    return render_template('questionario.html')

@user_bp.route('/logout')
def logout_usuario():
    session.pop('user_role', None)
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('index'))


