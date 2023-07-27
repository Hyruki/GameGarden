import discord
from discord import app_commands
from discord.ext import commands


class GameGarden:

    #Discord Fivver

    FVER = discord.Embed(title="Your custom discord Bot here")
    FVER.set_image(url="https://i.imgur.com/PE7s0rR.png")
    FVER.add_field(name="Why do you need to buy your bot here", value="Because all my bot are complete and good according your urge")

    #BASIC
    BASIC = discord.Embed(title="Recherchez vos jeux")
    BASIC.set_thumbnail(url="https://cdn.discordapp.com/icons/1128028794813419651/c53d011e7e4c7cc309efe0fbb0d6d131.png?size=128")
    BASIC.add_field(name="Comment chercher cotre jeux ? ", value="C'est très simple vous n'avez qu'à cliquer sur le boutton juste si dessous et ensuite une fenêtre apparaitra qui vous demandera le nom de votre jeux. Vous n'avez plus qu'à l'écrire pour ensuite l'installer et profiter pleinemennt de votre nouveux jeux video GRATUIT !")

    #GETTING OVER IT
    GOI = discord.Embed(title="Getting over it")
    GOI.set_image(url="https://vignette.wikia.nocookie.net/universe-of-smash-bros-lawl/images/7/7a/Getting_over_it_guy.png/revision/latest?cb=20180121155859")
    GOI.add_field(name="Description", value="Getting Over It est un jeu d’escalade punitif, un hommage au classique de 2002 de Jazzuo 'Sexy Hiking'. Vous déplacez le marteau avec la souris, et c’est tout ce qu’il y a. Avec de la pratique, vous pourrez sauter, vous balancer, grimper et voler. De grands mystères et une merveilleuse récompense attendent les maîtres randonneurs qui atteignent le sommet de la montagne.")
    GOI.add_field(name="Le Lien", value="https://link-target.net/889168/getting-over-it")


    #FNAF1
    FNAF = discord.Embed(title="Five night at Freddy's")
    FNAF.set_image(url="https://th.bing.com/th/id/R.8b44da0db0aba88238d91e75e911e726?rik=YoDK9fX1eb2%2f3Q&riu=http%3a%2f%2flasttokengaming.com%2fwp-content%2fuploads%2f2015%2f08%2f768.png&ehk=90tC4FMkA2xs%2fhMbWK7X2A1Q4APi9ML4YS%2fBXh70VD8%3d&risl=&pid=ImgRaw&r=0")
    FNAF.add_field(name="Description", value="De votre petit bureau, vous devez surveiller attentivement les caméras de sécurité. Vous avez une quantité très limitée d’électricité que vous êtes autorisé à utiliser par nuit (coupes budgétaires d’entreprise, vous savez). Cela signifie que lorsque vous manquez de courant pour la nuit, plus de portes de sécurité et plus de lumières! Si quelque chose ne va pas, à savoir si Freddybear ou ses amis ne sont pas à leur place, vous devez les trouver sur les moniteurs et vous protéger si nécessaire!")
    FNAF.add_field(name="Le Lien", value="https://link-hub.net/889168/fnaf-1")
    

    #SATISFACTORY
    SARY = discord.Embed(title="Satisfactory + Online")
    SARY.set_image(url="https://th.bing.com/th/id/R.d0f1506d454bbf40ec6065762fbb0aac?rik=zxJBx0Oy3e82oA&pid=ImgRaw&r=0")
    SARY.add_field(name="Description", value="Satisfactory est un jeu de construction d’usines en vue à la première personne dans un monde ouvert avec une touche d’exploration et de combats. Jouez seul ou entre amis, explorez une planète inconnue, construisez des usines à plusieurs niveaux et des tapis roulants à l’infini !")
    SARY.add_field(name="Le Lien", value="https://direct-link.net/889168/satisfactory")

    DDLCP = discord.Embed(title="Doki Doki Littérature Club Plus!")
    DDLCP.set_image(url="https://th.bing.com/th/id/OIP.O69WbIryVeCLAM4lfgaMHwHaEP?pid=ImgDet&rs=1")
    DDLCP.add_field(name="Description", value="Bienvenue dans un monde terrifiant de poésie romantique ! Écrivez des poèmes à l'élue de votre cœur et corrigez vos erreurs au fur et à mesure pour atteindre une fin idéale. C'est l'occasion ou jamais de découvrir pourquoi DDLC est l'un des jeux d'horreur psychologique les plus plébiscités de la décennie !")
    DDLCP.add_field(name="Le Lien", value="https://link-hub.net/889168/ddlcplus")
    

    DEVOUR = discord.Embed(title="Devour + Online")
    DEVOUR.set_image(url="https://powerups.es/wp-content/uploads/2021/01/capsule.jpg")
    DEVOUR.add_field(name="Description", value="DEVOUR est un jeu de survie d'horreur en coopération pour 1 à 4 joueurs. Arrêtez des fidèles possédés avant qu'ils ne vous entraînent en enfer. Courez. Criez. Cachez-vous. Mais ne vous faites pas prendre.")
    DEVOUR.add_field(name="Le Lien", value="https://link-center.net/889168/devour-and-online")


    DIA4 = discord.Embed(title="Diablo IV + Online")
    DIA4.set_image(url="https://bnetcmsus-a.akamaihd.net/cms/page_media/xb/XBMMNKOZ8ILU1625080135362.jpg")
    DIA4.add_field(name="Description", value="""Diablo® IV propose une expérience de jeu de rôle et d’action ultime, offrant une quantité inépuisable d’ennemis à abattre, d’innombrables techniques à maîtriser, des donjons cauchemardesques et un butin légendaire. Lancez-vous dans la campagne, en solo ou à plusieurs, et (re)découvrez des personnages emblématiques à travers une histoire captivante et un environnement d’une beauté sombre. Profitez du vaste contenu de haut niveau dans un monde partagé où les joueurs et joueuses se retrouveront dans les villes pour commercer, s’allieront pour combattre les boss hors instance ou se lanceront dans des zones JcJ afin de mettre leurs compétences à l’épreuve contre d’autres personnes, le tout sans passer par des salons. Le cross-play et la progression partagée sont disponibles sur toutes les plateformes.\n Ce n’est que le début pour Diablo® IV : de nouveaux évènements ainsi que de nouvelles histoires, saisons, récompenses et plus encore se profilent à l’horizon.""")
    DIA4.add_field(name="Le Lien", value="https://link-center.net/889168/diablo-iv")

    DSREM = discord.Embed(title="Dark Souls Remastered")
    DSREM.set_image(url="https://th.bing.com/th/id/OIP.KN0YSuui2HTXtGuZnLFakwHaDt?pid=ImgDet&rs=1")
    DSREM.add_field(name="Description", value=""" "Dark Souls Remastered" conserve l'essence de ce qui a fait de "Dark Souls" un classique du jeu vidéo, tout en affinant et améliorant son expérience pour convenir à une nouvelle génération de joueurs. Il offre le même défi brutal et récompense la patience et la stratégie, tout en se délectant de son atmosphère sombre et sa complexité de gameplay qui a rendu le titre original si révolutionnaire.""")
    DSREM.add_field(name="Le Lien", value="https://link-center.net/889168/dark-souls-remaster")