# lancheria-django-xisfood
Website-app desenvolvido integralmente no framework Django com banco de dados Postgresql

# IMPORTANTE: Elaborei como um tipo de exercício para treinar recursos no framework e indicarei aqui o Passo a Passo de tudo que fiz para quem estiver iniciando no mundo python/django.

# Aplicação Django:
<br>

# PARTE 1:
<br>

## Ambiente Virtual:
<br>

#### Devemos instalar o ambiente virtual VENV no windows para não ter problemas com versões do python e do django:
<br>

#### Crie uma pasta para sua aplicação, vamos chamar essa pasta de aplicacao (mas pode escolher qualquer nome), podemos criar diretamente na unidade C para facilitar na hora de digitar o caminho.
<br>

#### dentro dessa pasta que chamamos de aplicacao com o caminho c:\aplicacao, digitaremos o comando:

```

python3 -m venv ./venv

```

#### Neste caso, estamos instalando o ambiente virtual na pasta atual '.' e colocando os arquivos da instalação na subpasta 'venv'.
<br>

#### Após este comando, digite 'code .' para abrir a pasta aplicacao no Visual Studio Code e, no terminal do Visual Studio digite 

```

venv\Scripts\activate.bat

```

#### Dessa forma aparecerá a expressão 'venv' no terminal, demonstrando estar executando o ambiente virtual escolhido.
<br>

#### No ambiente virutal, instalaremos agora o django através do comando:

```

pip install Django

```

#### Será instalado a última versão do framework no ambiente virtual que criamos, verifique a versão de todas aplicações que estão instaladas no ambiente virtual através do comando:

```

pip freeze

```

#### provavelmente aparecerá algo parecido com:

```

asgiref==3.5.2
Django==4.0.5
sqlparse==0.4.2
tzdata==2022.1

```


## Iniciando o projeto no Django
<br>

#### Antes de iniciar um projeto no Django você pode consultar uma lista de comandos e opções possíveis com o comando:

 ```

django-admin help

```

#### Aparecerá uma lista de comandos, o que precisamos para iniciar o projeto é 'startproject' e, para isso, utilizamos então o comando na nossa pasta aplicacao e denominaremos nossa aplicação como nossoprojeto, mas pode ser qualquer nome, o ponto final é importante porque define que a instalação será feita diretamente na pasta aplicacao com o nome nossoprojeto:

```

django-admin startproject nossoprojeto .

```

### settings.py
<br>

#### Neste arquivo estão localizadas as principais configurações de nossa aplicação django.
<br>

#### No arquivo settings.py que foi colocado dentro da pasta nossoprojeto(ou na pasta que você definiu), modifique a linha 106 (ou a que tiver o seguinte texto LANGUAGE_CODE = 'en-us') para 'pt-br' ao invés de en-us.
<br>

#### No mesmo arquivo você pode modificar o TIME_ZONE de 'UTC' para 'America/Sao_Paulo', atualmente essa opção está na linha 108.
<br>

### urls.py
<br>

#### Este arquivo define as rotas permitidas de nossa aplicação django.
<br>

### manage.py
<br>

#### Este arquivo que também pode ser acessado por linha de comando faz a administração das principais funções do django, por exemplo, se você, na pasta aplicacao digitar:

```

python manage.py help

```

#### verá uma série de opções disponíveis, dentre elas a opção runserver que coloca a aplicação em modo servidor. Para isso digite:

```

python manage.py runserver

```

#### E pronto, a aplicação estará rodando em modo local na porta 8000, para acessar digite localhost:8000 ou então http://127.0.0.1:8000/ como aparece no terminal. Para fechar basta digitar ctrl+c
<br>

## Iniciando APP
<br>

#### Para iniciar nosso projeto específico, isto é, nossa aplicação de fato, que chamaremos de app, digite o comando: (destaco que 'app' é o nome que escolhi, mas poderia ser qualquer um e que 'startapp' é uma opção para iniciar novo projeto dentro da aplicação principal. 

```

python manage.py startapp app

```

