# Arhitectura sistemelor de calcul - Tema 1
# Multi Producer - Multi Consumer Marketplace
Brabete Adrian
334CC

***Organizare***

  Marketplace ul este realizat sa lucreze cu mai multi producatori si mai multi
consumatori. Producatori publica 2 tipuri de produse si acestea pot fi achizionate
atunci cand e disponibila implinirea unei comenzi in intregime.

Sincronizare:
  Pentru functionarea corecta a marketplace-ului pe mai multe thread-uri este nevoie
  de 2 elemente de sincronizare, 2 lock-uri.
  
  Primul lock are rolul de a sincroniza atribuirea de id uri pentru produceri:
  ```python
        self.lockPool[0].acquire()
        prod_id = len(self.qSize)
        self.qSize.append(0)
        self.lockPool[1].release()
  ```
  
  Iar al doilea este folosit in scop asemanator pentru atribuirea de id pentru cosul de cumparaturi.
  
  Structurile de date folosite:
  * Liste:
    * qSize: retine numarul de produse publicate de fiecare producator pentru a limita stock-ul la o 
             valoare setat in constructorul clasei marketplace
    * productPool: reprezinta totalitatea produselor disponibile
  * Dictionary:
    * cartDic: atribuie fiecarui cos produsele pe care le contine
    * producerDic: face legatura intre produs si producatorul care la publicat

  Consider ca performanta implementarii este decenta, destul de rapida pentru a trece testele :)
  Cred ca se poate optimiza in special pe numere mari reducand numarul de lock uri si folosind 
  2 cozi deoarece structurile de python sunt thread-safe.
 
***Implementare***
  Implemenarea este completa conform cerintei.
  Avand in vedere ca in acelasi timp am lucrat si la tema la SO in C, python a fost foarte intelegator.


***Git***
Repo-ul va fi privat pana la terminarea deadline-ului
link: https://github.com/SexySparrow/asc_tema1
