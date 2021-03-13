import requests
import os



HabboID = input("Escribe el nombre del keko: ") 

os.system("cls")
print("Elige el hotel: es/com/fi/com.br/fr/nl/de/it/com.tr")
Hotel = input("hotel: ")
response = requests.get(f'https://www.habbo.{Hotel}/api/public/users?name={HabboID}')








HabboID = response.json()['uniqueId']



print(HabboID)
os.system("cls")
    
url= f'https://www.habbo.{Hotel}/api/public/users/{HabboID}/badges'



print("Scaneando placas...Espera un momento")

print("Fichero creado: " + HabboID +".html") 

r= requests.get(url)
habbo = r.text

habbo = r.json()


archivo = open(HabboID + ".html", "a")


archivo.write("<link href='css/buscador.css' rel='stylesheet'>")


archivo.write("<link href='css/fuentes.css' rel='stylesheet'>")


archivo.write("<script src='js/stopExecutionOnTimeout-157cd5b220a5c80d4ff8e0e70ac069bffd87a61252088146915e8726e5d9f147.js'></script>")

archivo.write("<script src='js/jquery.min.js'></script>")

archivo.write("<script src='js/buscador.js'></script>")





 

archivo.write("<p class='buscador'>")
archivo.write("<label>Buscar:</label>")

archivo.write("<input id='buscador' type='input' value=''>")

archivo.write("<br />")
archivo.write("<br />")





archivo.write("</p>")

archivo.close()
   

archivo = open(HabboID + ".html" , "a")



archivo.close()
 
for Habboinfo in habbo:
 
 archivo = open(HabboID + ".html", "a", encoding="utf-8")
 
 
    
 

 

 archivo.write("<div class='item'>")
 archivo.write("<div class='texto'>") 
 archivo.write("<label class='buscarHabbo'>")
 archivo.write("<br />")
 archivo.write("<p>Nombre:"  + Habboinfo["name"]  +"</p>")
 archivo.write("<p>Descripción:"  + Habboinfo["description"]  +"</p>")
 archivo.write("<p>Código: " "<b>" + Habboinfo["code"]  +"</b>"+"</p>")
 archivo.write("<br />")
 archivo.write("</div>")
 archivo.write("<div class='botones'>")
 archivo.write("<span class='imagenPlaca'><img     src=https://images.habbo.com/c_images/album1584/"  + Habboinfo["code"]  +".gif" +"></span>")
 archivo.write("<span class='codigoPlaca'>"  + Habboinfo["code"]  +"</span>")
 archivo.write("</label>")
 

  
 archivo.close()



 archivo = open(HabboID + ".html", "a")

 archivo.write("</div>")
 archivo.write("</div>")
   
 archivo.close()
















 archivo = open (HabboID +  ".html" , "a")

 
 
archivo.write("<SPAN style='position: absolute; top: 105px; left: 810px;'>" "<b>"+ response.json()['name']+"</b>"" <script type='text/javascript' src='js/placas.js'></script>")


archivo.close()