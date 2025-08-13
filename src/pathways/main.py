from pathways.graphdb import get_graphdb_client, init_models, seed_junk_data

def main():
    print("Hello from pathways!")
    client = get_graphdb_client()
    init_models(client)
    seed_junk_data(client)

if __name__ == "__main__":
    main()
