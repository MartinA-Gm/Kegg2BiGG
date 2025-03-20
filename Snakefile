configfile: "config.yaml"

rule all:
    input:
        expand(
            "data/kegg_reaction_{config['reaction_id']}.csv",
            "data/kegg_compound_{config['compound_id']}.csv"
        )

rule fetch_kegg_reaction:
    input:
    output: kegg_reaction_{config["reaction_id"]}.csv
    shell: "python fetch_kegg_reaction.py {config["reaction_id"]}"

rule fetch_kegg_compound:
    input:
    output: kegg_compound_{config["compound_id"]}.csv
    shell: "python fetch_kegg_compound.py {config["compound_id"]}"