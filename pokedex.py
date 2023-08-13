import sys
import json
import requests
import pokemon_colorscripts
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def main(name):
    """General search function"""
    try:
        url=f'https://pokeapi.co/api/v2/pokemon/{name}'
        get_mon(name)
    except:
        try:
            get_info(name)  
        except:
            try:
                get_move(name)
            except:
                print("no can do boss")
                return

def get_mon(pokemon):
        # pokemon_colorscripts.pokemon_colorscripts(f" -n {pokemon}")
        """Returns Abilitis,type and stats of pokemon"""
        url=f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
        response=requests.get(url).content
        data=json.loads(response)
        types=data['types']
        abilities=data[f'abilities']
        stats=data['stats']
        print(color.BOLD+color.RED+'Type'+color.END,end='  ')
        for type in types:
            print(type['type']['name'].capitalize(),end='   ')
        print('\n'+color.BOLD+color.RED+'Abilities'+color.END,end='  ')
        for ability in abilities: 
            print(ability['ability']['name'].capitalize(),end='   ')
            # get_info(ability['ability']['name'])
        print_stats(stats)
        print('\n')

        return

def get_info(abliliy):
    url=f'https://pokeapi.co/api/v2/ability/{abliliy}'
    response=requests.get(url).content
    info=json.loads(response)
    effect=info['effect_entries'][1]['effect'].strip('\n')
    effect=''.join(effect.split('\n'))
    print(color.BOLD+color.RED+f'{abliliy.capitalize()}'+color.END)
    print(effect)
    print()
    # print(info)
    return

def get_move(move):
    """Returns info on moves"""
    url=f'https://pokeapi.co/api/v2/move/{move}'
    response=requests.get(url).content
    info=json.loads(response)
    print(color.BOLD+color.RED+f'{move.capitalize()}'+color.END)
    print(color.BOLD+'Damage: '+color.END,info['pp'])
    print(color.BOLD+'Accuracy: '+color.END,info['accuracy'])
    print(color.BOLD+'Damage-type: '+color.END+info['damage_class']['name'])
    print(color.BOLD+'Type: '+color.END+info['type']['name'])
    return

def print_stats(stats):
    print('\n'+color.RED+color.BOLD+'Stats'+color.END)
    # for stat in stats:
        # print(stat['stat']['name'].capitalize()+':  ',stat['base_stat'])
    print('Hp       ',"{0:0=3d}".format(stats[0]['base_stat']),end='   ')
    bar_graph(stats[0]['base_stat'])
    print('Attack   ',"{0:0=3d}".format(stats[1]['base_stat']),end='   ')
    bar_graph(stats[1]['base_stat'])
    print('Defence  ',"{0:0=3d}".format(stats[2]['base_stat']),end='   ')
    bar_graph(stats[2]['base_stat'])
    print('Sp Attack',"{0:0=3d}".format(stats[3]['base_stat']),end='   ')
    bar_graph(stats[3]['base_stat'])
    print('Sp Def   ',"{0:0=3d}".format(stats[4]['base_stat']),end='   ')
    bar_graph(stats[4]['base_stat'])
    print('Speed    ',"{0:0=3d}".format(stats[5]['base_stat']),end='   ')
    bar_graph(stats[5]['base_stat'])
    print('BST      ',stats[0]['base_stat']+stats[1]['base_stat']+stats[2]['base_stat']+stats[3]['base_stat']+stats[4]['base_stat']+stats[5]['base_stat'])
    return

def bar_graph(stat):
    fill='█'
    filledLength = int(stat//6)
    bar = fill * filledLength + '-' * (50 - filledLength)
    print(f'{bar}')

if __name__=='__main__':
    name=sys.argv[1]
    # # info=sys.argv[2]
    main(name)
    pokemon_colorscripts.show_pokemon_by_name(name,False,False,False)
    # get_mon(name)
    # bar_graph(60)