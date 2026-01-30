function alterarCampos() {
    // Ocultar campos dependendo do seu perfil de usuário
    const user_radio = document.getElementById('user');
    const empresa_radio = document.getElementById('empresa');
    const campo_usuario = document.getElementById('campo_usuario');
    const campo_empresa = document.getElementById('campo_empresa');
    const elementosEmpresa = campo_empresa.querySelectorAll('input');
    const elementosUsuario = campo_usuario.querySelectorAll('input');
    // Se a checkbox de usuários estiver marcada
    if (user_radio.checked) {
        // Exibe o campo de usuário comum e esconde o campo de empresas
        campo_usuario.style.display = 'block';
        campo_empresa.style.display = 'none';
        // Itera o campo de empresas e desabilita ele
        elementosEmpresa.forEach(elemento => {
            elemento.disabled = true
        });
        //Itera o campo de usuário comum e habilita ele
        elementosUsuario.forEach(elemento => {
            elemento.disabled = false
        });
    }

    // Se a checkbox de empresas estiver marcada
    else if (empresa_radio.checked) {
        // Exibe o campo de empresas e esconde o campo de usuário comum
        campo_empresa.style.display = 'block';
        campo_usuario.style.display = 'none';
        // Itera o campo de usuário comum e desabilita ele
        elementosUsuario.forEach(elemento => {
            elemento.disabled = true
        });
        //Itera o campo de empresa e habilita ele
        elementosEmpresa.forEach(elemento => {
            elemento.disabled = false
        });
    }
    else {
        campo_usuario.style.display ='none';
        campo_empresa.style.display ='none';
    }
    // Garante que o estado inicial seja configurado corretamente ao carregar a página
    document.addEventListener('DOMContentLoaded', (event) => {
        alterarCampos();
    });
}

// Função para validar pelo menos nome e sobrenome do usuário
function validarDoisNomes(form) {
    const inputNome = form.elements['nome'];
    const valorNome = inputNome.value.trim();
    
    // Divide a string por espaços e retira espaços duplos
    const nomes = valorNome.split;
    
    // Se não tiver dois nomes
    if (nomes.length < 2) {
        // Exibe mensagem pedindo nome completo
        inputNome.setCustomValidity('Por favor, insira o seu nome completo.');
        // Não envia o formulário
        return false; 

    // Se tiver
    } else {
        // Limpa a mensagem pedindo nome completo(se tiver)
        inputNome.setCustomValidity(''); 
        // Envia o formulário
        return true;
    }
}

// ===============================================================
//                      PAGINAÇÃO DE TABELAS
// ===============================================================

class PaginacaoTabela {
    constructor(idTabela, itensPorPagina = 10) {
        this.tabela = document.getElementById(idTabela);
        // Verificar se existe a tabela
        if (!this.tabela) {
            console.warn(`Tabela com ID "${idTabela}" não encontrada. PAginação não será inicializada.`);
            return;
        }

        this.corpoTabela = this.tabela.querySelector('tbody');
        this.itensPorPagina = itensPorPagina;
        this.paginaAtual = 1;
        this.linhas = Array.from(this.corpoTabela.querySelectorAll('tr'));

        // Se a tabela estiver vazia ela não conta na numeração das páginas
        this.linhas = this.linhas.filter(linha => !linha.querySelector('.tabela-vazia'));

        if (this.linhas.length === 0) {
            return;
        }

        this.totalPaginas = Math.ceil(this.linhas.length / this.itensPorPagina);
        this.inicializar();
    }

    inicializar() {
        this.criarControlesPaginacao();
        this.exibirPagina(1);
    }

    exibirPagina(pagina) {
        if (pagina < 1) pagina = 1;
        if (pagina > this.totalPaginas) pagina = this.totalPaginas;

        this.paginaAtual = pagina;

        // Esconde as linhas
        this.linhas.forEach(linha => linha.style.display = 'none');

        // Calcula quais as linhas mostrar
        const inicio = (pagina - 1) * this.itensPorPagina;
        const fim = inicio + this.itensPorPagina;

        // Mostra apenas as linhas das páginas atuais
        this.linhas.slice(inicio, fim).forEach(linha => {
            linha.style.display = '';
        });

        this.atualizarControlesPaginacao();
        this.atualizarInfoEntradas();
    }

