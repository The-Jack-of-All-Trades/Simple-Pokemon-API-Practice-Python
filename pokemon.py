import sys
import requests

if len(sys.argv) == 2:
    try:
        api = requests.get(f"https://pokeapi.co/api/v2/pokemon/{sys.argv[1]}")
        pokemon = api.json()

        name = pokemon['name']
        height = pokemon['height']
        weight = pokemon['weight']
        base_experience = pokemon['base_experience']
        print(f"""
Name: {name.title()}
Height: {height}
Weight: {weight}
Base Experience: {base_experience}"""
)

    except requests.RequestException:
        print("Pokemon not found")
        sys.exit()

else:
    print("Format: python pokemon.py pokemon")
    sys.exit()
