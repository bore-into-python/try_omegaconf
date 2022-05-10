from omegaconf import OmegaConf
from pathlib import Path
import hydra
import sys

OmegaConf.register_new_resolver("path", Path)

def param_resolver(param_name, default, descr):
    print(f'Descr = {descr}')
    argv = sys.argv
    for arg in argv:
        key, _, val = arg.partition('=')
        if key == param_name:
            return val
    return default

OmegaConf.register_new_resolver("cli", param_resolver)
    



cli_conf = OmegaConf.from_cli()

conf = OmegaConf.load("conf.yaml")
conf2 = OmegaConf.create({})
from contextlib import suppress
with suppress(FileNotFoundError):
    conf2 = OmegaConf.load("conf_prod.yaml")



    
#print(OmegaConf.to_yaml(conf))

config = OmegaConf.merge(conf, conf2, cli_conf)

#print(conf.list)
#print(conf.the_host)
#print(conf.docs)
#print(conf.b)