#### Agora, para fazer o nossoprojeto reconhecer o aplicativo que estamos criando, devemos editar o arquivo settings.py e nele colocar 'app', após a linha 33. Isso é, após a expressão 'INSTALLED_APPS = [' devemos incluir nosso aplicativo que chamamos de app, mas poderá ser o nome que você criou. Este nome precisará ser o mesmo que o presente no 'name' do arquivo 'apps.py' dentro do diretório app que acabamos de criar. Assim, nosso arquivo apps.py ficou assim:

```py

from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

```

#### Enquanto nosso arquivo settings.py, provavelmente entre as linhas 33 e 41 devem ter ficado basicamente assim:

```py

INSTALLED_APPS = [
    'app',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

```


## Criando Rotas

#### Crie um arquivo chamado urls.py na pasta 'app' para definirmos nossa primeira rota, para isso importaremos o django.urls e definiremos nossa rota index com o seguinte código:

```py

from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index')

]

```

#### Já no arquivo views.py do diretório app, você deve criar suas views. Apague o campo comentado e a partir da segunda linha digite:

```py

from django.http import HttpResponse

def index(request):
	return HttpResponse('<h1>APP</h1>')

```

#### No arquivo 'urls.py' da pasta 'nossoprojeto' você deve adicionar mais um path, ou seja, além do path admin/ que veio por padrão você deverá adicionar o caminho root através do comando:

```py

path('', include('app.urls')),

```

#### Antes disso, você também deve adicionar o include na importação do django.urls em que deverá ficar com a seguinte redação:

```py

from django.urls import path, include

```

#### Após essas modificações nosso arquivo deverá ficar com o seguinte texto:

```py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
]

```

#### Pronto, agora no localhost:8000 você já poderá visualizar o texto APP que foi inserido no arquivo 'views.py' da pasta 'app'
<br>

#### Obviamente não iremos criar/editar nosso conteúdo HTML no arquivo views.py, veremos isso a seguir.

<br><br>

# PARTE 2:
<br>

## Trabalhando com Templates, Rotas e Views
<br>

## Templates:
<br>

#### Na nossa pasta 'app' crie uma pasta chamada 'templates'
<br>

#### Nessa pasta 'templates' crie um arquivo chamado 'index.html'
<br>

#### Neste caso, editaremos a nossa página de exibição com o seguinte conteúdo:

```html

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Xis Food</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="">

    </head>
    <body>
        <h1>xis Food</h1>

        <h2>Nosso Cardápio</h2>
       
        <script src="" async defer></script>
    </body>
</html>

```

#### Mas para exibir nosso conteúdo html criado, devemos fazer alterações no arquivo 'views.py' da pasta 'app'. Deveremos informar nossa view que quando o usuário requisitar o index, que seja encaminhado para a página index.html. Sendo assim, removeremos aquela linha que tinha 'from django.http import HttpResponse' e, no return utilizaremos 'return render(request,'index.html')'. Nosso arquivo 'views.py' ficará com apenas o seguinte conteúdo:

```py

from django.shortcuts import render

def index(request):
    return render(request,'index.html')

```

#### Pronto, já temos uma página HTML sendo exibida em nosso root.

#### A partir deste momento devemos ter definido o tipo de conteúdo e o banco de dados que iremos utilizar. Optei por realizar o website de um restaurante/lancheria que denominei 'XisFood' e utilizarei, inicialmente, o banco de dados sequencial postgresql.
<br>

#### Editamos nosso 'index.html' para se adequar a escolha que fizemos de Restaurante, nosso arquivo ficou conforme arquivo (anexo 2A).

## Arquivos Estáticos

#### Trabalhando com Arquivos Estáticos
<br>

#### No arquivo 'settings.py' da pasta 'nossoprojeto', insira no início do documento o texto 'import os' e, a seguir, edite o campo 'TEMPLATES' que deve estar entre as linhas 55 e 69, onde diz:

```py

'DIRS': [],

```

#### deve dizer:

```py

'DIRS': [os.path.join(BASE_DIR, 'app/templates')],

```

