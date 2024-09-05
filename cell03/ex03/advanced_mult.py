#!/usr/bin/env python3

import sys

if(len(sys.argv) - 1 == 0) :
    table_de = 0
    while table_de <= 10 :

        print(f"Table de {table_de}:", end='')
        cinitel = 0
        while cinitel <= 10 :
            print(f" {table_de * cinitel}", end='')
            cinitel += 1
        print("")
        table_de += 1
else :
    print("none")



