# Pathways

Writing in Python cuz I want to actually finish a project for once.

Rewrite it in Rust or some shit. I don't care. Just make sure it works. Then force me to finally learn Rust.

Very much still WiP. Will throw out a release tag when it's worth looking at.

## Setup

```shell
uv sync
docker compose up -d
```
 
Visit https://ratel.hypermode.com in the browser. Enter `http://localhost:8080` as the server.

Run the below query:

```
query get_pathway_io_molecules ($pathway : string = "Glycolysis")
{
  interactionList(func: type(Pathway)) @filter(eq(name, $pathway)) {
    uid
    name
    interaction {
      name
      input {
        uid
        name
      }
      output {
        uid
        name
      }
    }
  }
}
```