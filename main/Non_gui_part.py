#Ayanabha
from gui_part import *
def slelect_random_word():
    import random
    myWords=['Apple','Apricot','Avocado','Banana','Blackberry','Blueberry','Cantaloupe','Cherry','Coconut','Cranberry','Date',
             'Dragonfruit','Elderberry','Fig','Grape','Grapefruit','Guava','Honeydew','Kiwi','Lemon','Lime','Lychee','Mango','Mandarin',
             'Melon','Mulberry','Nectarine','Orange','Papaya','Peach','Pear','Pineapple','Plum','Pomegranate','Raspberry','Strawberry',
             'Tangerine','Watermelon','Rose','Daisy','Lily','Sunflower','Tulip','Orchid','Iris','Carnation','Chrysanthemum','Peony','Marigold','Hydrangea',
             'Daffodil','Pansy','Zinnia','Snapdragon','Poppy','Lavender','Geranium','Petunia','Begonia','Fuchsia','Gladiolus','Afghanistan','Albania','Algeria',
             'AndorraAngola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus',
             'Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cabo Verde',
             'Cambodia','Cameroon','Canada','Central African Republic (CAR)','Chad','Chile','China','Colombia','Comoros','Costa Rica','Cote d Ivoire','Croatia''Cuba',
             'Cyprus','Czech Republic','Democratic Republic of the Congo','Denmark','Djibouti','Dominica','Dominican Republic','Ecuador','Egypt','El Salvador',
             'Equatorial Guinea','Eritrea','Estonia','Eswatini (formerly Swaziland)','Ethiopia','Fiji','Finland','France','Gabon','Gambia','Georgia','Germany','Ghana',
             'Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel',
             'Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Kosovo','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya',
             'Liechtenstein','Lithuania','Luxembourg','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico',
             'Micronesia','Moldova','Monaco','Mongolia','Montenegro','Morocco','Mozambique','Myanmar (formerly Burma)','Namibia','Nauru','Nepal','Netherlands','New Zealand',
             'Nicaragua','Niger','Nigeria','North Korea','North Macedonia (formerly Macedonia)','Norway','Oman','Pakistan','Palau','Palestine','Panama','Papua New Guinea',
             'Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines',
             'Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands',
             'Somalia','South Africa','South Korea','South Sudan','Spain','Sri Lanka','Sudan','Suriname','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand',
             'Timor-Leste (formerly East Timor)','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates (UAE)',
             'United Kingdom (UK)','United States of America (USA)','Uruguay','Uzbekistan','Vanuatu','Vatican City (Holy See)','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe']
    
    random_items=random.choice(myWords)
    print(random_items)
    pass 
def check_score():
    pass#returns score (how many times won,lost)
def check_letter():
    pass#returns true when letter in word else returns false
def check_rem_attempts():
    pass#returns remaining no of attempts
def main():
    pass#main game(loop)
#call take_input when input is required no need to define it it is defined in gui_part
a=select_random_word()
print(a)