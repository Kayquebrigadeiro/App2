# 🏠 Meus Móveis - Sistema de Controle de Móveis

Sistema web desenvolvido em Django para controle e organização de móveis domésticos com interface profissional e responsiva.

## ✨ Funcionalidades

- 📋 **Listagem de móveis** - Visualização responsiva (tabela no desktop, cards no mobile)
- ➕ **Cadastro de móveis** - Formulário com validação e feedback visual
- ✏️ **Edição de móveis** - Atualização de dados existentes
- 🗑️ **Exclusão de móveis** - Remoção com confirmação
- 📊 **Relatórios financeiros** - Resumo de gastos por cômodo
- 🔍 **Busca simples** - Filtro por nome ou cômodo
- 💬 **Mensagens flash** - Feedback visual para ações do usuário

## 🎨 Interface

- **Design profissional** com Bootstrap 5
- **Responsivo** - Mobile-first design
- **Acessível** - Contraste adequado e navegação por teclado
- **Paleta de cores consistente** - Verde (#0F6B66) como cor primária
- **Tipografia moderna** - Google Fonts (Inter)

## 🚀 Como executar

### Pré-requisitos
- Python 3.8+
- Django 4.0+

### Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/Kayquebrigadeiro/App2.git
   cd App2
   ```

2. **Navegue para o diretório do projeto**
   ```bash
   cd meus_moveis_web
   ```

3. **Execute as migrações**
   ```bash
   python manage.py migrate
   ```

4. **Crie um superusuário (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Inicie o servidor**
   ```bash
   python manage.py runserver
   ```

6. **Acesse o sistema**
   - Sistema: http://127.0.0.1:8000
   - Admin: http://127.0.0.1:8000/admin

## 📱 Rotas Disponíveis

- `/` - Página inicial
- `/listar/` - Lista de móveis
- `/novo/` - Cadastrar novo móvel
- `/editar/<id>/` - Editar móvel
- `/excluir/<id>/` - Excluir móvel
- `/relatorios/` - Resumo financeiro

## 💰 Formatação de Moeda

O sistema utiliza formatação brasileira para valores monetários (R$ 1.234,56) através de template filter customizado.

## 🎯 Estrutura do Projeto

```
meus_moveis_web/
├── meus_moveis_web/          # Configurações do projeto
├── moveis/                   # App principal
│   ├── templatetags/         # Filtros customizados
│   ├── forms.py             # Formulários
│   ├── models.py            # Modelos de dados
│   └── views.py             # Lógica de negócio
├── templates/               # Templates HTML
│   ├── includes/            # Componentes reutilizáveis
│   ├── base.html           # Layout base
│   ├── index.html          # Página inicial
│   ├── move_list.html      # Lista de móveis
│   ├── move_form.html      # Formulário
│   └── relatorios.html     # Relatórios
└── static/
    └── css/
        └── site.css        # Estilos customizados
```

## 🔧 Tecnologias Utilizadas

- **Backend**: Django 6.0
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Banco de dados**: SQLite
- **Tipografia**: Google Fonts (Inter)
- **Ícones**: Emojis nativos

## 📊 Capturas de Tela

Para visualizar o sistema:

1. Execute `python manage.py runserver`
2. Acesse as rotas:
   - **Desktop**: http://127.0.0.1:8000/listar/
   - **Mobile**: Redimensione o navegador para < 768px
   - **Formulário**: http://127.0.0.1:8000/novo/

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Desenvolvido com ❤️ usando Django e Bootstrap**