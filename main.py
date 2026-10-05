import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega a senha com segurança
senha = os.getenv("SENHA_BANCO")
print("Senha carregada com sucesso!")


print("Eu sou Vanessa")
print("Hello World")
print("Essa alteração será corrigida com o revert")

print("Fazer teste")
print("Essa alteração será corrigida com o resert")
print("Teste inicial Amend")
print("Senha enviada")

Ammend
reset
revert

# O que fazer caso você envie uma senha por engano para o Git:

# 1. Troque a senha imediatamente: Vá até o serviço onde a senha dava acesso (API, banco de dados, etc.) 
# e revogue ou altere a credencial, pois o histórico antigo pode ter sido visto.

# 2. Se ainda NÃO deu git push: Desfaça o commit mantendo o arquivo local com git reset --soft HEAD~1, 
# remova a senha do código, coloque-a no arquivo .env (protegido pelo .gitignore) e faça um novo commit limpo.

# 3. Se JÁ deu git push: O .gitignore sozinho não remove o que já foi enviado. 
# Ferramentas de limpeza de histórico são necessárias, mas, para repositórios pessoais ou de estudo, 
# a opção mais rápida e segura é excluir o repositório no GitHub, criar um novo limpo e reenviar o código.
