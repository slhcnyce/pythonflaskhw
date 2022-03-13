## BestCloudForMe Academy Python Boto3 HomeWork

# Nasıl Kullanılır
Aws hesabınızdan almış olduğunuz;

-Access Key Id
-Secret Access Key
-Region
-Instance Id

değerlerini ilgili metodlarla birlikte aşağıda anlatılan şekilde kullanabilirsiniz.

## Aws Hesabınızda Seçilen Regionda Mevcut Instance'leri Listelemek İçin

##### http://<api_host>:<api_port>/ec2/list

İlgili endpointe **GET** metodu ile accessid,accesskey ve region parametreleriyle istek atınız.

Örn: http://0.0.0.0:8080/ec2/list?accessid=YOURACCESSID&accesskey=YOURSCRETACCESSKEY&region=YOURREGION

## Aws Hesabınızda Seçilen Regionda Seçilen Instance'i Başlatmak İçin

##### http://<api_host>:<api_port>/ec2/start

İlgili endpointe **POST** metodu ile accessid,accesskey,region ve instid parametrelerini JSON body olarak istek atınız.

<p>
{<br>
    "accessid":"YOURACCESSID",<br>
    "accesskey":"YOURSECRETACCESSKEY",<br>
    "region":"YOURREGION",<br>
    "instid":"YOURINSTANCEID"<br>
}<br>
</p>

## Aws Hesabınızda Seçilen Regionda Seçilen Instance'i Durdurmak İçin

##### http://<api_host>:<api_port>/ec2/stop

İlgili endpointe **GET** metodu ile accessid,accesskey,region ve instid parametreleriyle istek atınız.

Örn: http://0.0.0.0:8080/ec2/stop?accessid=YOURACCESSID&accesskey=YOURSCRETACCESSKEY&region=YOURREGION&instid=YOURINSTANCEID