#### Dessa forma estaremos indicando que a base do diretório é a pasta app/templates, assim, a medida que a página cresce já teremos o mapeamento do nosso template.
<br>


#### Mas precisamos referenciar nossos arquivos estáticos, assim, acrescentaremos próximo ao final do mesmo arquivo 'settings.py', onde já tem STATIC_URL, acrescentaremos o Static_root e o Staticfiles_dirs e ficará assim:

```py

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'nossoprojeto/static')
]

```

#### Detalhe importante é que devemos criar, dessa forma, uma subpasta na pasta 'nossoprojeto' com o nome 'static'.
<br>

#### Devemos colar nessa pasta static as pastas 'css', 'fonts', 'img', 'js', 'scss' e o arquivo 'site.css' daquele nosso 'anexo 2A'.
<br>

#### Agora, no terminal, no ambiente virtual, insira o comando que irá coletar todos arquivos estáticos da sua aplicação:

```

python manage.py collectstatic

``` 

#### Você receberá uma mensagem do tipo '169 static files copied to 'C:\aplicacao\static'.' e isso indicará que as cópias foram feitas.
<br>

#### Agora, para indicar que o site possui arquivos estáticos, você deve carregá-los nos arquivos html, abra o arquivo index.html e insira, na primeira linha do arquivo html o seguinte comando:

```

{% load static %}

```

#### Assim você irá chamar os arquivos estáticos para o site.
<br>

#### Edite os campos que possuem elementos estáticos com código python, {% static 'urldoelementoestático'%}, por exemplo, na linha 87 ficará assim:

```html

<a class="nav-brand" href="index.html"><img src="{% static 'img/core-img/logo.png' %}" alt=""></a>

```

#### Ao inserir chamar cada elemento estático o site deve ficar com uma aparência semelhante a final contida no arquivo 'aplicacao - PARTE 2.rar'.

<br><br>

# PARTE 3:

## Criando links utilizando elementos python no html
<br>

#### Devemos modificar nossos caminhos utilizando {% url, 'nomedocaminho' %}, como, por exemplo, na linha 87 do nosso arquivo index.hmtl, ficaria assim:

```html

<a class="nav-brand" href="{% url 'index' %}"><img src="{% static 'img/core-img/logo.png' %}" alt=""></a>

```

#### Adicionaremos uma rota para o link produto.html, modificando o arquivo 'urls.py' do nosso diretório 'app', deixando-o com a seguinte redação:

```py

from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('produto', views.produto, name='produto')
]

```

#### Adicionaremos a função produto ao arquivo 'views.py' do nosso diretório 'app', colocaremos da seguinte forma:

```py

def produto(request):
    return render(request,'produto.html')

```

## Repartindo para evitar repetições (extendendo arquivos html)

#### Crie um arquivo chamado base.html na pasta templates do diretório app, e nesse arquivo cole todas as linhas do arquivo index desde a linha 1 com '{% load static %}' até a linha 24 com o '<body>'. Depois disso apague esse texto do arquivo index.html.
<br>

#### Faça o mesmo com as linhas 166 em diante até o final que vai do '<!-- ##### All Javascript Files ##### -->' até o '</html>' colando em baixo do body que colou no arquivo base.html.
<br>

#### Entre esses dois trechos copiados no arquivo base.html, insira os seguintes elementos python:

```html

    {% block content %}
    {% endblock %}

```

#### Assim você estará indicando onde inicia e termina a inclusão de elementos python nessa página base.html.
<br>

#### Insira o '{% load static %}' no início do arquivo index.html porque este arquivo segue contendo arquivos estáticos e, também, o elemento '{% extends 'base.html' %}' para concluir a ligação com o arquivo 'base.html' e também o elemento '{% block content %}' para indicar a partir de onde o código que será encaminhado, assim, o início do arquivo index.html ficará:

```html

{% extends 'base.html' %}
{% load static %}
{% block content %}

    <!-- Preloader -->

```

#### Ao final, na última página html, insira o elemento '{% endblock %}' para indicar o final do nosso bloco, o fim do arquivo ficará assim:

