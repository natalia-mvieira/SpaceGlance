# *SpaceGlance*

O projeto SpaceGlance cria uma galeria de imagens do espaço, dentro da qual é possível visualizar imagens e seus detalhes, além de adicionar novas fotos e fazer edições.

A página foi criada utilizando-se a linguagem **Python**, com o uso do *framework* **Django**.

O site apresenta as seguintes rotas:

### Home:
Nesta página, é onde se visualiza as imagens da galeria, além de ser possível buscar imagens pelo campo de busca e pelos filtros (*tags*). 

As imagens aparecem em *cards* contendo o nome da foto, legenda e a categoria (canto superior direito) à qual pertencem.

Se o usuário estiver logado, o menu lateral terá as opções de adição de nova imagem e de sair (*logout*):

<div align="center">
    <img src="https://github.com/natalia-mvieira/SpaceGlance/assets/144560412/2f5bd6eb-a848-4617-8139-550b8845a153" width="700px"/>
</div>

Se o usuário não estiver logado, é possível apenas a visualização, sendo que o menu lateral permite direcionamento para a página de cadastro ou login:

<div align="center">
    <img src="https://github.com/natalia-mvieira/SpaceGlance/assets/144560412/532255ba-9cd8-44d5-96be-334ffba0f176" width="700px"/>
</div>

### Cadastro:
Permite a criação de uma nova conta, com sistema de checagem de senhas e de verificação de e-mail:

<div align="center">
    <img src="https://github.com/natalia-mvieira/SpaceGlance/assets/144560412/b7e59a71-90f2-4351-b243-d80b0ba96155" width="700px"/>
</div>

### Login:
Nessa página, o usuário deve inserir seu nome de usuário e senha para poder ter acesso às funcionalidades de edição do site.

<div align="center">
    <img src="https://github.com/natalia-mvieira/SpaceGlance/assets/144560412/375836cd-3179-4abc-b004-8e9edafcddff" width="700px"/>
</div>

### Visualizar Imagem:
Ao clicar sobre uma imagem, haverá um direcionamento para outra página contendo a imagem, seu nome, legenda e, também, descrição com mais detalhes sobre a foto.

<div align="center">
    <img src="https://github.com/natalia-mvieira/SpaceGlance/assets/144560412/03269e4a-bc5a-41fc-856c-75fc470518af" width="700px"/>
</div>

Se o usuário estiver autenticado, aparecerá um menu contendo dois botões, sendo um de edição e outro para deletar a imagem.

<div align="center">
    <img src="https://github.com/natalia-mvieira/SpaceGlance/assets/144560412/da018d36-0069-4964-9104-14be57a6c5a6" width="700px"/>
</div>

### Inserir Imagem:
Quem estiver logado pode inserir novas imagens na galeria. Para isso, é utilizado um formulário com campos para o nome, legenda, categoria e descrição da imagem, além de um botão para escolha da imagem a partir do computador.

No banco de dados, além dessas informações, também ficam salvos a data da publicação e o usuário que publicou a imagem.

<div align="center">
    <img src="https://github.com/natalia-mvieira/SpaceGlance/assets/144560412/34318b3d-b591-4b5a-9f0e-2674f40c7a74" width="700px"/>
</div>

A princípio, as imagens salvas por qualquer usuário são diretamente publicadas na galeria, ficando visíveis a todos os demais usuários. Isso ocorre, pois no banco de dados há o campo booleando "publicada" que define se a imagem ficará disponível para visualização ou não, e esse campo, por padrão (*default*) é marcado. Porém, o usuário administrador (SuperUser), ao classificar uma imagem como não apropriada, pode desmarcar a opção "publicada" no banco de dados para que a imagem não mais fique disponível.

### Editar Imagem: 
Estando logado, o usuário pode clicar sobre uma imagem para realizar a sua edição, ou seja, alteração de nome, legenda, categoria, descrição ou foto. Nessa página, a edição é feita a partir do mesmo formulário que a página Inserir Imagem, mas aqui ele já é previamente preenchido com as informações atuais da foto.

<div align="center">
    <img src="https://github.com/natalia-mvieira/SpaceGlance/assets/144560412/8a18cc87-3403-4fc0-aba7-daf3fa225cef" width="700px"/>
</div>

### Buscar Imagem: 
Em todas as páginas do site é possível encontrar um campo de busca no canto superior direito. Esse campo permite a busca por imagens a partir de palavras-chave contidas no nome ou legenda da foto.

Após a pesquisa, todas as imagens existentes contendo o termo buscado serão mostradas.

<div align="center">
    <img src="https://github.com/natalia-mvieira/SpaceGlance/assets/144560412/cd1637fb-da99-4780-8996-be3ffe25a73d" width="700px"/>
</div>

## Busca por Tags:
As imagens apresentam categorias a partir do elemento principal de cada uma delas.
Há 5 categorias: Nebulosa, Galáxia, Estrela, Planeta e Lua.

Ao inserir ou editar uma imagem, a categoria deve ser escolhida.
A partir dessa divisão, é possível filtrar as imagens da galeria pelas tags que aparecem no menu superior. Ao clicar nas *tags*, similar à página de busca, apenas imagens daquela categoria específica aparecerão.

## Banco de Dados
No banco de dados do Django Admin, é possível ver as informações gerais da imagem (nome, legenda, categoria, descrição), além da data de publicação e o usuário que a publicou.

Para o visual da página, foi utilizado **CSS** e **HTML**, sendo os templates de base fornecidos pelo curso da Alura. O projeto tem foco em trabalhar com Back-End.

<ins>Observação</ins>: esse projeto foi realizado durante um curso da plataforma Alura.