    criarControlesPaginacao() {
        const containerPaginacao = document.createElement('div');
        containerPaginacao.className = 'pagination-container'
        containerPaginacao.innerHTML = `
        <div class="pagination-info">
                <span id="info-entradas"></span>
            </div>
            <div class="pagination-controls">
                <button class="pagination-btn" id="primeira-pagina">«</button>
                <button class="pagination-btn" id="pagina-anterior">‹</button>
                <div id="numeros-pagina"></div>
                <button class="pagination-btn" id="proxima-pagina">›</button>
                <button class="pagination-btn" id="ultima-pagina">»</button>
            </div>
            <div class="items-per-page">
                <label for="selecao-itens">Itens por página:</label>
                <select id="selecao-itens">
                    <option value="10" selected>10</option>
                    <option value="25">25</option>
                </select>
            </div>
        `;

        // Insere a parte de passar a página depois da tabela
        const containerTabela = this.tabela.closest('.tabela-container');
        containerTabela.parentNode.insertBefore(containerPaginacao, containerTabela.nextSibling);
        // Adiciona event listeners
        document.getElementById('primeira-pagina').addEventListener('click', () => this.exibirPagina(1));
        document.getElementById('pagina-anterior').addEventListener('click', () => this.exibirPagina(this.paginaAtual - 1));
        document.getElementById('proxima-pagina').addEventListener('click', () => this.exibirPagina(this.paginaAtual + 1));
        document.getElementById('ultima-pagina').addEventListener('click', () => this.exibirPagina(this.totalPaginas));

        document.getElementById('selecao-itens').addEventListener('change', (e) => {
            this.itensPorPagina = parseInt(e.target.value);
            this.totalPaginas = Math.ceil(this.linhas.length / this.itensPorPagina);
            this.exibirPagina(1);
        });
    }

    atualizarControlesPaginacao() {
        const containerNumerosPagina = document.getElementById('numeros-pagina');
        containerNumerosPagina.innerHTML = '';

        let paginaInicial = Math.max(1, this.paginaAtual - 2);
        let paginaFinal = Math.min(this.totalPaginas, this.paginaAtual + 2);

        if (paginaFinal - paginaInicial < 4) {
            if (paginaInicial === 1) {
                paginaFinal = Math.min(this.totalPaginas, paginaInicial + 4);
            } else if (paginaFinal === this.totalPaginas) {
                paginaInicial = Math.max(1, paginaFinal - 4);
            }
        }

        // Primeira página
        if (paginaInicial > 1) {
            const botao = this.criarBotaoPagina(1);
            containerNumerosPagina.appendChild(botao);

            if (paginaInicial > 2) {
                const reticencias = document.createElement('span');
                reticencias.className = 'pagination-dots';
                reticencias.textContent = '...';
                containerNumerosPagina.appendChild(reticencias);
            }
        }

        // Páginas numeradas
        for (let i = paginaInicial; i <= paginaFinal; i++) {
            const botao = this.criarBotaoPagina(i);
            containerNumerosPagina.appendChild(botao);
        }

        // Última página
        if (paginaFinal < this.totalPaginas) {
            if (paginaFinal < this.totalPaginas - 1) {
                const reticencias = document.createElement('span');
                reticencias.className = 'pagination-dots';
                reticencias.textContent = '...';
                containerNumerosPagina.appendChild(reticencias);
            }

            const botao = this.criarBotaoPagina(this.totalPaginas);
            containerNumerosPagina.appendChild(botao);
        }

        // Desabilita botões quando necessário
        document.getElementById('primeira-pagina').disabled = this.paginaAtual === 1;
        document.getElementById('pagina-anterior').disabled = this.paginaAtual === 1;
        document.getElementById('proxima-pagina').disabled = this.paginaAtual === this.totalPaginas;
        document.getElementById('ultima-pagina').disabled = this.paginaAtual === this.totalPaginas;
    }

    criarBotaoPagina(numeroPagina) {
        const botao = document.createElement('button');
        botao.className = 'pagination-btn page-number';
        botao.textContent = numeroPagina;

        if (numeroPagina === this.paginaAtual) {
            botao.classList.add('active');
        }

        botao.addEventListener('click', () => this.exibirPagina(numeroPagina));
        return botao;
    }

    atualizarInfoEntradas() {
        const inicio = (this.paginaAtual - 1) * this.itensPorPagina + 1;
        const fim = Math.min(this.paginaAtual * this.itensPorPagina, this.linhas.length);
        const total = this.linhas.length;

        document.getElementById('info-entradas').textContent =
            `Exibindo ${inicio} a ${fim} de ${total} entradas`;
    }
}

// Inicializa a paginação quando a página carregar
document.addEventListener('DOMContentLoaded', function () {
    // Só inicializa se a tabela de empresas existir
    if (document.getElementById('empresas-table')) {
        new PaginacaoTabela('empresas-table', 10);
    }
});