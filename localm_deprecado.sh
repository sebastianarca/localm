#!/bin/bash
# Este archivo como link simbolico en: /usr/local/bin/localm
# /usr/local/bin/localm -> /home/www/localhost/localm.sh*

#sudo mkdir /sys/fs/cgroup/systemd
#sudo mount -t cgroup -o none,name=systemd cgroup /sys/fs/cgroup/systemd/

# _now=$(date +"%Y%m%d")
# _mysqlContainer='mysql_prod'
# _mysqlUser='wp_mysql_user'
# _mysqlPass='wp_mysql_pass_1234'
# _mysqlDBName='custom'
# _directorioBackup='./sql_backup'

# docker exec -ti ${_mysqlContainer} mysqldump --routines --triggers --single-transaction -KBe -u ${_mysqlUser} -p${_mysqlPass} ${_mysqlDBName} > ${_directorioBackup}/Dump-${_mysqlContainer}-${_mysqlDBName}-${_now}.sql
# ####
# ## Restaurar base de datos
# ####
# # docker exec -ti ${_mysqlContainer} mysql -u ${_mysqlUser} -p${_mysqlPass} < file.sql


####
# docker run -ti symfony_init symfony check:requirements
####

ROOT_PATH='/home/otharwa/www/localhost'

dockerStart=''
dockerStop=''
dockerLogs=''
dockerBuild=''
while test $# -gt 0; do
  has_docker_options=true
  case "$1" in
    -h|--help)
      echo "localm, es un gestor de proyectos para localhost. (Localhost Manager)"
      echo " "
      echo "localm [opciones docker] proyecto1 proyecto2 (en orden de ejecucion)"
      echo " "
      echo "opciones docker:"
      echo "--help      Muestra esta ayuda"
      echo "--start     aplica el comando de docker-compose 'up -d'"
      echo "--stop      aplica el comando de docker-compose 'down --remove-orphans'"
      echo "--logs      aplica el comando de docker-compose 'logs -f'"
      echo "--build     aplica el comando de docker-compose 'build --force-rm'"
      echo "--monit     aplica el comando 'docker stats'"
      echo "--dir       ir al directorio de la aplicacion."
      echo " "
      printf "Proyectos disponibles: \n \
    base:                       Proyecto base, incluye MariaDB,Nginx Proxy \n \
    symfonyinit:                Ejemplo de Symfony \n \
    ecommerce:                  Ejemplo de Ecommerce con Wordpress \n \
    wordpresstest:              Instalacion basica de Wordpress \n \
    html_only:                  Ejemplo de HTML Unico \n \
"
      exit 0
      ;;
    --start)
      dockerStart='up -d'
      break
      ;;
    --stop)
      dockerStop='down --remove-orphans'
      break
      ;;
    --logs)
      dockerLogs='logs -f'
      break
      ;;
    --build)
      dockerBuild='build --force-rm'
      break
      ;;
    --monit)
      docker stats; exit 1;
      break
      ;;
    --dir)
      dockerDir=true
      break
      ;;
    *)
      echo 'tu vieja exit'; exit 1;
      break
      ;;
  esac
done

if [ -z "$has_docker_options" ]
then
    echo 'Use el argumento -h o --help para ver la ayuda.'; exit 1;
fi


pushd $ROOT_PATH
for proyect in "$@" 
do
    has_options=true
    case $proyect in
    base)
        if [[ ! -z ${dockerDir} ]]
        then
            echo "$ROOT_PATH" && exit 1;
        fi
        docker-compose -f ./docker-compose.yml -p vps $dockerStart $dockerStop $dockerLogs $dockerBuild;
        break
        ;;
    ecommerce)
        docker-compose -f ecommerce.test/docker/docker-compose.yml $dockerStart $dockerStop $dockerLogs $dockerBuild;
        break
        ;;
    symfonyinit)
        if [[ ! -z ${dockerDir} ]]
        then
            echo "$ROOT_PATH/symfony-init.test/" && exit 1;
        fi
        docker-compose -f symfony-init.test/docker/docker-compose.yml $dockerStart $dockerStop $dockerLogs $dockerBuild;
        break
        ;;
    wordpresstest)
        docker-compose -f wordpresstest.com/docker/docker-compose.yml $dockerStart $dockerStop $dockerLogs $dockerBuild;
        break
        ;;
    prestashop)
        docker-compose -f prestashop.test/docker/docker-compose.yml $dockerStart $dockerStop $dockerLogs $dockerBuild;
        break
        ;;
    html_only)
        docker-compose -f html_only.com/docker/docker-compose.yml $dockerStart $dockerStop $dockerLogs $dockerBuild;
        break
        ;;
    esac
done
popd