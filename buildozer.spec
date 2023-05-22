[app]
# Nome do seu aplicativo (sem espaços)
title = t engine

# Pacote do aplicativo (usado como nome do pacote Android)
package.name = com.t.engine
package.domain = com.t

# Versão do seu aplicativo
version = 1.0

# Versão mínima do SDK Android suportada pelo seu aplicativo
android.minapi = 21

# Versão máxima do SDK Android suportada pelo seu aplicativo
android.maxapi = 30

# Permissões necessárias para o seu aplicativo
android.permissions = INTERNET, ACCESS_NETWORK_STATE, ACESS_EXTERNAL_STORAGE

# Dependências do seu aplicativo (se houver)
requirements = pygame, numpy

# Nome do arquivo principal do seu aplicativo
source.filename = source/main.py

# Ícone do aplicativo (coloque o arquivo .png na pasta do projeto)
source.icon = icon.png

# Incluir arquivos adicionais necessários para o seu aplicativo (se houver)
source.include_exts = py,png,json

# Diretórios a serem excluídos da construção
source.exclude_patterns = __pycache__/*, .git/*

# Opções de compilação personalizadas (se necessário)
android.custom_gradle = False
