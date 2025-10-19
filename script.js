// ===== Funcionalidade das Abas =====
document.addEventListener('DOMContentLoaded', function() {
    // Obter todos os botões de aba
    const tabButtons = document.querySelectorAll('.tab-btn');
    
    // Adicionar evento de clique a cada botão
    tabButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Obter o ID da aba a ser exibida
            const tabId = this.getAttribute('data-tab');
            
            // Remover classe 'active' de todos os botões e conteúdos
            tabButtons.forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
            });
            
            // Adicionar classe 'active' ao botão clicado e seu conteúdo
            this.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });
    
    // Inicializar o highlight.js para colorir código
    if (typeof hljs !== 'undefined') {
        hljs.highlightAll();
    }
});

// ===== Scroll Suave para Links de Navegação =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        
        // Ignorar links que não apontam para seções
        if (href === '#') return;
        
        e.preventDefault();
        
        const target = document.querySelector(href);
        if (target) {
            const offsetTop = target.offsetTop - 70; // Ajustar para a altura da navbar
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// ===== Efeito de Scroll na Navbar =====
let lastScrollTop = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', function() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    if (scrollTop > 100) {
        navbar.style.boxShadow = '0 5px 20px rgba(0, 0, 0, 0.5)';
    } else {
        navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.3)';
    }
    
    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
});

// ===== Copiar Código para Clipboard =====
function addCopyButtons() {
    const codeBlocks = document.querySelectorAll('pre code');
    
    codeBlocks.forEach(codeBlock => {
        const pre = codeBlock.parentElement;
        
        // Criar botão de cópia
        const copyButton = document.createElement('button');
        copyButton.className = 'copy-btn';
        copyButton.textContent = 'Copiar';
        copyButton.style.cssText = `
            position: absolute;
            top: 10px;
            right: 10px;
            padding: 5px 10px;
            background-color: #5865F2;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            font-size: 12px;
            font-weight: 600;
            transition: all 0.3s ease;
            z-index: 10;
        `;
        
        // Adicionar evento de clique
        copyButton.addEventListener('click', function() {
            const text = codeBlock.textContent;
            navigator.clipboard.writeText(text).then(() => {
                copyButton.textContent = 'Copiado!';
                setTimeout(() => {
                    copyButton.textContent = 'Copiar';
                }, 2000);
            }).catch(err => {
                console.error('Erro ao copiar:', err);
            });
        });
        
        // Adicionar estilo de posicionamento relativo ao pre
        pre.style.position = 'relative';
        pre.appendChild(copyButton);
    });
}

// Chamar função após o DOM estar carregado
document.addEventListener('DOMContentLoaded', addCopyButtons);

// ===== Animação de Entrada dos Elementos =====
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.animation = 'fadeIn 0.6s ease forwards';
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.step, .download-card').forEach(el => {
        el.style.opacity = '0';
        observer.observe(el);
    });
});

// ===== Verificação de Suporte a Recursos =====
console.log('Script carregado com sucesso!');
console.log('Versão: 1.0.0');

