import requests
from dataclasses import dataclass
from typing import Union, Optional, Generator, Dict


@dataclass(frozen=True)
class PokemonStats:
    hp: int
    attack: int
    defense: int
    special_attack: int
    special_defense: int
    speed: int


@dataclass(frozen=True)
class BasePokemon:
    name: str


@dataclass(frozen=True)
class Pokemon(BasePokemon):
    id: int
    weight: int
    height: int
    stats: PokemonStats


class PokeError(Exception):
    pass


class PokeAPI:
    BASE_URL: str = 'https://pokeapi.co/api/v2'
    __cache: Dict[int, Pokemon] = {}

    @classmethod
    def get_pokemon(cls, name: Union[int, str]) -> Pokemon:
        if not isinstance(name, (int, str)):
            raise PokeError('Pokémon can be found only via its ID or name')

        for pokemon in cls.__cache.values():
            if pokemon.id == name or pokemon.name == name:
                return pokemon

        url: str = f'{cls.BASE_URL}/pokemon/{name}'
        result: requests.Response = requests.get(url)
        if not result.ok:
            raise PokeError(f'Pokémon {name} is not found')
        result: dict = result.json()
        stats: PokemonStats = PokemonStats(
            **{stat['stat']['name'].replace('-', '_'): stat['base_stat'] for stat in result['stats']}
        )
        pokemon: Pokemon = Pokemon(id=result['id'],
                                   name=result['name'],
                                   weight=result['weight'],
                                   height=result['height'],
                                   stats=stats)
        cls.__cache[pokemon.id] = pokemon
        return pokemon

    @classmethod
    def get_all(cls, get_full=False) -> Generator[Union[BasePokemon, Pokemon], None, None]:
        url: str = f'{cls.BASE_URL}/pokemon'
        result: dict = requests.get(url).json()
        while result['next'] is not None:
            for pokemon in result['results']:
                if get_full:
                    yield cls.get_pokemon(pokemon['name'])
                else:
                    yield BasePokemon(pokemon['name'])
            url = result['next']
            result = requests.get(url).json()


def main():
    ditto: Pokemon = PokeAPI.get_pokemon('ditto')
    print(ditto)

    heaviest: Optional[Pokemon] = None
    for i, pokemon in zip(range(50), PokeAPI.get_all(True)):
        print(i, pokemon)
        heaviest = pokemon if heaviest is None else max(heaviest, pokemon, key=lambda x: x.weight)

    print(heaviest)


if __name__ == '__main__':
    main()