```html

    </footer>
    <!-- ##### Footer Area Start ##### -->

{% endblock %}

```

#### Faça o mesmo com a página produto.html e indique todos elementos estáticos e urls no arquivo produto.html.
<br>

## Repartindo para evitar repetições (particionando arquivos html)
<br>

#### Crie uma pasta chamada 'partials' dentro da subpasta 'templates' da pasta 'app', isso é, app/templates/partials.
<br>

#### Nessa pasta crie dois arquivos, um chamado 'menu.hmtl' e outro chamado 'footer.html'.
<br>

#### Recorte o Header do arquivo 'index.html', isso é, desde o trecho comentado <!-- ##### Header Area Start ##### --> até o trecho comentado <!-- ##### Header Area End ##### --> e cole no arquivo 'menu.html'
<br>

#### Faça o mesmo com o footer.hmtl, removendo os códigos referentes ao footer do index.html e do produto.html e colocando-os no arquivo footer.html.
<br>

#### No lugar onde ficava estes trechos, tanto no arquivo index.html quanto no arquivo produto.html, insira, respectivamente, os seguintes elementos:

```html

{% include 'partials/menu.html' %}

```

#### e
<br>

```html

{% include 'partials/footer.html' %}

```
#### A seguir insira '{% load static %}' no início dos arquivos footer.html e menu.html para carregar os arquivos estáticos que ficaram no menu e no footer e, pronto, está finalizada a partição dos arquivos para compartilhamento entre várias páginas. A finalidade do 'partials' é compartilhar código para facilitar a manutenção do website.
<br>

#### O documento 'aplicacao - PARTE 3.rar' contem estes arquivos da forma que eu modifiquei e indiquei neste manual.

<br><br>

# PARTE 4:
<br>

## Nomes de Produtos Dinâmicos
<br>

#### Abra o arquivo 'views.py' do diretório 'app' e edite o 'def index' para ficar assim:

```py

def index(request):
    return render(request,'index.html',{'nome_do_produto':'Xis Salada'})

```

#### Dessa forma estamos passando um dicionário como parâmetro, contendo a chave 'nome_do_produto' com o valor 'Xis Salada'.
<br>

#### Abra o arquivo 'index.html' da pasta 'templates' do diretório 'app' e, dentro da tag <h5> onde diz Nome do Produto, você deve colocar:

```html

{{nome_do_produto}}

```

#### Essas chaves duplas ao invés da chaves e porcentagem serve para indicar que esse código deve exibir algo na página html, neste caso indicamos para exibir o valor de uma chave.
<br>

#### Agora, ao invés de criarmos um dicionário para exibir, criaremos uma lista para iteração e inserir elementos novos na tela inicial. Modificaremos novamente nosso arquivo 'views.py' na função index e deixaremos o mesmo assim:

```py

produtos = {
	1:'Xis Salada',
	2:'SmashBurger',
	3:'Xis Frango'
    }

    dados = {
	'nome_dos_produtos': produtos
    }

    return render(request, 'index.html', dados)

```

#### E na nossa index.html, abaixo da div class="row" e antes do trecho comentado <!-- Single Best Product Area -->, insira o seguinte código:

```html

{% for chave, nome_do_produto in nome_dos_produtos.items %}

```

#### Ao final do fechamento da div class col-12 col-sm-6 col-lg-4, para dizer onde o for é encerrado, digite:

```html

{% endfor %}

```

## Banco de Dados

#### Optei pelo banco de dados PostgreSQL e a instalação do mesmo pode ser feita através do link:
<br>

