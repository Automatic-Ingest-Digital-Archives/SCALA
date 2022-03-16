### Cron to do the solr backup

This backup cron will run a script that will backup all collections in solr and save this backup in the **/roda/backup/index/solr** folder.

- The backup cron runs at 00:00 every day **(0 0 * * *)**.

- To change the cron expression you can access it through  **01-code/images/roda/cron.d/sorl_backup**. After that you need to build another image of roda to install the cron with the new expression.

- The backup files are saved in the folder **/roda/backup/index/solr**.

- The script is stored in **/01-code/images/roda/roda-scripts** and named **roda_solr_backup**.


To prevent the system from accumulating multiple backup files a cron was created with the name **solr_backup_delete** that has the function of deleting old backup files.

### Cron to delete older backup files

This cron checks the folder of backup files and lists them sorted by date. It saves the ten most recent ones and deletes the rest of the files.

- This cron runs at 02:00 every day **(0 2 * * *)**.

- To change the cron expression you can access it through **01-code/images/roda/cron.d/solr_backup_delete**. After that you need to build another image of roda to install the cron with the new expression.

- The script is stored in **/01-code/images/roda/roda-scripts** and named **roda_solr_backup_delete**.

- You can change the number of saved files by updating the docker-compose **(01-code/deploys/production/docker-compose.yml)** variable named **RODA_SOLR_BACKUP_INDEX**. To do the change of this value you need to restart the docker services. 
