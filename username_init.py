import random


database = ['toyname45','phoinex','lolroom','angel','bubbles','shimmer'
,
'angelic'
,
'bubbly'
,
'glimmer'
,
'baby'
,
'pink'
,
'little'
,
'butterfly'
,
'sparkly'
,
'doll'
,
'sweet'
,
'sparkles'
,
'dolly'
,
'sweetie'
,
'sprinkles'
,
'lolly'
,
'princess'
,
'fairy'
,
'honey'
,
'snowflake'
,
'pretty'
,
'sugar'
,
'cherub'
,
'lovely'
,
'blossom'
,
'ecophobia'
,
'hippophobia'
,
'scolionophobia'
,
'ergophobia'
,
'musophobia'
,
'zemmiphobia'
,
'geliophobia'
,
'tachophobia'
,
'hadephobia'
,
'glossophobia'
,
'radiophobia'
,
'triskaidekaphobia','EatBullets','PR0_GGRAM3D','TheSickness','Shoot2Kill','Overkill','Killspree','MindlessKilling','Born2Kill','TheZodiac','ZodiacKiller','Osamaisback',
'Osamaisback','OsamasGhost','T3rr0r1st','ToySoldier','MilitaryMan','DeathSquad','Veteranofdeath','Angelofdeath','Ebola','MustardGas','Knuckles','bullshit']





    

def recom_username_loop():
    recom = []
    for i in range(10):
        data = random.choice(database)
        recom.append(data)
    return recom
    
