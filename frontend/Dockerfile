# Usar a imagem do Nginx para servir os arquivos estáticos
FROM nginx:alpine

# Definir o diretório de trabalho no container onde os arquivos serão copiados
WORKDIR /usr/share/nginx/html

# Copiar os arquivos do frontend (HTML, CSS, JS) para dentro do diretório de trabalho do Nginx
COPY ./frontend/ .

# Expor a porta 3000, pois queremos que o Nginx escute nessa porta
EXPOSE 3000

# Configuração do Nginx para escutar na porta 3000
CMD ["nginx", "-g", "daemon off;"]
