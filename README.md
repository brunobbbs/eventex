Eventex
=======

Repositório de estudo do projeto realizado no curso [**Welcome to the Django**](http://welcometothedjango.com.br/)


## Como instalar?

1. Faça o clone do repositório;
```console
git clone git@github.com:brunobbbs/eventex.git wttd
cd wttd/
```
2. Crie um virtualenv com Python 3.5
```console
python -m venv .wttd
```
3. Ative o virtualenv
```console
source .wttd/bin/activate
```
4. Instale as dependências do projeto;
```console
pip install -r requirements.txt
```
5. Configure a instância com .env
```console
cp contrib/env-sample .env
```
6. Execute os testes
```console
python manage.py test
```