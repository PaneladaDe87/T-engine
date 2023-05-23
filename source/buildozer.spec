[app]

# (obrigatório) Nome do seu aplicativo

title = t engine

# (obrigatório) Pacote do aplicativo (com '.' substituindo os '-')

package.name = com.paneladade87.t

# (obrigatório) Versão do seu aplicativo

version = 0.1

# (obrigatório) Código de versão do Android (apenas números)

android.version_code = 1

# (obrigatório) Caminho para o arquivo principal do seu aplicativo Python

# Certifique-se de que este arquivo existe na mesma pasta que o buildozer.spec

source.dir = .

# (opcional) Lista de arquivos ou diretórios adicionais a serem incluídos no pacote

# Inclua aqui todos os arquivos e diretórios necessários para o seu aplicativo

#source.include_exts = py,png,jpg,kv,atlas

#source.include_patterns = assets/*,images/*.png

# (opcional) Lista de arquivos ou diretórios a serem excluídos do pacote

#source.exclude_exts = spec,txt,md

#source.exclude_patterns = tests/*,bin/*.png

# (opcional) Dependências do aplicativo separadas por vírgula

requirements = kivy

# (opcional) Permissões extras do Android

#android.permissions = INTERNET,ACCESS_FINE_LOCATION

# (opcional) Versão mínima do Android suportada pelo seu aplicativo

#android.minapi = 21

# (opcional) Configuração adicional para o Android

#android.gradle_dependencies = 'implementation "com.google.firebase:firebase-messaging:17.3.4"'

# (opcional) Configuração do iOS

#ios.requirements = kivy_ios

# (opcional) Configuração adicional para o iOS

#ios.plist_custom_entries = CFBundleName: My Awesome App

# (opcional) Configuração de acesso ao armazenamento externo no Android

#android.permissions = WRITE_EXTERNAL_STORAGE

# (opcional) Configuração de acesso à internet no Android

#android.permissions = INTERNET

