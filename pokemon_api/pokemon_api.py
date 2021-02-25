import requests

class httpComponent:

    def get(url):
        return requests.get(url).json()

    def getWithParams(url,payload):
        return requests.get(url, params = payload).json()
    
class PokemonFinder:

    def getPokemonList():
        return httpComponent.get('https://pokeapi.co/api/v2/pokemon/')

    def printFirstTenPokemons(list):
        for index,pokemon in enumerate(list):
            if index == 9:
                break
            print(pokemon['name'])

    def printLastTenTenPokemons(list):
        list = list[::-1]
        for index,pokemon in enumerate(list):
            print(pokemon['name'])
            if index == 9:
                break

    def printPokemonURLByName(pokemonList, name):
        for pokemon in pokemonList:
            if pokemon['name'] == name:
                print(pokemon['url'])

pokemonList = PokemonFinder.getPokemonList()
pokemonList = pokemonList['results']
PokemonFinder.printFirstTenPokemons(pokemonList)
PokemonFinder.printLastTenTenPokemons(pokemonList)
PokemonFinder.printPokemonURLByName(pokemonList,'metapod')