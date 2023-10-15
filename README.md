3 Competência em Django


Utilizando o Django, crie um sistema que simule o gerenciamento de projetos para diferentes 
empresas.
A aplicação deve permitir a adição/exclusão/edição de novas empresas e projetos, assim como 
a atribuição e exclusão dos usuarios nos projetos criados, deve ser integrada com um banco de 
dados relacional de sua preferência e frontend usando templates, cumprindo os seguintes 
requisitos:
Objetivos:
. Cada usuário passará por uma autenticação simples, apenas com login e senha.
. A página inicial deve conter as empresas cadastradas que o usuário está vinculado.
. A aplicação deverá possibilitar a exibição dos projetos vinculados ao usuário quando for
realizado o acesso à página da empresa.
. Construa o banco de dados com relacionamentos que possam validar o sistema, ou seja:
. Somente o criador da empresa pode excluir a empresa com todos os projetos 
contidos.
. Somente o criador do projeto pode excluí-lo.
. Somente o criador do projeto pode adicionar novas pessoas ou remover as que já 
estão.
. Desenvolva CRUDs básicos, relacionados: um para o controle de usuários e outro para o 
controle dos projetos e empresas.
. Desenvolva o frontend utilizando bibliotecas e frameworks de sua preferência, como por 
exemplo, o bootstrap.
. Crie os seguintes usuários base:
o Caso1: Um usuário que criou uma empresa ( login: user1 | senha: senha_caso1 );
o Caso2: Um usuário que criou três projetos na empresa do Caso1 ( login: user2 | 
senha: senha_caso2 );
o Caso3: Crie dois usuários, um usuário que participa de dois dos projetos criados 
no Caso2 ( login: user3 | senha: senha_caso3 ) e outro que participa de somente 
um ( login: user4 | senha: senha_caso4 ).
o Caso4: Crie mais uma empresa com o usuário do Caso1.
Critérios de avaliação:
 Correto funcionamento da aplicação;
 Estrutura do projeto Django (configuração, aplicativos, modelos, etc.).
 Funcionalidade de formulários para adicionar e editar projetos.
 Organização e clareza do código;
 Uso de templates para renderizar as páginas