[PostgreeSQL Download](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

#### Durante a instalação deve ser definido uma senha, o diretório de instalação, a porta que estará disponível para o banco de dados e após instalado, você deve executar o arquivo pgAdmin.
<br>

#### Insira a senha salva anteriormante e, em seguida, clique com o botão da direita em 'Servers', depois selecione 'Register' e, em seguida escolha a opção 'Server'.
<br>

#### Defina o 'name' do banco de dados, neste caso utilizaremos o nome 'dbserver', e na opção Connection defina o Host da aplicação, como estamos fazendo uma instalação local, definiremos o nome como 'localhost' e a senha que definimos, neste caso defini a senha '123456'. Repare que a porta da nossa aplicação será a 5432.
<br>

#### Para nossa aplicação Django 'converse' com nosso PostgreSQL devemos instalar um módulo chamado psycopg2, faremos em linha de comando com o seguinte código:

```

pip install psycopg2

```

#### Depois de instalado o módulo psycopg2, precisamos instalar os arquivos binários deste módulo e também faremos via linha de comando no venv com o seguinte código:

```

pip install psycopg2-binary

```

#### No banco de dados 'dbserver', clique com o botão da direita, escolha a opção 'Create' e, em seguida a opção 'Database' e vamos chamar este Database de xis_food, clicamos em salvar e já temos nosso xis_food em nosso banco de dados.
<br>

#### Agora, no arquivo 'settings.py' do diretório 'nossoprojeto', na variável DATABASES devemos alterar a estrutura e deixá-lo com a seguinte configuração:

```py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'xis_food',
        'USER': 'postgres',
        'PASSWORD':'123456',
        'HOST':'localhost'
    }
}

```

#### Destaco que essas informações estão contidas nas propriedades do nosso banco de dados lá no postgre.
<br>

### Criando o modelo de produtos para nosso banco de dados
<br>

#### Abra o arquivo models.py contido em nosso diretório 'app' e edite-o deixando da seguinte forma:

```py

from django.db import models
from datetime import datetime

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    ingredientes = models.TextField()
    valor = models.CharField(max_length=10)
    imagem = models.ImageField()
    categoria = models.CharField(max_length=100)
    data_produto = models.DateTimeField(default=datetime.now, blank=True)

```

#### Assim importamos também o datetime e criamos a estrutura de nosso banco de dados da classe Produto. Definimos que terá os seguintes campos: nome_produto, ingrendientes, valor, imagem, categoria e data_produto e também definimos algumas de suas propriedades indicando, por exemplo, o tamanho máximo de determinado campo e o tipo de dado que ele conterá.
<br>

#### Como utilizaremos um campo de Imagens, você deve instalar, via terminal, um módulo chamado Pillow que pode ser feito da seguinte forma:

```

python -m pip install Pillow

```

#### Agora devemos indicar como visualizar esse nosso modelo criado em nosso banco de dados, o Django realiza isso através de migrações. Devemos utilizar, para isso, no terminal, os comandos:

```

python manage.py makemigrations

```

#### Este comando criou a lista para a migração e, em seguida:

```

python manage.py migrate

```

#### Neste momento estaremos finalizando as migrações tanto do próprio Django (relacionadas a função Admin) que já haviam sido criadas lá no início da aplicação, quanto deste nosso modelo criado agora.
<br>

#### Para visualizar como nossos arquivos estão, após essa migração, acesse o arquivo 'aplicacao - PARTE 4.rar'

# PARTE 5:
<br>

## Usuário Admin
<br>

#### Em nosso arquivo chamado 'admin.py' do nosso diretório 'APP'

```PY

from .models import Produto

```

#### Mas isso por si só não é suficiente, precisamos adicionar o modelo que desejamos adicionar ao usuário Admin, por esse motivo também precisamos acrescentar:

```py

admin.site.register(Produto)

```

#### Definiremos então um nome de usuário administrador e a respectiva senha através do comando:

```

python manage.py createsuperuser

```

#### Definimos nosso usuário administrador como 'anderson', email: 'andersondeaguiardeoliveira@gmail.com' e senha '123456'. O Django informou que a senha é insegura e pediu confirmação, digitamos Y e pronto, a conta de administrador foi criada e ela pode ser acessada através do link:
<br>

[Link de Administrador](localhost:8000/admin)
<br>

#### No endereço mencionado acima, podemos realizar login de usuário administradora través do nome e senha definidos acima e realizar o cadastro de nossos produtos, clieque em '+ Adicionar' no campo Produtos, insira o nome 'Xis Salada', os ingredientes 'Pão grande, Hamburguer, Queijo Mussarela, Ovo, Alface, Tomate, Cebola, Maionese e Condimentos.', o preço '14.00', a imagem 'xissalada.jpg' que está presente no arquivo 'anexo 5A.rar', digite a categoria Lanches Salgados e clieque em 'Salvar'. Pronto, temos então nosso primeiro produto cadastrado no banco de dados através da aplicação Django.
<br>

#### Agora que temos nosso banco de dados, não faz sentido enviar um 'dicionário' python para o index.html. Por este motivo, vamos editar nossa função index no arquivo 'views.py' do diretório 'app'. Que passará a contar com a seguinte redação:

```py

from django.shortcuts import render
from .models import Produto

def index(request):    
    produtos = Produto.objects.all()
    dados = {
        'produtos': produtos
    }
    return render(request, 'index.html', dados)

def produto(request):
    return render(request,'produto.html')

```

#### Percebe-se que inserimos o model Produto via import e, também adicionamos todos elementos do objeto Produto através da função objects.all().
<br>

#### Em nosso arquivo 'index.html', onde fizemos aquele for para iterar cada produto, agora devemos utilizar a seguinte redação:

```html

<div class="row">
    {% if produtos %}
    {% for produto in produtos %}
    <div class="col-12 col-sm-6 col-lg-4">
        <div class="single-best-produto-area mb-30">
            <img src="{% static produto.imagem.url %}" alt="">
            <div class="produto-content">
                <a href="{% url 'produto' %}">
                    <h5>{{produto.nome_produto}}</h5>
                </a>
            </div>
        </div>
    </div>
    {% endfor %}
    {% else %}
    {% endif %}
</div>

```

#### Crie uma pasta chamada 'produtos' no diretório 'app', essa pasta será responsável por armazenar suas imagens cujo link aparecerá no banco de dados.
<br>

#### Modifique seu arquivo models.py acrescentando, para fazer o upload à pasta raiz, a referência:

```py

upload_to='./'

```

#### Modifique o arquivo settings.py do diretório 'nossoprojeto' para pesquisar na raiz por arquivos estáticos, da seguinte forma:

```py

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'nossoprojeto/static'), './'
]

```

### Parâmetros no URL
<br>

#### No arquivo index.html precisamos alterar o link enviando o parâmetro ID de cada produto, para isso fazemos da seguinte forma:

```html

<a href="{% url 'produto' produto.id %}">

```

#### No arquivo 'urls.py' do diretório 'app' devemos alterar o url da views.produto, ficará assim:

```py

path('<int:produto_id>' , views.produto, name='produto')

```

#### Adicionaremos, em seguida, o parâmetro 'produto_id' em nossa função 'def produto' no arquivo 'views.py' do diretório 'app':

```py

def produto(request, produto_id):
    return render(request,'produto.html')

```

#### Adicionarei a função cardápio no arquivo views.py com o seguinte conteúdo:

```py

def cardapio(request):
    return render(request, 'cardapio.html')

```

#### Incluirei o caminho Cardapio na lista de urls do 'app', no arquivo urls.py:

```py

path('cardapio' , views.cardapio, name='cardapio'),

```

#### No menu.html irei alterar o link do navbar que enviava para produto e colocarei o caminho para cardapio, ficará com o seguinte texto:

```html

<li><a href="{% url 'cardapio' %}">Cardapio</a></li>

```

#### O arquivo cardapio.html será colocado na pasta 'templates' que está dentro do diretório 'app' e o seu conteúdo será, inicialmente, idêntico àquele que está no arquivo produto.html.
<br>

#### Para incluir na página produto.html os dados de cada produto, devemos modificar a função 'def produto' na 'views.py' para pegar o parâmetro indicado no próprio link que foi especificado, neste caso a função ficará assim:

```py

def produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    
    produto_a_exibir = {
	    'produto' : produto
    }
    
    return render(request,'produto.html', produto_a_exibir)

```

#### Em sequência podemos alterar no arquivo produto.html para incluir os dados do objeto que foi selecionado e cujo id consta no url.
<br>

#### Ao final dessas alterações teremos arquivos semelhantes a este 'aplicacao - PARTE 5.rar'.
<br>

# PARTE 6:
<br>

## Cardapio

#### Inicialmente, vamos fazer uma pequena modificação em nosso banco de dados, acrescentando um ítem booleano que vamos denominar "visivel", dessa forma, nosso arquivo 'models.py' do diretório app ficará com o seguinte elemento:

```py

visivel = models.BooleanField(default=True)

```

#### Agora, no campo Admin vamos adicionar alguns como True e outros como false, neste caso colocarei o Xis Salada como False e os demais como True.
<br>

#### Feito isso, modificaremos então nossa página 'index.html' do diretório 'app' para mostrar de forma distinta aqueles disponíveis e aqueles indisponíveis, após mais um if nosso trecho do código modificado ficará assim (linhas 29 a 58):

```html

<div class="row">
    {% if produtos %}
    {% for produto in produtos %}
    {% if produto.visivel == True %}
    <div class="col-12 col-sm-6 col-lg-4">
        <div class="single-best-produto-area mb-30">
            <img src="{% static produto.imagem.url %}" alt="">
            <div class="produto-content">
                <a href="{% url 'produto' produto.id %}">
                    <h5>{{produto.nome_produto}}</h5>
                </a>
            </div>
        </div>
    </div>
    {% else%}
    <div class="col-12 col-sm-6 col-lg-4">
        <div class="single-best-produto-area mb-30">
            <img src="{% static produto.imagem.url %}" alt="">
            <div class="produto-content">
                <a href="{% url 'produto' produto.id %}">
                    <h5>{{produto.nome_produto}} (INDISPONÍVEL) </h5>
                </a>
            </div>
        </div>
    </div>
    {% endif%}
    {% endfor %}
    {% else %}
    {% endif %}
</div>

```

#### Enquanto isso, alteramos nosso 'models.py' para, no campo 'categoria', comportar apenas as categorias pré-definidas, acrescentamos uma tupla denominada ESCOLHAS:

```PY

ESCOLHAS = (
    ('1', 'Lanches Salgados'),
    ('2', 'Pizzas'),
    ('3', 'Bebidas'),
    ('4', 'Sobremesas'),
)

```

#### E nosso campo 'categoria' ficou assim:

```py

categoria = models.CharField(max_length=1, choices=ESCOLHAS)

```

#### Após essa alteração, adotei método partials criando arquivos bebidas.html, lanches_salgados.html, pizzas.html e sobremesas.html na pasta partials, com redação semelhante:

```html

{% load static %}
{% if produtos %}
{% for produto in produtos %}
{% if produto.visivel == True %}
{% if produto.categoria == '1'%}
<div class="container">
    <div class="row">                    
        <div class="col-10 col-md-10">
            <div class="produto-headline my-5">
                <div class="produto-duration">
                    <h6>{{produto.nome_produto}}</h6>
                    <h6>RS {{produto.valor}}</h6>
                    <p>{{produto.ingredientes}}</p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endif %}
{% endif %}
{% endfor %}
{% else %}
{% endif %}

```

#### E chamei estes arquivos no arquivo 'cardapio.html', por exemplo, através do elemento:

```html

{% include 'partials/lanches_salgados.html' %}

```

#### Essas modificações tornaram meu código mais inteligível e, também, ficou mais fácil dar manutenção à ele.
<br>

#### Adicionei a função request.get_full_path em meu arquivo cardapio.html para buscar o url com os parâmetros enviados pelo formulário, dessa forma pude fazer a restrição de exibição conforme selecionado em elemento html denominado 'option'.
<br>

#### Ao final dessas alterações teremos arquivos semelhantes a este 'aplicacao - PARTE 6.rar'.
<br>

# PARTE 7:
<br>

## Os próximos passos serão a criação de Sistema de Loja Online com carrinho de compras e sistema de pagamento implementado no código. 
