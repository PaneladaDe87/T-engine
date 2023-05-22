[app]

# (str) Nome do aplicativo

title = t engine

# (str) Nome do pacote

package.name = com.example.t.engine

# (str) Versão do aplicativo

version = 1.0.0

# (str) Código da versão do aplicativo (incrementar para cada versão)

version.code = 1

# (str) Descrição curta (exibida sob o ícone do aplicativo no Android)

description = lol

# (list) Dependências do aplicativo

requirements = pygame, numpy

# (str) Arquivo principal do aplicativo

source.dir = ./source

# (list) Arquivos ou diretórios adicionais a serem incluídos no pacote

source.include_exts = py,png,jpg

source.include_patterns = assets/*,images/*.png

# (list) Arquivos ou diretórios a serem excluídos do pacote

source.exclude_exts = spec,txt,md

source.exclude_patterns = tests/*,bin/*

# (list) Permissões do aplicativo

android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (list) Serviços específicos do Android

android.services = vibration

# (int) SDK mínimo necessário

android.minapi = 21

# (int) SDK de destino

android.sdk = 28

# (int) Nível de API mínimo necessário

android.ndk = 21

# (bool) Ativar ou desativar o console do Pygame (para depuração)

android.console = True

# (list) Argumentos adicionais a serem passados para o comando "adb"

android.adb_args = -d

p4a.architectures = armeabi-v7a, arm64-v8a

# (list) Bibliotecas compartilhadas do Android a serem incluídas

android.gradle_dependencies = com.android.support:support-v4:27.1.0

# (list) O que adicionar para a pasta privada do aplicativo

android.private_storage = True

# (list) O que adicionar para a pasta externa do aplicativo

android.external_storage = False

# (list) O que adicionar para a pasta de cache do aplicativo

android.arch = armeabi-v7a

# (list) Permissões do Android para APK

# (list) Pacotes Python adicionais a serem incluídos no pacote

p4a.architectures = armeabi-v7a, arm64-v8a

# (list) Bibliotecas compartilhadas do Android a serem incluídas

android.gradle_dependencies = com.android.support:support-v4:27.1.0

# (list) O que adicionar para a pasta privada do aplicativo

android.private_storage = True

# (list) O que adicionar para a pasta externa do aplicativo

android.external_storage = False

# (list) O que adicionar para a pasta de cache do aplicativo

android.arch = armeabi-v7a

# (list) Python-for-Android extras

p4a.local_recipes = custom_recipes/

# (list) Python-for-Android distribuições personalizadas a serem incluídas

p4a.dist_name = meu_aplicativo

# (list) Opções adicionais a serem passadas para o Gradle

android.gradle_build_flags = 

# (list) Opções adicionais a serem passadas para o build.py

android.build_args = -v

# (list) Opções adicionais a serem passadas para o Android Gradle Plugin

android.gradle_dependencies = 'com.google.firebase:firebase-core:16.0.8', 'com.google.firebase:firebase-ads:17.2.1'

# (list) Opções adicionais a serem passadas para o Android Gradle Plugin

android.add_src = 

# (list) Opções adicionais a serem passadas para o build.gradle

android.add_dependency = com.google.firebase:firebase-core:16.0.8, com.google.firebase:firebase-ads:17.2.1

# (list) O que adicionar para a pasta privada do aplicativo

android.private_storage = True

# (list) O que adicionar para a pasta externa do aplicativo

android.external_storage = False

# (list) O que adicionar para a pasta de cache do aplicativo

android.arch = armeabi-v7a

# (list) Python-for-Android extras

p4a.local_recipes = custom_recipes/

# (list) Python-for-Android distribuições personalizadas a serem incluídas

p4a.dist_name = meu_aplicativo

# (list) Opções adicionais a serem passadas para o Gradle

android.gradle_build_flags = 

# (list) Opções adicionais a serem passadas para o build.py

android.build_args = -v

# (list) Opções adicionais a serem passadas para o Android Gradle Plugin

android.gradle_dependencies = 'com.google.firebase:firebase-core:16.0.8', 'com.google.firebase:firebase-ads:17.2.1'

# (list) Opções adicionais a serem passadas para o Android Gradle Plugin

android.add_src = 

# (list) Opções adicionais a serem passadas para o build.gradle

android.add_dependency = com.google.firebase:firebase-core:16.0.8, com.google.firebase:firebase-ads:17.2.1

# (str) Configurações adicionais do Android Gradle Plugin

android.gradle_manifest = 

# (str) Configurações adicionais do build.gradle

android.gradle_dependencies = 

# (str) Configurações adicionais do build.gradle

android.gradle_build_ext = 

# (list) Opções de build do Android, se separadas por semicolons, são passadas para o Gradle

# para fins de análise. O build.gradle deve usar uma sintaxe compatível para processar essas opções.

android.gradle_build_profile = 

# (list) Opções de build do Android, se separadas por semicolons, são passadas para o Gradle

# para fins de análise. O build.gradle deve usar uma sintaxe compatível para processar essas opções.

android.gradle_defines = 

# (list) Opções de build do Android, se separadas por semicolons, são passadas para o Gradle

# para fins de análise. O build.gradle deve usar uma sintaxe compatível para processar essas opções.

android.gradle_plugins = 

# (str) Configurações adicionais do Android Gradle Plugin

android.gradle_manifest = 

# (str) Configurações adicionais do build.gradle

android.gradle_dependencies = 

# (str) Configurações adicionais do build.gradle

android.gradle_build_ext = 

# (list) Opções de build do Android, se separadas por semicolons, são passadas para o Gradle

# para fins de análise. O build.gradle deve usar uma sintaxe compatível para processar essas opções.

android.gradle_build_profile = 

# (list) Opções de build do Android, se separadas por semicolons, são passadas para o Gradle

# para fins de análise. O build.gradle deve usar uma sintaxe compatível para processar essas opções.

android.gradle_defines = 

# (list) Opções de build do Android, se separadas por semicolons, são passadas para o Gradle

# para fins de análise. O build.gradle deve usar uma sintaxe compatível para processar essas opções.

android.gradle_plugins = 

# (str) Arquivo a ser executado quando o aplicativo é iniciado (usado apenas para o Android/SDL2)

android.entrypoint = org.kivy.android.PythonSDL2Activity

# (list) Permissões personalizadas adicionais a serem concedidas ao aplicativo

android.permissions = CAMERA, ACCESS_FINE_LOCATION

# (list) Permissões personalizadas adicionais a serem concedidas ao aplicativo

android.permissions = CAMERA, ACCESS_FINE_LOCATION

# (list) Opções de build específicas para a plataforma iOS

ios.buildozer_ios_appid = com.example.seuaplicativo

# (list) Opções de build específicas para a plataforma iOS

ios.buildozer_ios_appid = com.example.seuaplicativo

# (list) Permissões personalizadas adicionais a serem concedidas ao aplicativo

android.permissions = CAMERA, ACCESS_FINE_LOCATION

# (list) Opções de build específicas para a plataforma iOS

ios.buildozer_ios_appid = com.example.seuaplicativo

