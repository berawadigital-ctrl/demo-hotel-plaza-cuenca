# Contenido de la demo Hotel Plaza Cuenca (es/en/fr/de). Hechos de hotelplazacuenca.es leidos el 02/11/2026 (ver berawa/sources.json). Sin valoraciones ni porcentajes de opiniones; sin precios ni ofertas.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hotel real.','en':' Images are illustrations and do not show the actual hotel.','fr':' Les images sont des illustrations et ne montrent pas l’hôtel réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hotel.'}
H={'es':['Dobles, triple e individual','Habitación adaptada'],'en':['Doubles, triple and single','Accessible room'],'fr':['Doubles, triple et individuelle','Chambre adaptée'],'de':['Doppel-, Dreibett- und Einzelzimmer','Barrierefreies Zimmer']}
RD={
'es':['Doble con dos camas, doble de matrimonio, triple e individual. Cada habitación es diferente, decorada con objetos traídos de Marruecos, Mauritania o Senegal.','También hay una habitación adaptada. Todas con baño completo, wifi gratuito, aire acondicionado, calefacción y televisión.'],
'en':['Twin double, double, triple and single. Every room is different, decorated with objects brought from Morocco, Mauritania or Senegal.','There is also an accessible room. All with full bathroom, free wifi, air conditioning, heating and TV.'],
'fr':['Double à deux lits, double à grand lit, triple et individuelle. Chaque chambre est différente, décorée d’objets rapportés du Maroc, de Mauritanie ou du Sénégal.','Il y a aussi une chambre adaptée. Toutes avec salle de bain complète, wifi gratuit, climatisation, chauffage et télévision.'],
'de':['Doppelzimmer mit zwei Betten, Doppelzimmer mit Ehebett, Dreibett- und Einzelzimmer. Jedes Zimmer ist anders, eingerichtet mit Objekten aus Marokko, Mauretanien oder dem Senegal.','Außerdem gibt es ein barrierefreies Zimmer. Alle mit komplettem Bad, kostenlosem WLAN, Klimaanlage, Heizung und Fernseher.']}
ART={
'hero':('arches',1601,['#2a1a12','#c8803e','#f0c98e','#8e4f26','#6a3a1c','#3a2010']),
'intro':('columns',1602,['#f4ede3','#fbf6ee','#a0602e','#71431f','#3a2010']),
'r1':('arches',1611,['#f1e8dc','#cf8a48','#a0602e','#71431f','#3a2010']),
'r2':('hills',1612,['#efe7da','#f3dcb8','#d08f50','#a89878','#7c6e52','#544a38']),
'g1':('skyline',1621,['#2a1a12','#c8803e','#f0c98e','#8e4f26','#6a3a1c','#3a2010']),
'g2':('hills',1622,['#ece5d8','#f1dfc0','#c98a4c','#a59a78','#7a7052','#524b38']),
'g3':('columns',1623,['#f2eadf','#faf5ec','#9c5c2c','#6e421e','#3a2010']),
'g4':('arches',1624,['#2a1a12','#d18c4a','#f4d3a0','#94582c','#70401e','#3e2412'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Plaza Cuenca · Hotel con encanto en el centro de Cuenca',see_rooms='Ver las habitaciones',hero_k='Cuenca · Calle Sándalo 1',hero_t='No hay huésped igual, no encontrarás habitación igual',hero_s='Un hotel con encanto en el centro de Cuenca, decorado con objetos traídos de África.',
 intro_t='Un hotel diferente para viajeros diferentes',intro_p1='El Hotel Plaza abrió en el verano de 2013 en el centro de Cuenca, a 1,5 km del casco histórico y a pocos minutos de las estaciones de autobuses y de tren.',
 intro_p2='Lámparas y espejos marroquíes, bancos senegaleses, telas de los mercados de Dakar y lavabos de piedra de fósil: objetos que Manuel Plaza ha ido reuniendo en sus viajes.',
 stats=['Abierto en 2013','19 habitaciones','A 1,5 km del casco histórico','Espacio privado para motos'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Cálidas, acogedoras y confortables; cunas para bebés bajo petición.',
 svcs=['Wifi gratuito','Aire acondicionado y calefacción','Servicio de habitaciones','Cunas bajo petición','Aparcamiento privado para motos','Bicicletas admitidas previa solicitud'],
 around_s='Cuenca, entre las hoces del Júcar y el Huécar: casco antiguo Patrimonio de la Humanidad desde 1996, la Catedral, las Casas Colgadas y el Museo de Arte Abstracto Español.',
 loc_p='Calle Sándalo 1 · 16004 Cuenca, en el centro de la ciudad. Para el check-in, llama para confirmar tu hora de llegada.',
 chips=['¿Qué habitaciones tenéis?','¿Admitís mascotas?','¿Dónde aparco la moto?','¿Cómo reservo?']),
'en':dict(title='Hotel Plaza Cuenca · Charming hotel in central Cuenca',see_rooms='See the rooms',hero_k='Cuenca · Calle Sándalo 1',hero_t='No two guests alike, no two rooms alike',hero_s='A charming hotel in central Cuenca, decorated with objects brought from Africa.',
 intro_t='A different hotel for different travellers',intro_p1='Hotel Plaza opened in the summer of 2013 in the centre of Cuenca, 1.5 km from the old town and a few minutes from the bus and train stations.',
 intro_p2='Moroccan lamps and mirrors, Senegalese benches, fabrics from Dakar’s markets and fossil-stone washbasins: objects Manuel Plaza has gathered on his travels.',
 stats=['Open since 2013','19 rooms','1.5 km from the old town','Private space for motorbikes'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Warm, cosy and comfortable; baby cots on request.',
 svcs=['Free wifi','Air conditioning and heating','Room service','Cots on request','Private motorbike parking','Bicycles allowed on request'],
 around_s='Cuenca, between the gorges of the Júcar and Huécar: an old town on the World Heritage list since 1996, the Cathedral, the Hanging Houses and the Museum of Spanish Abstract Art.',
 loc_p='Calle Sándalo 1 · 16004 Cuenca, in the city centre. For check-in, please call to confirm your arrival time.',
 chips=['Which rooms do you have?','Do you accept pets?','Where can I park my motorbike?','How do I book?']),
'fr':dict(title='Hôtel Plaza Cuenca · Hôtel de charme au centre de Cuenca',see_rooms='Voir les chambres',hero_k='Cuenca · Calle Sándalo 1',hero_t='Aucun client pareil, aucune chambre pareille',hero_s='Un hôtel de charme au centre de Cuenca, décoré d’objets rapportés d’Afrique.',
 intro_t='Un hôtel différent pour des voyageurs différents',intro_p1='L’Hôtel Plaza a ouvert à l’été 2013 au centre de Cuenca, à 1,5 km du centre historique et à quelques minutes des gares routière et ferroviaire.',
 intro_p2='Lampes et miroirs marocains, bancs sénégalais, tissus des marchés de Dakar et lavabos en pierre fossile : des objets réunis par Manuel Plaza au fil de ses voyages.',
 stats=['Ouvert en 2013','19 chambres','À 1,5 km du centre historique','Espace privé pour motos'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Chaleureuses, accueillantes et confortables ; lits bébé sur demande.',
 svcs=['Wifi gratuit','Climatisation et chauffage','Service en chambre','Lits bébé sur demande','Stationnement privé pour motos','Vélos acceptés sur demande'],
 around_s='Cuenca, entre les gorges du Júcar et du Huécar : vieille ville inscrite au patrimoine mondial depuis 1996, la cathédrale, les Maisons suspendues et le Musée d’art abstrait espagnol.',
 loc_p='Calle Sándalo 1 · 16004 Cuenca, au centre-ville. Pour l’arrivée, appelez pour confirmer votre heure.',
 chips=['Quelles chambres avez-vous ?','Acceptez-vous les animaux ?','Où garer ma moto ?','Comment réserver ?']),
'de':dict(title='Hotel Plaza Cuenca · Charmantes Hotel im Zentrum von Cuenca',see_rooms='Zimmer ansehen',hero_k='Cuenca · Calle Sándalo 1',hero_t='Kein Gast ist wie der andere, kein Zimmer wie das andere',hero_s='Ein charmantes Hotel im Zentrum von Cuenca, eingerichtet mit Objekten aus Afrika.',
 intro_t='Ein anderes Hotel für andere Reisende',intro_p1='Das Hotel Plaza öffnete im Sommer 2013 im Zentrum von Cuenca, 1,5 km von der Altstadt und wenige Minuten von Bus- und Bahnhof entfernt.',
 intro_p2='Marokkanische Lampen und Spiegel, senegalesische Bänke, Stoffe von den Märkten Dakars und Waschbecken aus Fossilstein: Objekte, die Manuel Plaza auf seinen Reisen gesammelt hat.',
 stats=['Seit 2013','19 Zimmer','1,5 km von der Altstadt','Privater Stellplatz für Motorräder'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Warm, gemütlich und komfortabel; Babybetten auf Anfrage.',
 svcs=['Kostenloses WLAN','Klimaanlage und Heizung','Zimmerservice','Babybetten auf Anfrage','Privater Motorradstellplatz','Fahrräder nach Anfrage erlaubt'],
 around_s='Cuenca, zwischen den Schluchten von Júcar und Huécar: Altstadt seit 1996 Weltkulturerbe, die Kathedrale, die Hängenden Häuser und das Museum für spanische abstrakte Kunst.',
 loc_p='Calle Sándalo 1 · 16004 Cuenca, im Stadtzentrum. Für den Check-in rufen Sie bitte an, um Ihre Ankunftszeit zu bestätigen.',
 chips=['Welche Zimmer gibt es?','Sind Haustiere erlaubt?','Wo parke ich mein Motorrad?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://booking.avirato.com/?code=2403545&lang='
BOOK=dict(mode='engine',url=dict(es=R+'es',en=R+'en',fr=R+'fr',de=R+'de'))
D=dict(name='Hotel Plaza Cuenca',ac='#2a2320',ac2='#9c5c2c',ac2_a11y='#7a4520',book=BOOK,around=['Casas Colgadas','Catedral de Cuenca','Museo de Arte Abstracto Español'],foot=FOOT,
 address='Calle Sándalo 1 · 16004 Cuenca',phones=['+34 969 239 477','+34 683 706 153'],emails=['reservas@hotelplazacuenca.es'],maps='Hotel Plaza Cuenca, Calle Sándalo 1, 16004 Cuenca',t=T)
META=dict(repo='demo-hotel-plaza-cuenca',name='Hotel Plaza Cuenca',legal_name='Hnos. Plaza Pérez, S.A. (aviso legal de su web)',registry_ids=['A16025272'],
 url='https://hotelplazacuenca.es/',domain='hotelplazacuenca.es',municipality='Cuenca',province='Cuenca',sector='hotel con encanto en el centro de Cuenca',
 read_at='2026-11-02T06:56:00+01:00',created_at='2026-11-02T06:55:00+01:00',built_at='2026-11-02T07:10:00+01:00',audit_date='2026-11-02T06:44:00+01:00',
 rating=dict(value=4.3,coincide=['web'],date='2026-10-30',url='https://www.google.com/maps/search/Hotel+Plaza+Cuenca'),
 book=dict(mode='engine',url=R+'es',note='motor de reservas real enlazado desde su web (Avirato, code=2403545), HTTP 200 comprobado el 02/11/2026 con lang=es, en, fr y de.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Cuántas habitaciones tiene el hotel?','K01'),('¿Admitís mascotas?','K02'),('¿Dónde aparco la moto?','K03'),('¿Tenéis cuna para bebés?','K04'),('¿Hay wifi?','K05'),('¿A qué hora es el check-in?','K06'),('¿Dónde está el hotel?','K07'),('¿Qué ver en Cuenca?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Puedo llevar la bicicleta?','K10'),('¿Organizáis actividades de aventura?','K11'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('How many rooms does the hotel have?','K01'),('Do you accept pets?','K02'),('Where can I park my motorbike?','K03'),('Do you have a cot for babies?','K04'),('Is there wifi?','K05'),('What time is check-in?','K06'),('Where is the hotel?','K07'),('What to see in Cuenca?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('Can I bring my bicycle?','K10'),('Do you organise adventure activities?','K11'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Combien de chambres a l’hôtel ?','K01'),('Acceptez-vous les animaux ?','K02'),('Où garer ma moto ?','K03'),('Avez-vous un lit bébé ?','K04'),('Y a-t-il le wifi ?','K05'),('À quelle heure est l’arrivée ?','K06'),('Où se trouve l’hôtel ?','K07'),('Que voir à Cuenca ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Puis-je venir avec mon vélo ?','K10'),('Organisez-vous des activités d’aventure ?','K11'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Wie viele Zimmer hat das Hotel?','K01'),('Sind Haustiere erlaubt?','K02'),('Wo parke ich mein Motorrad?','K03'),('Gibt es ein Babybett?','K04'),('Gibt es WLAN?','K05'),('Ab wann ist der Check-in?','K06'),('Wo liegt das Hotel?','K07'),('Was kann man in Cuenca sehen?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Kann ich mein Fahrrad mitbringen?','K10'),('Bieten Sie Abenteueraktivitäten an?','K11'),('Was kostet eine Nacht?',None),('Haben Sie ein Schwimmbad?',None)]}
